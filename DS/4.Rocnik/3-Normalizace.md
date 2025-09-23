# Normalizace, normální formy 1NF - 3NF

= Normalizace je process úpravy struktury databáze (tabulky), aby nedocházelo k **redundanci dat** (opakující se data) a aby byla zajištěna **konzistence** z hlediska jednoznačnosti **při vyhledávání**.

Pro zajištění správně normalizované DB používáme normální formy **1. NF až 3. NF**:

## 1. NF (atomicita)
- je splněná **0. NF** (je stanovený PK)
- a zároveň všechny prvky jsou atomární (každé políčko obsahuje pouze jednu hodnotu)

### Př. (Důležitý): 

| id      | zaměstnanec     | adresa            | telefon          |
| ------- | --------------- | ----------------- | ---------------- |
| 1       | Jan Kos         | P2, Ječná 30      | 222 333, 777 888 |
| 2       | Krčí David      | Nad Popisku 5, P2 | 111222           |
| Problém | Nesplňuje 1. NF | Nesplňuje 1. NF   | Nesplňuje 1. NF  |
### Řešení:
a) je-li počet atributů omezený a max 5, pak je rozdělíme do více atributů

Zaměstnanec -> jméno, příjmení
Adresa -> město, ulice, číslo popisné

b) je-li hodnot více (nevíme přesný počet), vytvoříme novou tabulku a propojíme vazbou

![[pasted1.png]]

| Zam              | Telefon  |
| ---------------- | -------- |
| PK id            | PK id    |
| jmeno            | F zam_id |
| prijmeni         | cislo    |
| mesto            |          |
| ulice + c. popis |          |
## 2. NF
- musí být splněná 1. NF (totiž je i 0. NF) a zároveň každý neklíčový atribut je závislý na celém primárním klíči
	- je o slozeny PK (sklada se ze 2 a více atributů)
pouze
- pokud je PK jednoduchy je 2. NF automaticky splnena a redundance jsou zpusobeny 3. NF

### Př.: 

| č. studenta | příjmení | třída | patro |
| ----------- | -------- | ----- | ----- |
| 1           | Novak    | C4a   | 2     |
| 2           | Kohout   | C4a   | 2     |
| 3           | Kolac    | C4a   | 2     |
| 1           | Kos      | C4b   | 4     |
| 2           | Novak    | C4b   | 4     |

č. studenta + třída = složený PK
příjmení = neklíčový atribut
patro závisý na třída (= část PK) -> **nesplňuje 2. NF**

### Řešení:
rozdělení do více tabulek zavedením jednoduchých klíčů
![[pasted2.png]]


| Třída      | student    |
| ---------- | ---------- |
| PK id      | PK id      |
| ozn_tridy  | F trida_id |
| patro      | cis_stud   |
| tr. ucitel | prijmeni   |
