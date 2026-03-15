
# **1. Uložená procedura (stored procedure)**

### **Co je to + proč se používá**

* Uložený blok SQL příkazů na serveru.
* Automatizuje opakující se operace, snižuje přenos dat mezi aplikací a DB, hlídá logiku na jednom místě, zvyšuje bezpečnost.

### **Syntaxe – vytvoření / změna / smazání**

```sql
-- MySQL vytvoření
DELIMITER //
CREATE PROCEDURE proc_name(IN p1 INT, OUT p2 INT)
BEGIN
    SELECT p1 + 1 INTO p2;
END //
DELIMITER ;

-- změna
ALTER PROCEDURE proc_name COMMENT 'popis';
DROP PROCEDURE proc_name;

-- začátek změny
ALTER PROCEDURE dbo.proc_name
AS
BEGIN
    -- tělo...
END;
```

### **Typy procedur podle parametrů**

* **IN** – jen vstup
* **OUT** – jen výstup
* **INOUT** – vstup i výstup

### **Spuštění**

```sql
CALL proc_name(5, @vystup);
SELECT @vystup;
```

### **Rozdíl mezi procedurou a pohledem**

* **Procedura** = provádí akce, může měnit data, volá se `CALL`, může mít logiku.
* **Pohled (view)** = uložený SELECT, nic neprovádí, jen zobrazuje data.

---

# **2. Trigger**

### **Jak pomáhá udržet konzistenci při mazání**

* Umí automaticky reagovat na `DELETE` a např. ukládat záznamy do logu, ručně provádět kaskádové mazání nebo zabránit mazání.

### **Syntaxe – vytvoření / změna / smazání**

```sql
-- MySQL
DELIMITER //
CREATE TRIGGER trg_name
AFTER DELETE ON tabulka
FOR EACH ROW
BEGIN
    INSERT INTO log(t) VALUES (NOW());
END //
DELIMITER ;

-- MySQL změna
DROP TRIGGER trg_name;

-- MSSQL začátek změny
ALTER TRIGGER dbo.trg_name
ON dbo.tabulka
AFTER DELETE
AS
BEGIN
    -- tělo...
END;
```

### **Kdy je vhodné vytvářet trigger + jak se spustí**

* Když má DB reagovat automaticky (log, kontrola dat, ochrana).
* Spouští se **sám**, při akci `INSERT`, `UPDATE`, `DELETE`.

### **Jak může upravovat data**

* `BEFORE` může měnit `NEW` hodnoty před uložením.
* `AFTER` může zapisovat do jiných tabulek (logování, kaskády).

---

# **3. Funkce**

### **Co je uživatelská funkce + rozdíl od systémové**

* **Uživatelská funkce** = vytvořená programátorem, vrací hodnotu přes `RETURN`.
* **Systémová** = součást DB (NOW, AVG…). Nejde měnit.

### **Jak vypočítat průměrnou známku**

* Nejjednodušeji systémovou funkcí **`AVG()`**.

### **Syntaxe – vytvoření / změna / smazání**

```sql
-- MySQL
DELIMITER //
CREATE FUNCTION fn_name(x INT)
RETURNS INT
DETERMINISTIC
BEGIN
    RETURN x * 2;
END //
DELIMITER ;

-- MySQL změna
DROP FUNCTION fn_name;

-- MSSQL začátek změny
ALTER FUNCTION dbo.fn_name(@x INT)
RETURNS INT
AS
BEGIN
    RETURN @x * 2;
END;
```

### **Rozdíl skalární vs tabulková funkce**

* **Skalární** – vrací jednu hodnotu.
* **Tabulková** – vrací tabulku (běžné v MSSQL, ne v MySQL).

---

# **4. Životní cyklus databáze**

### **Která fáze je nejdůležitější**

* **Analýza** – špatná analýza = špatný návrh = špatná databáze.

### **Co je přínosné ukončení životního cyklu**

* Když je údržba dražší než nová DB.
* Ukončení umožní nasadit nový systém, odstranit historické chyby, zrychlit provoz a přizpůsobit se novým požadavkům.