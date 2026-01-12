# HSRP (Hot Standby Router Protocol)

## Teorie
FHRP (First Hop Redundancy Protocol). HSRP je proprietární protokol Cisco pro redundanci výchozí brány (Gateway).
Dovoluje více routerům sdílet jednu virtuální IP adresu a MAC adresu, kterou používají koncoví klienti jako svou bránu.

### Klíčové pojmy
- **Virtual IP**: Adresa brány nastavená na PC. Není přiřazena fyzickému interfacu, ale HSRP skupině.
- **Active Router**: Router, který aktuálně posílá pakety. (Ten s nejvyšší prioritou).
- **Standby Router**: Router, který čeká a monitoruje Active router. Převezme roli, pokud Active selže.
- **Priority**: Určuje Active router. Default je 100. Vyšší vyhrává.
- **Preemption**: Pokud je zapnuto, router s vyšší prioritou okamžitě převezme roli Active (i když už jeden běží). Defaultně vypnuto.
- **HSRP Version**: V1 (default, skupina multicast 224.0.0.2), V2 (podpora IPv6, multicast 224.0.0.102).

## Konfigurace

### Základní nastavení
Nastavuje se na interfacu (nebo subinterfacu/SVI), který je bránou pro LAN.

**R1 (Active):**
```bash
R1(config)# interface g0/1
R1(config-if)# ip address 192.168.1.2 255.255.255.0  # Fyzická IP
R1(config-if)# standby 1 ip 192.168.1.1              # Virtuální IP (Skupina 1)
R1(config-if)# standby 1 priority 150                # Vyšší priorita -> bude Active
R1(config-if)# standby 1 preempt                     # Převezme roli, když se vrátí online
```

**R2 (Standby):**
```bash
R2(config)# interface g0/1
R2(config-if)# ip address 192.168.1.3 255.255.255.0  # Fyzická IP
R2(config-if)# standby 1 ip 192.168.1.1              # Stejná virtuální IP
R2(config-if)# standby 1 priority 100                # Default (nižší než R1)
R2(config-if)# standby 1 preempt                     # Doporučeno i zde
```

### Ověření
```bash
R1# show standby brief
R1# show standby
```
Výpis ukáže stav (Active/Standby), Virtuální IP, a kdo je Active router.
