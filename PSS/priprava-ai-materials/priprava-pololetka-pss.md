# Příprava na pololetní písemnou práci PSS

Tento dokument slouží jako souhrnná příprava na test. Obsahuje teorii, konfigurační příkazy a vysvětlení klíčových pojmů pro témata: OSPF, VLAN, NAT, L2 bezpečnost, HSRP a EtherChannel.

---

## 1. OSPF (Open Shortest Path First)

### Teorie
OSPF je link-state směrovací protokol, který používá metriku "cost" (založenou na šířce pásma) pro výpočet nejkratší cesty.
Základní vlastnosti:
- **Link-State protokol**: Každý router zná topologii celé oblasti.
- **Hierarchický návrh**: Používá oblasti (Areas) pro škálování. Páteřní oblast je Area 0. Všechny ostatní oblasti se musí připojovat k Area 0.
- **Rychlá konvergence**: Rychle reaguje na změny v síti.
- **Dijkstrův algoritmus**: Používán pro výpočet nejkratší cesty.

#### Doplňující otázky
**1. Co je to Area (oblast)?**
Představ si to jako **škálování**. Kdyby byla celá obrovská síť v jedné "placce", každý router by se zbláznil z množství informací o každé malé změně na druhém konci světa.

* **Area** je logická skupina routerů.
* Uvnitř Area znají routery detailní mapu sebe navzájem.
* Mezi oblastmi se posílají jen "souhrny" (summary), což šetří výkon routerů.

**2. Jak se počítá vzdálenost?**
OSPF nepoužívá počet skoků (jako RIP), ale metriku zvanou **Cost** (cena).

* Tato cena se vypočítá na základě **šířky pásma** (rychlosti linky, bandwidth).
* Cílem Dijkstrova algoritmu je najít cestu s nejnižším součtem těchto cen.

### Konfigurace (IPv4)

#### Základní nastavení procesu na routeru
```bash
Router(config)# router ospf 10          # 10 je Process ID (label)
Router(config-router)# router-id 1.1.1.1 # Unikátní identifikátor routeru
```

#### Přidání sítí do OSPF (klasický způsob)
```bash
# network Process_ID Síť Wildcard_maska Oblast
Router(config-router)# network 10.10.1.0 0.0.0.255 area 0  # Wildcard maska (inverzní maska)
```
Pozor: Wildcard maska pro /30 (255.255.255.252) je 0.0.0.3.

#### Nastavení OSPF přímo na rozhraní (modernější způsob)
```bash
Router(config)# interface g0/0/0
Router(config-if)# ip ospf 10 area 0    # Zapne OSPF proces 10 pro Area 0 na tomto rozhraní
```

#### Pasivní rozhraní
Zabrání odesílání OSPF Hello paketů na rozhraní, kde nejsou další routery (bezpečnost a efektivita).
```bash
Router(config-router)# passive-interface g0/0/1
# nebo pro všechny a pak povolit konkrétní:
Router(config-router)# passive-interface default
Router(config-router)# no passive-interface g0/0/0
```

#### Propagace defaultní routy
Pokud má router defaultní routu (např. do internetu), může ji poslat ostatním.
```bash
Router(config-router)# default-information originate
```

#### Point-to-Point síť
Na spojích mezi dvěma routery (bez switche) se nevolí DR/BDR, což zrychluje konvergenci.
```bash
Router(config-if)# ip ospf network point-to-point
```

### Konfigurace (IPv6) - OSPFv3
Nutné povolit IPv6 routing: `ipv6 unicast-routing`.

```bash
Router(config)# ipv6 router ospf 10
Router(config-rtr)# router-id 1.1.1.1
Router(config)# interface g0/0/0
Router(config-if)# ipv6 ospf 10 area 0
```

### Ověření / Troubleshooting
- `show ip protocols`: Zobrazí běžící protokoly, Router ID, sítě.
- `show ip ospf neighbor`: Zobrazí sousedy (stav by měl být FULL nebo 2WAY).
- `show ip route`: Zobrazí směrovací tabulku (OSPF cesty označené jako 'O').
- `clear ip ospf process`: Restartuje OSPF proces (vynutí znovunavázání sousedství).

