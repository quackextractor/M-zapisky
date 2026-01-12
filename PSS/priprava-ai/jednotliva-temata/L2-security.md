# L2 Security (Zabezpečení na 2. vrstvě)

Zabezpečení switche proti útokům jako MAC Flooding (přeplnění CAM tabulky) nebo Rogue DHCP server (falešný DHCP server).

**Techniky:**
*   **Port Security:** Omezuje počet MAC adres na portu. Chrání proti MAC flooding.
*   **DHCP Snooping:** Rozlišuje porty na "trusted" (důvěryhodné - tam je DHCP server) a "untrusted" (nedůvěryhodné - tam jsou klienti). Chrání proti Rogue DHCP.

## Konfigurace L2 Security

### Port Security
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
*   `sticky`: Naučí se MAC adresu prvního připojeného zařízení a uloží ji do running-config.

### DHCP Snooping
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
*   Všechny ostatní porty jsou automaticky `untrusted` (defaultní stav).

## Ověření konfigurace

### Kontrola Port Security a DHCP Snooping
Zobrazí stav zabezpečení portů a tabulku DHCP snoopingu.

```text
show port-security interface FastEthernet0/1
show ip dhcp snooping
show ip dhcp snooping binding
```

**Očekávaný výstup:**
*   `show port-security ...`: Port Status: Secure-up/Secure-down, Violation Mode: Shutdown.
*   `show ip dhcp snooping binding`: Tabulka přidělených IP adres klientům (MAC adresa, IP adresa, VLAN, Port).
