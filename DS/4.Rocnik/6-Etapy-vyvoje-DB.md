# 5 - Etapy vývoje db

## Důležité diagramy
### 1) fáze: vytváření db

![[1-faze.svg]]

### 2) fáze: provoz db

![[faze-2.svg]]
## Fáze podrobně

### 1. Analýza

#### a) analýza organizace
- analýza HW + SW, případně návrh nového HW + SW
- nastavení účtů, rolí a práv: **konzultace s firmou**
- analýza typů datových souborů (.csv) + četnost vstupů
- analýza typů záloh, čas zálohy
#### b) analýza db (nová, stávající)
- nová: sledujeme požadavky firmy
- stávající: sledujeme problémy a chyby existující db
### 2. Návrh

#### a) logické schéma
- určení entit + určení vazeb
- zajištění normalizace (denormalizace)
- (dekompozice vztahu M:N)
	-> **konzultace s klientem**
- mohou být i atributy (bez PK, FK)
- 
> vysvětlit normalizaci, uvádět příklad k logickém schématu
> **dekompozice** = rozložení vztahy M:N na 2 x 1:N + vazební tabulka
#### b) relační schéma
- obsahuje:
	- tabulky (entity)
	- sloupce (atributy)
	- vazby řešené pomocí **PK** a **FK**
- **neslouží pro klienta**, ale jde o **technické řešení** db
- **zajištění integrity**
	- **entitová**
	- **referenční**
	- nedochází k sirotků
	- **doménová** - dat. typ, další omezení

> vysvětlit integritu

### 3. Implementace
- realizace navržené db na vybrané servery v jazyce SQL - struktura
	- => vyřešené **strukturální požadavky**
- realizace další "objektů" procedury, funkce, pohledy, triggery, indexy, ...
	- => řešení **procedurální části**
- uživatelské účty

### 4. Testování
- vložení testovacích dat (mock data)
- ověření funkce **procedurální části**
- ověření db 
	- integritní omezení
	- nedochází k redundancím
- ověření uživatelských účtů, práv a rolí
- ověření zálohování
- testování vstupů a výstupů (úprava dat na vstupu ER, ELT)

### 5. Nasazení db do provozu
* db je správně normalizovaná
* db splňuje integritní omezení
Skládá se z:
- nahrání **struktury db** na PC uživatele (transakce)
- nahrání **"živých"** uživatelských dat
- otestování v provozu (všech funkcí)
- předání
### 6. Údržba
- přidání indexů
- zvýšení četnosti záloh
- zmenšení objemu dat db
- správa uživatelů