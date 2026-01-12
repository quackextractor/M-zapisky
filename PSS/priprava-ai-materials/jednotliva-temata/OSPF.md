# OSPF (Open Shortest Path First)

## Teorie
OSPF je link-state směrovací protokol, který používá metriku "cost" (založenou na šířce pásma) pro výpočet nejkratší cesty.
Základní vlastnosti:
- **Link-State protokol**: Každý router zná topologii celé oblasti.
- **Hierarchický návrh**: Používá oblasti (Areas) pro škálování. Páteřní oblast je Area 0. Všechny ostatní oblasti se musí připojovat k Area 0.
- **Rychlá konvergence**: Rychle reaguje na změny v síti.
- **Dijkstrův algoritmus**: Používán pro výpočet nejkratší cesty.

## Konfigurace (IPv4)

### Základní nastavení procesu na routeru
```bash
Router(config)# router ospf 10          # 10 je Process ID (lokální význam)
Router(config-router)# router-id 1.1.1.1 # Unikátní identifikátor routeru
```

### Přidání sítí do OSPF (klasický způsob)
```bash
Router(config-router)# network 10.10.1.0 0.0.0.255 area 0  # Wildcard maska (inverzní maska)
```
Pozor: Wildcard maska pro /30 (255.255.255.252) je 0.0.0.3.

### Nastavení OSPF přímo na rozhraní (modernější způsob)
```bash
Router(config)# interface g0/0/0
Router(config-if)# ip ospf 10 area 0    # Zapne OSPF proces 10 pro Area 0 na tomto rozhraní
```

### Pasivní rozhraní
Zabrání odesílání OSPF Hello paketů na rozhraní, kde nejsou další routery (bezpečnost a efektivita).
```bash
Router(config-router)# passive-interface g0/0/1
# nebo pro všechny a pak povolit konkrétní:
Router(config-router)# passive-interface default
Router(config-router)# no passive-interface g0/0/0
```

### Propagace defaultní routy
Pokud má router defaultní routu (např. do internetu), může ji poslat ostatním.
```bash
Router(config-router)# default-information originate
```

### Point-to-Point síť
Na spojích mezi dvěma routery (bez switche) se nevolí DR/BDR, což zrychluje konvergenci.
```bash
Router(config-if)# ip ospf network point-to-point
```

## Konfigurace (IPv6) - OSPFv3
Nutné povolit IPv6 routing: `ipv6 unicast-routing`.

```bash
Router(config)# ipv6 router ospf 10
Router(config-rtr)# router-id 1.1.1.1
Router(config)# interface g0/0/0
Router(config-if)# ipv6 ospf 10 area 0
```

## Ověření / Troubleshooting
- `show ip protocols`: Zobrazí běžící protokoly, Router ID, sítě.
- `show ip ospf neighbor`: Zobrazí sousedy (stav by měl být FULL nebo 2WAY).
- `show ip route`: Zobrazí směrovací tabulku (OSPF cesty označené jako 'O').
- `clear ip ospf process`: Restartuje OSPF proces (vynutí znovunavázání sousedství).
