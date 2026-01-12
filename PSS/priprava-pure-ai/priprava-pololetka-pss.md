# Příprava na pololetní písemnou práci z PSS

Tento dokument slouží jako souhrnná příprava na písemku. Obsahuje vysvětlení pojmů a konfigurační příkazy pro témata: OSPF, VLAN, NAT, L2 Security, HSRP a Etherchannel.

---

## OSPF (Open Shortest Path First)

OSPF je link-state směrovací protokol, který používá metriku "cost" (založenou na šířce pásma) k určení nejlepší cesty. Routery si vyměňují informace o topologii sousedům a udržují si kompletní mapu sítě (LSDB).

**Klíčové pojmy:**
*   **Process ID:** Číslo procesu na routeru (lokální význam).
*   **Area:** Logické rozdělení sítě. Vždy musí existovat páteřní oblast (Area 0), na kterou jsou napojeny ostatní oblasti.
*   **Wildcard maska:** Inverzní maska (např. 255.255.255.0 -> 0.0.0.255).
*   **Passive Interface:** Rozhraní, kde OSPF neběží, ale jeho síť je propagována.
*   **Router ID:** Jedinečný identifikátor routeru (nejvyšší IP loopbacku nebo aktivního fyzického rozhraní, nebo manuálně nastaveno).

### Konfigurace OSPF

#### Základní nastavení OSPF
Tento blok povolí OSPF na routeru a specifikuje sítě, které se mají účastnit směrování.

```text
enable
configure terminal
router ospf 1
 router-id 1.1.1.1
 network 192.168.10.0 0.0.0.255 area 0
 network 10.0.0.0 0.0.0.3 area 0
 passive-interface GigabitEthernet0/1
 auto-cost reference-bandwidth 1000
exit
```

#### Propagace výchozí cesty (Default Route)
Pokud router má výchozí cestu (např. do internetu), může ji poslat ostatním OSPF routerům.

```text
enable
configure terminal
router ospf 1
 default-information originate
exit
```

### Ověření konfigurace

#### Zobrazení sousedů a nastavení
Ověří, zda se vytvořilo sousedství (stav by měl být FULL nebo 2WAY).

```text
show ip ospf neighbor
show ip ospf interface brief
show ip route ospf
```

---

## VLAN (Virtual LAN)

VLAN logicky rozděluje fyzický switch na více virtuálních sítí. Zařízení v různých VLAN spolu nemohou komunikovat bez routeru (L3 zařízení).

**Klíčové pojmy:**
*   **Access port:** Přenáší provoz pouze jedné VLAN (připojení PC).
*   **Trunk port:** Přenáší provoz více VLAN (propojení switch-switch nebo switch-router). Používá 802.1q tagování.
*   **Native VLAN:** VLAN, která na trunku není tagovaná (z bezpečnostních důvodů by měla být změněna z defaultní VLAN 1).
*   **ROAS (Router on a Stick):** Způsob směrování mezi VLAN pomocí jednoho fyzického rozhraní routeru rozděleného na sub-interface.

### Konfigurace VLAN

#### Vytvoření VLAN a přiřazení portů (Switch)
Vytvoří VLANy a přiřadí fyzické porty do konkrétních VLAN.

```text
enable
configure terminal
vlan 10
 name ZAMESTNANCI
vlan 20
 name HOSTE
exit

interface range FastEthernet0/1-10
 switchport mode access
 switchport access vlan 10
exit

interface range FastEthernet0/11-20
 switchport mode access
 switchport access vlan 20
exit
```

#### Nastavení Trunku (Switch)
Nastaví port pro přenos všech (nebo vybraných) VLAN.

```text
enable
configure terminal
interface GigabitEthernet0/1
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,99
exit
```

#### Inter-VLAN Routing - Router on a Stick (Router)
Nastavení sub-interfaců na routeru pro komunikaci mezi VLANami.

```text
enable
configure terminal
interface GigabitEthernet0/0
 no shutdown
exit

interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
exit

interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
exit
```

### Ověření konfigurace

#### Kontrola VLAN a Trunků
Ověří existenci VLAN, přiřazení portů a stav trunk linek.

```text
show vlan brief
show interfaces trunk
show ip interface brief
```

---

## NAT (Network Address Translation)

NAT překládá privátní IP adresy (vnitřní síť) na veřejné IP adresy (internet). Umožňuje šetřit veřejné IPv4 adresy.

**Typy NAT:**
*   **Static NAT:** 1:1 mapování (jedna privátní IP na jednu veřejnou IP). Používá se pro servery přístupné zvenčí.
*   **Dynamic NAT:** Mapování privátních IP na skupinu (pool) veřejných IP.
*   **PAT (Port Address Translation) / NAT Overload:** Mnoho privátních IP na jednu (nebo několik) veřejných IP s využitím portů. Nejčastější doma a ve firmách.

### Konfigurace NAT

#### Definice Inside a Outside rozhraní
Nutný krok pro všechny typy NAT. Router musí vědět, kde je vnitřní a kde vnější síť.

```text
enable
configure terminal
interface GigabitEthernet0/0
 ip nat inside
exit

interface GigabitEthernet0/1
 ip nat outside
exit
```

#### Static NAT (1:1)
Příklad: Zpřístupnění interního serveru 192.168.10.10 na veřejné IP 203.0.113.10.

