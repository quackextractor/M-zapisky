# 4 - Normalizace vs Denormalizace: SQL DDL, DML

## 3. NF
- existuje **PK jednoduchý**, **je splněna 1. NF** a zároveň je defaultně **splněna i 2. NF** a zároveň **neklíčové atributy na sobě navzájem nezávisí**
    

=> **Neklíčové atributy nejsou tranzitivně závislé**

|**id**|**název zboží**|**název výrobce**|**(město) adresa výrobce**|
|---|---|---|---|
|1|mléko|Olma|Olomouc|
|2|tvaroh|Olma|Olomouc|
|3|mléko|Tatra|Kunín|
|4|jogurt|Tatra|Kunín|
|5|jogurt|Tatra|Praha|
|6|tvaroh|Tatra|Kunín|

![[4NF.png]]  
![[4NF2.png]]

---

## Denormalizace

**Denormalizace** DB znamená, že DB může obsahovat:

### a) duplikovaná (redundantní) data

např. kontakt na zákazníka bude v objednávce, abychom se vyhnuli nutnosti spojovat tabulky joinem

### b) uložené informace (data vs informace)

např. předem spočítané hodnoty agr. funkcemi, jako `cena_položky` (`cena_ks × počet_ks`), `cena_celkem` (`SUMA cena_položky`), abychom zrychlili výpis nebo přehled (není potřeba vše počítat při výpisu)

### c) data spojená z různých tabulek = datový sklad

např. produkt i dodavatel v tabulce **dodávka** pro získání rychlých přehledů (statistik)  
=> eliminace více joinů (pracuje pouze nad jednou tabulkou)

---

## Normalizace × Denormalizace

|Výhody|Normalizace|Denormalizace|
|---|---|---|
||+ lepší integrita|+ rychlé čtení a jednodušší dotazy|
||+ bez redundancí||
||+ jednodušší správa||
|**Nevýhody**|||
||- pomalé čtení, přehledů a statistik|- redundance|
|||- riziko nekonzistentních dat|
|||- složitá správa (údržba)|
