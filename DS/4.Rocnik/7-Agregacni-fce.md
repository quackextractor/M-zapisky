# Agregační funkce, GROUP BY, HAVING

Funkce, které pracují jen s jedním argumentem a vrací vždy pouze jednu hodnotu:

- nelze je samostatně použít v klauzuli **WHERE**, musí být součástí podselectu nebo použití v **HAVING** po **GROUP BY**
    

**Špatně:**

```sql
SELECT *
FROM zakaznici
WHERE COUNT(objednavky) > 5;  -- chybné, COUNT() nelze použít v WHERE
```

**Správně:**

```sql
SELECT *
FROM zakaznici
WHERE cena > (select avg(cena) from vyrobek);
```

```sql
SELECT zakaznik_id, COUNT(objednavky) AS pocet_objednavek
FROM objednavky
GROUP BY zakaznik_id
HAVING COUNT(objednavky) > 5;  -- správné, použití agregace po GROUP BY
```

Další: count(), sum(), avg(), min(), max()
-> parametr číslo, min/max ale i datum a varchar()

## Agregační funkce – příklady

### 1. `COUNT()`

Počítá počet řádků nebo nenulových hodnot určitého sloupce.

```sql
-- Počet objednávek pro každého zákazníka
SELECT zakaznik_id, COUNT(objednavky_id) AS pocet_objednavek
FROM objednavky
GROUP BY zakaznik_id;
```

### 2. `SUM()`

Sečte hodnoty v číselném sloupci.

```sql
-- Celková částka objednávek pro každého zákazníka
SELECT zakaznik_id, SUM(castka) AS celkova_castka
FROM objednavky
GROUP BY zakaznik_id;
```

### 3. `AVG()`

Vypočítá průměrnou hodnotu.

```sql
-- Průměrná částka objednávky pro každého zákazníka
SELECT zakaznik_id, AVG(castka) AS prumerna_castka
FROM objednavky
GROUP BY zakaznik_id;
```

### 4. `MIN()` a `MAX()`

Najde nejmenší nebo největší hodnotu sloupce. Funguje i pro datum nebo varchar.

```sql
-- Nejstarší a nejnovější objednávka každého zákazníka
SELECT zakaznik_id, MIN(datum_objednavky) AS nejstarsi, MAX(datum_objednavky) AS nejmladsi
FROM objednavky
GROUP BY zakaznik_id;

-- Nejmenší a největší jméno zákazníka (abecedně)
SELECT MIN(jmeno) AS nejmensi_jmeno, MAX(jmeno) AS nejvetsi_jmeno
FROM zakaznici;
```

## Klauzule GROUP BY
- seskupený dotaz, pro každou skupinu vytvoří souhrn
- sloupce (atributy) uvedené za GROUP BY určuje pořadí seskupování zleva doprava

Jasně, doplním k oběma příkladům i možné **example output**.

---

## Počet zaměstnanců a součet platů v oddělení

```sql
SELECT oddeleni_id,
       COUNT(zamestnanec_id) AS pocet_zamestnancu,
       SUM(plat) AS soucet_platu
FROM zamestnanci
GROUP BY oddeleni_id
ORDER BY oddeleni_id ASC;
```

### Kroky, které SQL provede:

1. **Načtení dat** – vybere všechny řádky z tabulky `zamestnanci`.
    
2. **Seskupení (`GROUP BY`)** – rozdělí řádky do skupin podle hodnot ve sloupci `oddeleni_id`.
    
3. **Agregace** – pro každou skupinu spočítá:
    
    - `COUNT(zamestnanec_id)` – počet zaměstnanců v oddělení
        
    - `SUM(plat)` – součet platů v oddělení
        
4. **Řazení (`ORDER BY`)** – výsledky se seřadí podle `oddeleni_id` vzestupně.
    
5. **Výsledek** – zobrazí tabulka se třemi sloupci: `oddeleni_id`, `pocet_zamestnancu`, `soucet_platu`.
    

**Example output:**

|oddeleni_id|pocet_zamestnancu|soucet_platu|
|---|---|---|
|1|5|250000|
|2|3|180000|
|3|4|220000|

---

## Počet zaměstnanců podle pohlaví a součet platů v oddělení

```sql
SELECT oddeleni_id,
       pohlavi,
       COUNT(zamestnanec_id) AS pocet_zamestnancu,
       SUM(plat) AS soucet_platu
FROM zamestnanci
GROUP BY oddeleni_id, pohlavi
ORDER BY oddeleni_id ASC, pohlavi ASC;
```

### Kroky, které SQL provede:

1. **Načtení dat** – vybere všechny řádky z tabulky `zamestnanci`.
    
2. **Seskupení (`GROUP BY`)** – rozdělí řádky do skupin podle kombinace `oddeleni_id` + `pohlavi`.
    
3. **Agregace** – pro každou skupinu spočítá:
    
    - `COUNT(zamestnanec_id)` – počet zaměstnanců daného pohlaví v oddělení
        
    - `SUM(plat)` – součet platů zaměstnanců daného pohlaví v oddělení
        
4. **Řazení (`ORDER BY`)** – výsledky se seřadí podle `oddeleni_id` a uvnitř oddělení podle `pohlavi`.
    
5. **Výsledek** – zobrazí tabulka se čtyřmi sloupci: `oddeleni_id`, `pohlavi`, `pocet_zamestnancu`, `soucet_platu`.
    

**Example output:**

