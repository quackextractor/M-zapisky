# NAT (Network Address Translation)

## Teorie
NAT překládá IP adresy v hlavičce paketu (typicky privátní na veřejné). To šetří veřejné IPv4 adresy a zvyšuje bezpečnost (skrývá vnitřní topologii).

### Typy NAT
1.  **Static NAT**: 1:1 mapování (jedna privátní IP na jednu veřejnou IP). Používá se pro servery přístupné z internetu.
2.  **Dynamic NAT**: Mapování z poolu veřejných adres. (Mnoho k Mnoho).
3.  **PAT (Port Address Translation) / NAT Overload**: Mapování mnoha privátních adres na jednu veřejnou IP pomocí unikátních zdrojových portů. Nejčastější v domácnostech.

## Konfigurace (Cisco)

### Definice rozhraní
Nejprve musíme určit, kde je vnitřní (inside) a vnější (outside) síť.
```bash
Router(config)# interface g0/0
Router(config-if)# ip nat inside

Router(config)# interface g0/1
Router(config-if)# ip nat outside
```

### Static NAT (1:1)
```bash
Router(config)# ip nat inside source static 192.168.1.10 209.165.200.225
```

### Dynamic NAT (Pool)
```bash
Router(config)# ip nat pool MY_POOL 209.165.200.226 209.165.200.240 netmask 255.255.255.224
Router(config)# access-list 1 permit 192.168.1.0 0.0.0.255
Router(config)# ip nat inside source list 1 pool MY_POOL
```

### PAT (NAT Overload)
Použití jedné veřejné IP na rozhraní.
```bash
Router(config)# access-list 1 permit 192.168.1.0 0.0.0.255
Router(config)# ip nat inside source list 1 interface g0/1 overload
```
*Klíčové slovo `overload` zapíná PAT.*

## Konfigurace (Linux iptables)
Linux používá `iptables` (nebo novější `nftables`). Pravidla se píší do tabulky `nat`, řetězec `POSTROUTING` (pro SNAT) nebo `PREROUTING` (pro DNAT).

### Maškaráda (SNAT - Source NAT)
Odpovídá PAT. Překládá odchozí provoz na IP adresu odchozího rozhraní.
```bash
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```
*-t nat (tabulka nat), -A POSTROUTING (přidat do řetězce), -o eth0 (výstupní interface), -j MASQUERADE (cíl).*

### Port Forwarding (DNAT - Destination NAT)
Přístup zvenku na vnitřní server (ekvivalent Static NAT s portem).
```bash
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination 192.168.1.50:80
```

### Zobrazení tabulky NAT
```bash
iptables -t nat -L -n -v
```
