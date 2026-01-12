# L2 Bezpečnost (L2 Security)

## Teorie
Zabezpečení na 2. vrstvě (Data Link Layer) je klíčové, protože útoky zde mohou ohrozit celou síťovou infrastrukturu.

### Typy útoků a mitigace
1.  **MAC Address Table Flooding**: Útočník zaplní CAM tabulku falešnými MAC adresami, switch se změní v hub a posílá vše všude. -> *Obrana: Port Security.*
2.  **DHCP Starvation / Spoofing**: Vyčerpání adres nebo podvržení falešného DHCP serveru (Man-in-the-Middle). -> *Obrana: DHCP Snooping.*
3.  **ARP Spoofing / Poisoning**: Útočník se vydává za gateway MAC. -> *Obrana: Dynamic ARP Inspection (DAI).*
4.  **VLAN Hopping**: Útok na DTP nebo tagování rámců pro přístup do jiné VLAN. -> *Obrana: Vypnout DTP, nastavit Native VLAN.*
5.  **STP Attacks**: Manipulace s topologií (podvržení Root Bridge). -> *Obrana: BPDU Guard, Root Guard.*

## Konfigurace

### Port Security
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

### DHCP Snooping
Rozlišuje porty na **Trusted** (DHCP server, uplink) a **Untrusted** (klienti). Zahazuje DHCP Offer z untrusted portů.
```bash
Switch(config)# ip dhcp snooping
Switch(config)# ip dhcp snooping vlan 10
Switch(config)# interface g0/1             # Uplink k serveru
Switch(config-if)# ip dhcp snooping trust
```

### Dynamic ARP Inspection (DAI)
Ověřuje ARP pakety proti vazbám z DHCP Snooping databáze.
```bash
Switch(config)# ip arp inspection vlan 10
Switch(config)# interface g0/1             # Uplink
Switch(config-if)# ip arp inspection trust
```

### Mitigace STP útoků (BPDU Guard / PortFast)
Zapnout na portech pro koncová zařízení. Pokud přijde BPDU (znak switche), port se vypne.
```bash
Switch(config)# interface f0/1
Switch(config-if)# spanning-tree portfast
Switch(config-if)# spanning-tree bpduguard enable
```
