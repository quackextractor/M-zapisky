# EtherChannel

## Teorie
EtherChannel je technologie pro agregaci linek (link aggregation). Umožňuje spojit více fyzických linek do jedné logické (Port-Channel).
- **Výhody**: Vyšší propustnost (load balancing), redundance (pokud jedna linka spadne, ostatní jedou), STP vidí jen jednu linku (žádné blokování smyček).
- **Protokoly**:
    - **PAgP (Port Aggregation Protocol)**: Cisco proprietární. Módy: `auto`, `desirable`.
    - **LACP (Link Aggregation Control Protocol) 802.3ad**: Průmyslový standard. Módy: `passive`, `active`.
    - **ON (Static)**: Bez vyjednávání.

### Podmínky pro vytvoření
Všechny porty v channelu musí mít shodné nastavení:
- Rychlost a Duplex.
- VLAN mód (access/trunk).
- Native VLAN a povolené VLANy (u trunku).

## Konfigurace

### L2 EtherChannel (LACP)
```bash
Switch(config)# interface range g0/1 - 2
Switch(config-if-range)# channel-group 1 mode active    # Vytvoří interface Port-channel 1
Switch(config-if-range)# exit

Switch(config)# interface port-channel 1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20
```

### L3 EtherChannel (Routed Port)
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