| oddeleni_id | pohlavi | pocet_zamestnancu | soucet_platu |
| ----------- | ------- | ----------------- | ------------ |
| 1           | F       | 2                 | 100000       |
| 1           | M       | 3                 | 150000       |
| 2           | F       | 1                 | 60000        |
| 2           | M       | 2                 | 120000       |
| 3           | F       | 2                 | 110000       |
| 3           | M       | 2                 | 110000       |

## Klauzule HAVING

- podmínka (omezení) pro skupiny
    
- má smysl pouze pokud je **GROUP BY**
    
- pracuje podobně jako **WHERE**, ale zde může být samostatně použitá agregační funkce
    

### Příklad: Počet zaměstnanců v odděleních s více než 5 zaměstnanci

```sql
SELECT oddeleni_id,
       COUNT(zamestnanec_id) AS pocet_zamestnancu
FROM zamestnanci
GROUP BY oddeleni_id
HAVING COUNT(zamestnanec_id) > 5
ORDER BY oddeleni_id ASC;
```

### Kroky, které SQL provede:

1. **Načtení dat** – vybere všechny řádky z tabulky `zamestnanci`.
    
2. **Seskupení (`GROUP BY`)** – rozdělí řádky do skupin podle hodnot ve sloupci `oddeleni_id`.
    
3. **Agregace** – pro každou skupinu spočítá:
    
    - `COUNT(zamestnanec_id)` – počet zaměstnanců v oddělení
        
4. **Filtrace (`HAVING`)** – ponechá jen ty skupiny, kde `COUNT(zamestnanec_id) > 5`.
    
5. **Řazení (`ORDER BY`)** – výsledky se seřadí podle `oddeleni_id` vzestupně.
    
6. **Výsledek** – zobrazí tabulka se dvěma sloupci: `oddeleni_id`, `pocet_zamestnancu`.
    

**Example output:**

|oddeleni_id|pocet_zamestnancu|
|---|---|
|1|7|
|3|8|

---

## JOINs 
- spojení tabulek pomocí PK a FK pro select
Jasně, doplním k JOIN příkladům i možné **example output**.

Jasně, tady je doplněné stručné info k JOINům bez konkrétních SQL příkladů:

---

## JOINs

- spojení tabulek pomocí **PK** (primární klíč) a **FK** (cizí klíč) pro **SELECT**
    

### a) **INNER JOIN**

- vrací pouze řádky, kde existuje odpovídající záznam v obou tabulkách.
    
- pokud není shoda, řádek se nevrátí.
    

### b) **LEFT (RIGHT) JOIN**

- **LEFT JOIN** – vrací všechny řádky z levé tabulky; pokud není odpovídající záznam v pravé, doplní `NULL`.
    
- **RIGHT JOIN** – obráceně, všechny řádky z pravé tabulky; pokud není odpovídající záznam v levé, doplní `NULL`.
    

### c) **FULL OUTER JOIN**

- vrací všechny řádky z obou tabulek; pokud není shoda, doplní `NULL` na straně, kde odpovídající záznam chybí.

---

### a) **INNER JOIN**

```sql
SELECT o.objednavka_id, z.jmeno, o.castka
FROM objednavky o
INNER JOIN zakaznici z
ON o.zakaznik_id = z.zakaznik_id;
```

**Example output:**

|objednavka_id|jmeno|castka|
|---|---|---|
|101|Jan Novak|5000|
|102|Eva Kral|3200|
|103|Petr Svoboda|4500|

> Vrací jen objednávky, které mají existujícího zákazníka.

---

### b) **LEFT JOIN**

```sql
SELECT z.jmeno, o.objednavka_id, o.castka
FROM zakaznici z
LEFT JOIN objednavky o
ON z.zakaznik_id = o.zakaznik_id;
```

**Example output:**

|jmeno|objednavka_id|castka|
|---|---|---|
|Jan Novak|101|5000|
|Eva Kral|102|3200|
|Petr Svoboda|103|4500|
|Marie Novak|NULL|NULL|

> Zobrazí všechny zákazníky, i ty bez objednávek (`NULL` ve sloupcích objednávky).

---
### c) **RIGHT JOIN**

- vrací **všechny řádky z pravé tabulky**, odpovídající z levé tabulky, pokud existuje, jinak `NULL`
    

**Příklad:** všechny objednávky a jejich zákazníky, i když některá objednávka nemá existujícího zákazníka

```sql
SELECT z.jmeno, o.objednavka_id, o.castka
FROM zakaznici z
RIGHT JOIN objednavky o
ON z.zakaznik_id = o.zakaznik_id;
```

**Example output:**

|jmeno|objednavka_id|castka|
|---|---|---|
|Jan Novak|101|5000|
|Eva Kral|102|3200|
|Petr Svoboda|103|4500|
|NULL|104|2800|

> Zobrazí všechny objednávky, i ty, které nemají existujícího zákazníka (`NULL` ve sloupci jméno).


---

### d) **FULL OUTER JOIN**

```sql
SELECT z.jmeno, o.objednavka_id, o.castka
FROM zakaznici z
FULL OUTER JOIN objednavky o
ON z.zakaznik_id = o.zakaznik_id;
```

**Example output:**

|jmeno|objednavka_id|castka|
|---|---|---|
|Jan Novak|101|5000|
|Eva Kral|102|3200|
|Petr Svoboda|103|4500|
|Marie Novak|NULL|NULL|
|NULL|104|2800|

> Zahrnuje všechny zákazníky i všechny objednávky; pokud není shoda, zobrazí `NULL`.

