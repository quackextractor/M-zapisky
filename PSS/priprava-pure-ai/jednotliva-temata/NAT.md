# NAT (Network Address Translation)

NAT překládá privátní IP adresy (vnitřní síť) na veřejné IP adresy (internet). Umožňuje šetřit veřejné IPv4 adresy.

**Typy NAT:**
*   **Static NAT:** 1:1 mapování (jedna privátní IP na jednu veřejnou IP). Používá se pro servery přístupné zvenčí.
*   **Dynamic NAT:** Mapování privátních IP na skupinu (pool) veřejných IP.
*   **PAT (Port Address Translation) / NAT Overload:** Mnoho privátních IP na jednu (nebo několik) veřejných IP s využitím portů. Nejčastější doma a ve firmách.

## Konfigurace NAT

### Definice Inside a Outside rozhraní
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

### Static NAT (1:1)
Příklad: Zpřístupnění interního serveru 192.168.10.10 na veřejné IP 203.0.113.10.

```text
enable
configure terminal
ip nat inside source static 192.168.10.10 203.0.113.10
exit
```

### PAT (Overload)
Nejběžnější scénář. Překlad celé sítě 192.168.10.0/24 na adresu vnějšího rozhraní (např. G0/1). Vyžaduje Access List (ACL) pro definici provozu.

```text
enable
configure terminal
access-list 1 permit 192.168.10.0 0.0.0.255
ip nat inside source list 1 interface GigabitEthernet0/1 overload
exit
```

## Ověření konfigurace

### Zobrazení tabulky překladů
Zobrazí aktuální aktivní překlady.

```text
show ip nat translations
show ip nat statistics
```

**Očekávaný výstup `show ip nat translations`:**
Tabulka se sloupci `Inside global`, `Inside local`, `Outside local`, `Outside global`.
*   **Inside local:** Privátní IP PC.
*   **Inside global:** Veřejná IP (za kterou se maskuje).
