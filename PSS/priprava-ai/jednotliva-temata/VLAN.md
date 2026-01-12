# VLAN (Virtual LAN)

VLAN logicky rozděluje fyzický switch na více virtuálních sítí. Zařízení v různých VLAN spolu nemohou komunikovat bez routeru (L3 zařízení).

**Klíčové pojmy:**
*   **Access port:** Přenáší provoz pouze jedné VLAN (připojení PC).
*   **Trunk port:** Přenáší provoz více VLAN (propojení switch-switch nebo switch-router). Používá 802.1q tagování.
*   **Native VLAN:** VLAN, která na trunku není tagovaná (z bezpečnostních důvodů by měla být změněna z defaultní VLAN 1).
*   **ROAS (Router on a Stick):** Způsob směrování mezi VLAN pomocí jednoho fyzického rozhraní routeru rozděleného na sub-interface.

## Konfigurace VLAN

### Vytvoření VLAN a přiřazení portů (Switch)
Vytvoří VLANy a přiřadí fyzické porty do konkrétních VLAN.

```text
enable
configure terminal
vlan 10
 name ZAMESTNANCI
vlan 20
 name HOSTE
exit

interface range FastEthernet0/1-10
 switchport mode access
 switchport access vlan 10
exit

interface range FastEthernet0/11-20
 switchport mode access
 switchport access vlan 20
exit
```

### Nastavení Trunku (Switch)
Nastaví port pro přenos všech (nebo vybraných) VLAN.

```text
enable
configure terminal
interface GigabitEthernet0/1
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 10,20,99
exit
```

### Inter-VLAN Routing - Router on a Stick (Router)
Nastavení sub-interfaců na routeru pro komunikaci mezi VLANami.

```text
enable
configure terminal
interface GigabitEthernet0/0
 no shutdown
exit

interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
exit

interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
exit
```

## Ověření konfigurace

### Kontrola VLAN a Trunků
Ověří existenci VLAN, přiřazení portů a stav trunk linek.

```text
show vlan brief
show interfaces trunk
show ip interface brief
```

**Očekávaný výstup:**
*   `show vlan brief`: Seznam aktivních VLAN a portů, které k nim patří.
*   `show interfaces trunk`: Seznam trunk portů, použitá enkapsulace (802.1q) a povolené VLANy.
