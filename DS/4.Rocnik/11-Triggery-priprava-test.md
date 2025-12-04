# Teorie – poslední test

## View, procedury, funkce, triggery

U každého: co obsahuje, tipy, syntaxe, jak se spouští.

---

# VIEW

**Co to je:** uložený SELECT.
**Co má obsahovat:** definici dotazu.
**Syntaxe:**

```sql
CREATE VIEW jmeno AS
SELECT ...
```

**Spuštění:**

```sql
SELECT * FROM jmeno;
```

---

# PROCEDURY (se vstupními a výstupními parametry)

**Co to je:** uložený blok SQL příkazů.
**Obsahuje:** vstupní parametry, výstupní parametry, logiku.
**Syntaxe (MySQL):**

```sql
DELIMITER //
CREATE PROCEDURE jmeno(IN vstup INT, OUT vystup INT)
BEGIN
    SET vystup = vstup * 2;
END //
DELIMITER ;
```

**Spuštění:**

```sql
CALL jmeno(5, @out);
SELECT @out;
```

---

# FUNKCE

**Typy:**

1. **Agregační:** COUNT, SUM, AVG
2. **Systémové:** NOW, USER, VERSION
3. **Uživatelské:** vlastní funkce

**Parametry:**

* Agregační a systémové: 1 vstup
* Uživatelské: mohou mít více vstupů

**Syntaxe uživatelské funkce (MySQL):**

```sql
CREATE FUNCTION jmeno(param INT)
RETURNS INT
BEGIN
    RETURN param * 2;
END;
```

**Otázky:**
a) agregační
b) group by
c) having

---

# GROUP BY a HAVING

**GROUP BY:** seskupuje data
**HAVING:** filtruje agregace
Příklad:

```sql
SELECT oddeleni, COUNT(*)
FROM zam
GROUP BY oddeleni
HAVING COUNT(*) > 5;
```

---

# TRIGGER

**Co to je:** objekt uložený na serveru, navázaný na konkrétní tabulku.
**Spouští se automaticky** při INSERT, UPDATE, DELETE.
**Podobný proceduře, ale nemá vstupní parametry.**
**Používá systémové dočasné tabulky:**

* MSSQL: `inserted` a `deleted`
* MySQL: `NEW` a `OLD`

**Chování:**

* INSERT: `NEW` plná, `OLD` prázdná
* DELETE: `OLD` plná, `NEW` prázdná
* UPDATE: obě plné
* `NEW` a `OLD` jsou jen pro čtení

**Tipy:**

* BEFORE – spustí se před akcí
* INSTEAD OF – nahradí akci (hlavně u view)
* AFTER – spustí se po akci
* Max 6 triggerů na tabulku (before/after insert/update/delete)

**Použití:** automatické činnosti bez potvrzení (na rozdíl od procedur)

**Syntaxe (MySQL):**

```sql
DELIMITER //
CREATE TRIGGER trg_jmeno
BEFORE INSERT ON tabulka
FOR EACH ROW
BEGIN
    -- statements
END //
DELIMITER ;
```

---

# Etapy vývoje

(co obvykle chtějí u zkoušky)

1. Hotové schéma
2. Popis jednotlivých bloků
3. Detailní popis
4. Čtyři otázky z prezentace o etapách vývoje