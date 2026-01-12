# Etherchannel (Link Aggregation)

Etherchannel spojuje více fyzických linek do jedné logické linky. Zvyšuje propustnost a poskytuje redundanci (když jedna linka spadne, ostatní jedou dál).

**Protokoly:**
*   **PAgP (Port Aggregation Protocol):** Cisco proprietární (`desirable` / `auto`).
*   **LACP (Link Aggregation Control Protocol):** Standard IEEE 802.3ad (`active` / `passive`).
*   **Static (ON):** Bez protokolu (`on`).

**Důležité:** Všechny porty v Etherchannelu musí mít shodné nastavení (rychlost, duplex, VLAN, Trunk mód).

## Konfigurace Etherchannelu

### LACP Konfigurace (Standard)
Nastavíme na obou stranách na `active` (nebo jednu stranu `active` a druhou `passive`).

```text
enable
configure terminal
interface range GigabitEthernet0/1-2
 channel-group 1 mode active
exit
```

### Konfigurace Port-Channel rozhraní
Po vytvoření skupiny se vytvoří virtuální interface `Port-channel 1`. Ten se konfiguruje místo fyzických portů (např. jako Trunk).

```text
interface Port-channel 1
 switchport mode trunk
 switchport trunk allowed vlan 10,20
exit
```

### Layer 3 Etherchannel (na routeru nebo L3 switchi)
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

## Ověření konfigurace

### Kontrola stavu Etherchannelu
Zobrazí souhrn o skupinách a stavu portů.

```text
show etherchannel summary
```

**Očekávaný výstup:**
Flagy: `P` (Bundled in Port-channel), `S` (Layer2), `U` (In use).
V ideálním případě uvidíte: `Po1(SU)  P(Gi0/1) P(Gi0/2)`.
