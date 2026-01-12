# VLAN (Virtual LAN)

## Teorie
VLAN (Virtual Local Area Network) umožňuje logicky rozdělit jednu fyzickou síť (L2) na více oddělených sítí (broadcastových domén).
- **Výhody**: Bezpečnost (oddělení provozu), snížení broadcastového provozu, flexibilita.
- **Trunking (802.1Q)**: Propojení mezi switchi přenášející více VLAN. Rámce jsou "tagovány" (přidána značka s číslem VLAN).
- **Native VLAN**: Nenetagovaná VLAN na trunku (by default VLAN 1). Oba konce trunku musí mít stejnou Native VLAN.
- **DTP (Dynamic Trunking Protocol)**: Cisco protokol pro automatické vyjednání trunku.
- **VTP (VLAN Trunking Protocol)**: Umožňuje centrálně spravovat VLAN databázi (Server) a replikovat ji na ostatní switche (Client).

## Konfigurace

### Vytvoření VLAN
```bash
Switch(config)# vlan 10
Switch(config-vlan)# name ZAMESTNANCI
```

### Přiřazení portu do VLAN (Access port)
```bash
Switch(config)# interface f0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
```

### Konfigurace Trunku
```bash
Switch(config)# interface g0/1
Switch(config-if)# switchport trunk encapsulation dot1q  # Někdy nutné (starší modely podporují i ISL)
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk native vlan 99       # Změna native VLAN (bezpečnost)
Switch(config-if)# switchport trunk allowed vlan 10,20,99 # Povolení konkrétních VLAN
```

### Konfigurace VTP
```bash
Switch(config)# vtp domain MOJE_DOMENA
Switch(config)# vtp mode server          # nebo client, transparent
Switch(config)# vtp password TAJNE_HESLO
```
*Pozor: VTP Server přepisuje databázi Clientů podle vyššího Revision Number. Nový switch v síti může smazat všechny VLANy, pokud má vyšší číslo revize!*

### Inter-VLAN Routing (Router-on-a-stick)
Propojení VLAN mezi sebou pomocí routeru.
```bash
Router(config)# interface g0/0.10        # Subinterface
Router(config-subif)# encapsulation dot1Q 10  # Přiřazení k VLAN 10
Router(config-subif)# ip address 192.168.10.1 255.255.255.0
```

### Inter-VLAN Routing (L3 Switch - SVI)
```bash
Switch(config)# ip routing               # Povolení routování
Switch(config)# interface vlan 10        # SVI (Switch Virtual Interface)
Switch(config-if)# ip address 192.168.10.1 255.255.255.0
Switch(config-if)# no shutdown
```