---

## 2. VLAN (Virtual LAN)

### Teorie
VLAN (Virtual Local Area Network) umožňuje logicky rozdělit jednu fyzickou síť (L2) na více oddělených sítí (broadcastových domén).
- **Výhody**: Bezpečnost (oddělení provozu), snížení broadcastového provozu, flexibilita.
- **Trunking (802.1Q)**: Propojení mezi switchi přenášející více VLAN. Rámce jsou "tagovány" (přidána značka s číslem VLAN).
- **Native VLAN**: Nenetagovaná VLAN na trunku (by default VLAN 1). Oba konce trunku musí mít stejnou Native VLAN.
- **DTP (Dynamic Trunking Protocol)**: Cisco protokol pro automatické vyjednání trunku.
- **VTP (VLAN Trunking Protocol)**: Umožňuje centrálně spravovat VLAN databázi (Server) a replikovat ji na ostatní switche (Client).

### Konfigurace

#### Vytvoření VLAN
```bash
Switch(config)# vlan 10
Switch(config-vlan)# name ZAMESTNANCI
```

#### Přiřazení portu do VLAN (Access port)
```bash
Switch(config)# interface f0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
```

#### Konfigurace Trunku
```bash
Switch(config)# interface g0/1
Switch(config-if)# switchport trunk encapsulation dot1q  # Někdy nutné (starší modely podporují i ISL)
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk native vlan 99       # Změna native VLAN (bezpečnost)
Switch(config-if)# switchport trunk allowed vlan 10,20,99 # Povolení konkrétních VLAN
```

#### Konfigurace VTP
```bash
Switch(config)# vtp domain MOJE_DOMENA
Switch(config)# vtp mode server          # nebo client, transparent
Switch(config)# vtp password TAJNE_HESLO
```
*Pozor: VTP Server přepisuje databázi Clientů podle vyššího Revision Number. Nový switch v síti může smazat všechny VLANy, pokud má vyšší číslo revize!*

#### Inter-VLAN Routing (Router-on-a-stick)
Propojení VLAN mezi sebou pomocí routeru.
```bash
Router(config)# interface g0/0.10        # Subinterface
Router(config-subif)# encapsulation dot1Q 10  # Přiřazení k VLAN 10
Router(config-subif)# ip address 192.168.10.1 255.255.255.0
```

#### Inter-VLAN Routing (L3 Switch - SVI)
```bash
Switch(config)# ip routing               # Povolení routování
Switch(config)# interface vlan 10        # SVI (Switch Virtual Interface)
Switch(config-if)# ip address 192.168.10.1 255.255.255.0
Switch(config-if)# no shutdown
```

---

## 3. NAT (Network Address Translation)

### Teorie
NAT překládá IP adresy v hlavičce paketu (typicky privátní na veřejné). To šetří veřejné IPv4 adresy a zvyšuje bezpečnost (skrývá vnitřní topologii).

#### Typy NAT
1.  **Static NAT**: 1:1 mapování (jedna privátní IP na jednu veřejnou IP). Používá se pro servery přístupné z internetu.
2.  **Dynamic NAT**: Mapování z poolu veřejných adres. (Mnoho k Mnoho).
3.  **PAT (Port Address Translation) / NAT Overload**: Mapování mnoha privátních adres na jednu veřejnou IP pomocí unikátních zdrojových portů. Nejčastější v domácnostech.

### Konfigurace (Cisco)

#### Definice rozhraní
Nejprve musíme určit, kde je vnitřní (inside) a vnější (outside) síť.
```bash
Router(config)# interface g0/0
Router(config-if)# ip nat inside

Router(config)# interface g0/1
Router(config-if)# ip nat outside
```

#### Static NAT (1:1)
```bash
Router(config)# ip nat inside source static 192.168.1.10 209.165.200.225
```

#### Dynamic NAT (Pool)
```bash
Router(config)# ip nat pool MY_POOL 209.165.200.226 209.165.200.240 netmask 255.255.255.224
Router(config)# access-list 1 permit 192.168.1.0 0.0.0.255
Router(config)# ip nat inside source list 1 pool MY_POOL
```