```text
enable
configure terminal
ip nat inside source static 192.168.10.10 203.0.113.10
exit
```

#### PAT (Overload)
Nejběžnější scénář. Překlad celé sítě 192.168.10.0/24 na adresu vnějšího rozhraní (např. G0/1). Vyžaduje Access List (ACL) pro definici provozu.

```text
enable
configure terminal
access-list 1 permit 192.168.10.0 0.0.0.255
ip nat inside source list 1 interface GigabitEthernet0/1 overload
exit
```

### Ověření konfigurace

#### Zobrazení tabulky překladů
Zobrazí aktuální aktivní překlady.

```text
show ip nat translations
show ip nat statistics
```

---

## L2 Security (Zabezpečení na 2. vrstvě)

Zabezpečení switche proti útokům jako MAC Flooding (přeplnění CAM tabulky) nebo Rogue DHCP server (falešný DHCP server).

**Techniky:**
*   **Port Security:** Omezuje počet MAC adres na portu. Chrání proti MAC flooding.
*   **DHCP Snooping:** Rozlišuje porty na "trusted" (důvěryhodné - tam je DHCP server) a "untrusted" (nedůvěryhodné - tam jsou klienti). Chrání proti Rogue DHCP.

### Konfigurace L2 Security

#### Port Security
Zapnutí na access portu. Nastavíme max 1 MAC adresu a při porušení vypnutí portu (shutdown).

```text
enable
configure terminal
interface FastEthernet0/1
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation shutdown
exit
```

#### DHCP Snooping
Globálně zapne DHCP snooping a určí trusted port (kde je připojen pravý DHCP server nebo router).

```text
enable
configure terminal
ip dhcp snooping
ip dhcp snooping vlan 1
interface GigabitEthernet0/1
 ip dhcp snooping trust
exit
```

### Ověření konfigurace

#### Kontrola Port Security a DHCP Snooping
Zobrazí stav zabezpečení portů a tabulku DHCP snoopingu.

```text
show port-security interface FastEthernet0/1
show ip dhcp snooping
show ip dhcp snooping binding
```

---

## HSRP (Hot Standby Router Protocol)

HSRP je Cisco proprietární protokol pro redundanci výchozí brány (Gateway). Umožňuje spojit více routerů do jednoho virtuálního routeru.

**Klíčové pojmy:**
*   **Active Router:** Směruje data.
*   **Standby Router:** Čeká a sleduje Active router. Pokud Active vypadne, převezme jeho roli.
*   **Virtual IP:** Adresa, kterou mají PC nastavenou jako Default Gateway.
*   **Priority:** Určuje, kdo bude Active (vyšší vyhrává). Default je 100.
*   **Preempt:** Umožní routeru s vyšší prioritou převzít roli Active, i když už existuje jiný Active router (např. po restartu hlavního routeru).

### Konfigurace HSRP

#### Konfigurace Active Routeru (R1)
Nastavíme vyšší prioritu (např. 150) a zapneme preempt.

```text
enable
configure terminal
interface GigabitEthernet0/0
 ip address 192.168.1.2 255.255.255.0
 standby 1 ip 192.168.1.1
 standby 1 priority 150
 standby 1 preempt
exit
```

#### Konfigurace Standby Routeru (R2)
Necháme defaultní prioritu (100).

```text
enable
configure terminal
interface GigabitEthernet0/0
 ip address 192.168.1.3 255.255.255.0
 standby 1 ip 192.168.1.1
exit
```

### Ověření konfigurace

#### Kontrola stavu HSRP
Zobrazí, který router je Active a který Standby.

```text
show standby brief
show standby
```

---

## Etherchannel (Link Aggregation)

Etherchannel spojuje více fyzických linek do jedné logické linky. Zvyšuje propustnost a poskytuje redundanci (když jedna linka spadne, ostatní jedou dál).

**Protokoly:**
*   **PAgP (Port Aggregation Protocol):** Cisco proprietární (`desirable` / `auto`).
*   **LACP (Link Aggregation Control Protocol):** Standard IEEE 802.3ad (`active` / `passive`).
*   **Static (ON):** Bez protokolu (`on`).

**Důležité:** Všechny porty v Etherchannelu musí mít shodné nastavení (rychlost, duplex, VLAN, Trunk mód).

### Konfigurace Etherchannelu

#### LACP Konfigurace (Standard)
Nastavíme na obou stranách na `active` (nebo jednu stranu `active` a druhou `passive`).

```text
enable
configure terminal
interface range GigabitEthernet0/1-2
 channel-group 1 mode active
exit
```

#### Konfigurace Port-Channel rozhraní
Po vytvoření skupiny se vytvoří virtuální interface `Port-channel 1`. Ten se konfiguruje místo fyzických portů (např. jako Trunk).

```text
interface Port-channel 1
 switchport mode trunk
 switchport trunk allowed vlan 10,20
exit
```

#### Layer 3 Etherchannel (na routeru nebo L3 switchi)
Porty se nesmí chovat jako switchporty (`no switchport`).

```text
enable
configure terminal
interface range GigabitEthernet0/1-2
 no switchport
 channel-group 1 mode active
exit

interface Port-channel 1
 ip address 10.0.0.1 255.255.255.252
exit
```

### Ověření konfigurace

#### Kontrola stavu Etherchannelu
Zobrazí souhrn o skupinách a stavu portů.

```text
show etherchannel summary
```
