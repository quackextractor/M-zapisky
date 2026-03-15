
# **1. Pohled (view)**

### **Definice, co je pohled + proč "virtuální tabulka"**

* **Pohled** je uložený `SELECT` dotaz v databázi.
* **Virtuální tabulka** proto, že data fyzicky neukládá (pokud není materializovaný), ale pouze zobrazuje aktuální data z podkladových tabulek v momentě dotazu.

### **Syntaxe – vytvoření / změna / smazání**

```sql
-- MySQL vytvoření
CREATE VIEW view_name AS
SELECT sloupe1, sloupec2
FROM tabulka
WHERE podminka;

-- změna (nebo nahrazení)
CREATE OR REPLACE VIEW view_name AS
SELECT ...;

-- smazání
DROP VIEW view_name;
```

### **Kdy je vhodné vytvářet + použití pro zabezpečení**

* **Vhodnost:** Pro zjednodušení složitých dotazů (skrytí JOINů), pro opakované použití stejného výběru dat.
* **Zabezpečení:** Uživatel dostane práva jen k pohledu, nikoliv k celé tabulce. Můžeme tak skrýt citlivé sloupce nebo filtrovat řádky.

### **Spuštění**

* S pohledem se pracuje jako s běžnou tabulkou v příkazu `SELECT`.

```sql
SELECT * FROM view_name;
```

---

# **2. Trigger**

### **Co je trigger + typy**

* **Trigger** (spoušť) je procedura, která se automaticky spustí při určité události (změně dat) nad tabulkou.
* **Typy (timing):**
    * `BEFORE` – před provedením akce (kontrola dat).
    * `AFTER` – po provedení akce (logování).
    * `INSTEAD OF` – místo akce (často u pohledů).
- **Akce:**
	- `INSERT`
	- `UPDATE`
	- `DELETE`
### **Syntaxe – vytvoření / změna / smazání**

```sql
-- MySQL vytvoření
DELIMITER //
CREATE TRIGGER trg_name
BEFORE INSERT ON tabulka
FOR EACH ROW
BEGIN
    -- logika triggeru
END //
DELIMITER ;

-- MySQL smazání
DROP TRIGGER trg_name;
```

### **Kdy je vhodné vytvářet + spouštěcí události**

* **Vhodnost:** Pro automatickou integritu dat, logování historie změn, kaskádové operace.
* **Události:** `INSERT`, `UPDATE`, `DELETE`.

### **Dočasné tabulky (inserted/deleted, NEW/OLD)**

* Slouží k přístupu k datům v rámci logiky triggeru.
* **MySQL:**
    * `NEW` – obsahuje nová data (u `INSERT`, `UPDATE`).
    * `OLD` – obsahuje původní data (u `UPDATE`, `DELETE`).
* **MSSQL:** `inserted` a `deleted`.

---

# **3. Funkce**

### **Popis + typy funkcí**

* **Funkce** je databázový objekt (podprogram), který provede výpočet a vrací hodnotu.
* **Typy:**
    * **Agregační** (`SUM`, `AVG`, `COUNT`) – počítají nad více řádky.
    * **Systémové** (`NOW`, `VERSION`) – vestavěné v DB.
    * **Uživatelské** – definované programátorem.

### **Syntaxe – vytvoření uživatelské funkce**

```sql
DELIMITER //
CREATE FUNCTION fn_name(param INT)
RETURNS INT
DETERMINISTIC
BEGIN
    RETURN param * 2;
END //
DELIMITER ;
```

### **Kdy používat + spuštění**

* **Použití:** Pro výpočty, formátování nebo transformaci dat přímo v SQL dotazech.
* **Spuštění:** Volá se v rámci `SELECT` nebo v podmínkách `WHERE`.

```sql
SELECT fn_name(10);
```

### **Rozdíl od uložené procedury**

* **Funkce:** Musí vracet hodnotu (`RETURN`), volá se v rámci výrazu (`SELECT`), nemůže obsahovat transakce.
* **Procedura:** Volá se `CALL`, může vracet více hodnot přes `OUT` parametry, může řídit transakce, slouží pro složitější logiku.

---

# **4. Životní cyklus databáze**

### **Blokové schéma (etapy) + popis**

1. **Analýza** – Sběr a rozbor požadavků, zjištění informačních potřeb, identifikace datových toků.
2. **Návrh** – Vytvoření ER diagramu (konceptuální schéma), transformace na relační schéma, normalizace.
3. **Implementace** – Fyzické vytvoření databáze (SQL skripty), tabulek a pohledů.
4. **Testování** – Ověření funkčnosti na testovacích datech, ladění výkonu.
5. **Provoz (Nasazení)** – Plnění ostrými daty, reálné využívání uživateli.
6. **Údržba** – Zálohování, optimalizace, úpravy dle nových požadavků.

### **Co prozradí datová analýza**

* Definuje, jaká data budeme ukládat a jaké jsou mezi nimi vztahy.
* Určuje vstupy a výstupy systému (datové toky).
* Je klíčová pro správný návrh struktury (špatná analýza vede ke špatnému návrhu).