#### PAT (NAT Overload)
Použití jedné veřejné IP na rozhraní.
```bash
Router(config)# access-list 1 permit 192.168.1.0 0.0.0.255
Router(config)# ip nat inside source list 1 interface g0/1 overload
```
*Klíčové slovo `overload` zapíná PAT.*

### Konfigurace (Linux iptables)
Linux používá `iptables` (nebo novější `nftables`). Pravidla se píší do tabulky `nat`, řetězec `POSTROUTING` (pro SNAT) nebo `PREROUTING` (pro DNAT).

#### Maškaráda (SNAT - Source NAT)
Odpovídá PAT. Překládá odchozí provoz na IP adresu odchozího rozhraní.
```bash
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```
*-t nat (tabulka nat), -A POSTROUTING (přidat do řetězce), -o eth0 (výstupní interface), -j MASQUERADE (cíl).*

#### Port Forwarding (DNAT - Destination NAT)
Přístup zvenku na vnitřní server (ekvivalent Static NAT s portem).
```bash
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination 192.168.1.50:80
```

#### Zobrazení tabulky NAT
```bash
iptables -t nat -L -n -v
```

---

## 4. L2 Bezpečnost (L2 Security)

### Teorie
Zabezpečení na 2. vrstvě (Data Link Layer) je klíčové, protože útoky zde mohou ohrozit celou síťovou infrastrukturu.

#### Typy útoků a mitigace
1.  **MAC Address Table Flooding**: Útočník zaplní CAM tabulku falešnými MAC adresami, switch se změní v hub a posílá vše všude. -> *Obrana: Port Security.*
2.  **DHCP Starvation / Spoofing**: Vyčerpání adres nebo podvržení falešného DHCP serveru (Man-in-the-Middle). -> *Obrana: DHCP Snooping.*
3.  **ARP Spoofing / Poisoning**: Útočník se vydává za gateway MAC. -> *Obrana: Dynamic ARP Inspection (DAI).*
4.  **VLAN Hopping**: Útok na DTP nebo tagování rámců pro přístup do jiné VLAN. -> *Obrana: Vypnout DTP, nastavit Native VLAN.*
5.  **STP Attacks**: Manipulace s topologií (podvržení Root Bridge). -> *Obrana: BPDU Guard, Root Guard.*

### Konfigurace

#### Port Security
Omezí počet MAC adres na portu nebo povolí jen konkrétní.
```bash
Switch(config)# interface f0/1
Switch(config-if)# switchport mode access  # Musí být access port
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security maximum 2
Switch(config-if)# switchport port-security mac-address sticky
Switch(config-if)# switchport port-security violation shutdown  # (nebo restrict, protect)
```
*Pozn: `sticky` se naučí aktuální MAC a uloží ji do konfigurace.*

#### DHCP Snooping
Rozlišuje porty na **Trusted** (DHCP server, uplink) a **Untrusted** (klienti). Zahazuje DHCP Offer z untrusted portů.
```bash
Switch(config)# ip dhcp snooping
Switch(config)# ip dhcp snooping vlan 10
Switch(config)# interface g0/1             # Uplink k serveru
Switch(config-if)# ip dhcp snooping trust
```

#### Dynamic ARP Inspection (DAI)
Ověřuje ARP pakety proti vazbám z DHCP Snooping databáze.
```bash
Switch(config)# ip arp inspection vlan 10
Switch(config)# interface g0/1             # Uplink
Switch(config-if)# ip arp inspection trust
```

#### Mitigace STP útoků (BPDU Guard / PortFast)
Zapnout na portech pro koncová zařízení. Pokud přijde BPDU (znak switche), port se vypne.
```bash
Switch(config)# interface f0/1
Switch(config-if)# spanning-tree portfast
Switch(config-if)# spanning-tree bpduguard enable
```

---

## 5. HSRP (Hot Standby Router Protocol)

