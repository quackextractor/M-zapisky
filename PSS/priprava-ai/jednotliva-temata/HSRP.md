# HSRP (Hot Standby Router Protocol)

HSRP je Cisco proprietární protokol pro redundanci výchozí brány (Gateway). Umožňuje spojit více routerů do jednoho virtuálního routeru.

**Klíčové pojmy:**
*   **Active Router:** Směruje data.
*   **Standby Router:** Čeká a sleduje Active router. Pokud Active vypadne, převezme jeho roli.
*   **Virtual IP:** Adresa, kterou mají PC nastavenou jako Default Gateway.
*   **Priority:** Určuje, kdo bude Active (vyšší vyhrává). Default je 100.
*   **Preempt:** Umožní routeru s vyšší prioritou převzít roli Active, i když už existuje jiný Active router (např. po restartu hlavního routeru).

## Konfigurace HSRP

### Konfigurace Active Routeru (R1)
Nastavíme vyšší prioritu (např. 150) a zapneme preempt.

```text
enable
configure terminal
interface GigabitEthernet0/0
 ip address 192.168.1.2 255.255.255.0
 standby 1 ip 192.168.1.1
 standby 1 priority 150
 standby 1 preempt
exit
```
*   `192.168.1.1` je virtuální IP brána.
*   `192.168.1.2` je fyzická IP routeru.

### Konfigurace Standby Routeru (R2)
Necháme defaultní prioritu (100).

```text
enable
configure terminal
interface GigabitEthernet0/0
 ip address 192.168.1.3 255.255.255.0
 standby 1 ip 192.168.1.1
exit
```

## Ověření konfigurace

### Kontrola stavu HSRP
Zobrazí, který router je Active a který Standby.

```text
show standby brief
show standby
```

**Očekávaný výstup `show standby brief`:**
Interface | Grp | Prio | P State | Active | Standby | Virtual IP
--- | --- | --- | --- | --- | --- | ---
Gi0/0 | 1 | 150 | Active | local | 192.168.1.3 | 192.168.1.1
