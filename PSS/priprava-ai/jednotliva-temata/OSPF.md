# OSPF (Open Shortest Path First)

OSPF je link-state směrovací protokol, který používá metriku "cost" (založenou na šířce pásma) k určení nejlepší cesty. Routery si vyměňují informace o topologii sousedům a udržují si kompletní mapu sítě (LSDB).

**Klíčové pojmy:**
*   **Process ID:** Číslo procesu na routeru (lokální význam).
*   **Area:** Logické rozdělení sítě. Vždy musí existovat páteřní oblast (Area 0), na kterou jsou napojeny ostatní oblasti.
*   **Wildcard maska:** Inverzní maska (např. 255.255.255.0 -> 0.0.0.255).
*   **Passive Interface:** Rozhraní, kde OSPF neběží, ale jeho síť je propagována.
*   **Router ID:** Jedinečný identifikátor routeru (nejvyšší IP loopbacku nebo aktivního fyzického rozhraní, nebo manuálně nastaveno).

## Konfigurace OSPF

### Základní nastavení OSPF
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

### Propagace výchozí cesty (Default Route)
Pokud router má výchozí cestu (např. do internetu), může ji poslat ostatním OSPF routerům.

```text
enable
configure terminal
router ospf 1
 default-information originate
exit
```

## Ověření konfigurace

### Zobrazení sousedů a nastavení
Ověří, zda se vytvořilo sousedství (stav by měl být FULL nebo 2WAY).

```text
show ip ospf neighbor
show ip ospf interface brief
show ip route ospf
```

**Očekávaný výstup `show ip ospf neighbor`:**
Měli byste vidět sousední routery, jejich Router ID, stav (např. FULL/DR, FULL/BDR) a interface, přes který jsou dostupní.