### Teorie
FHRP (First Hop Redundancy Protocol). HSRP je proprietární protokol Cisco pro redundanci výchozí brány (Gateway).
Dovoluje více routerům sdílet jednu virtuální IP adresu a MAC adresu, kterou používají koncoví klienti jako svou bránu.

#### Klíčové pojmy
- **Virtual IP**: Adresa brány nastavená na PC. Není přiřazena fyzickému interfacu, ale HSRP skupině.
- **Active Router**: Router, který aktuálně posílá pakety. (Ten s nejvyšší prioritou).
- **Standby Router**: Router, který čeká a monitoruje Active router. Převezme roli, pokud Active selže.
- **Priority**: Určuje Active router. Default je 100. Vyšší vyhrává.
- **Preemption**: Pokud je zapnuto, router s vyšší prioritou okamžitě převezme roli Active (i když už jeden běží). Defaultně vypnuto.
- **HSRP Version**: V1 (default, skupina multicast 224.0.0.2), V2 (podpora IPv6, multicast 224.0.0.102).

### Konfigurace

#### Základní nastavení
Nastavuje se na interfacu (nebo subinterfacu/SVI), který je bránou pro LAN.

**R1 (Active):**
```bash
R1(config)# interface g0/1
R1(config-if)# ip address 192.168.1.2 255.255.255.0  # Fyzická IP
R1(config-if)# standby 1 ip 192.168.1.1              # Virtuální IP (Skupina 1)
R1(config-if)# standby 1 priority 150                # Vyšší priorita -> bude Active
R1(config-if)# standby 1 preempt                     # Převezme roli, když se vrátí online
```

**R2 (Standby):**
```bash
R2(config)# interface g0/1
R2(config-if)# ip address 192.168.1.3 255.255.255.0  # Fyzická IP
R2(config-if)# standby 1 ip 192.168.1.1              # Stejná virtuální IP
R2(config-if)# standby 1 priority 100                # Default (nižší než R1)
R2(config-if)# standby 1 preempt                     # Doporučeno i zde
```

#### Ověření
```bash
R1# show standby brief
R1# show standby
```
Výpis ukáže stav (Active/Standby), Virtuální IP, a kdo je Active router.

---

## 6. EtherChannel

### Teorie
EtherChannel je technologie pro agregaci linek (link aggregation). Umožňuje spojit více fyzických linek do jedné logické (Port-Channel).
- **Výhody**: Vyšší propustnost (load balancing), redundance (pokud jedna linka spadne, ostatní jedou), STP vidí jen jednu linku (žádné blokování smyček).
- **Protokoly**:
    - **PAgP (Port Aggregation Protocol)**: Cisco proprietární. Módy: `auto`, `desirable`.
    - **LACP (Link Aggregation Control Protocol) 802.3ad**: Průmyslový standard. Módy: `passive`, `active`.
    - **ON (Static)**: Bez vyjednávání.

#### Podmínky pro vytvoření
Všechny porty v channelu musí mít shodné nastavení:
- Rychlost a Duplex.
- VLAN mód (access/trunk).
- Native VLAN a povolené VLANy (u trunku).

### Konfigurace

#### L2 EtherChannel (LACP)
```bash
Switch(config)# interface range g0/1 - 2
Switch(config-if-range)# channel-group 1 mode active    # Vytvoří interface Port-channel 1
Switch(config-if-range)# exit

Switch(config)# interface port-channel 1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20
```

#### L3 EtherChannel (Routed Port)
Na L3 switchi. Interface má IP adresu, ne switchport.
```bash
Switch(config)# interface range g0/1 - 2
Switch(config-if-range)# no switchport               # Změní na L3 port
Switch(config-if-range)# channel-group 1 mode active
Switch(config-if-range)# exit

Switch(config)# interface port-channel 1
Switch(config-if)# ip address 192.168.1.1 255.255.255.0
```

### Ověření
```bash
Switch# show etherchannel summary
```
Hledáme flag **SU** (S = Layer2, U = In Use) nebo **RU** (R = Layer3, U = In Use).
Flag **D** (Down) nebo **I** (Stand-alone) značí chybu.
