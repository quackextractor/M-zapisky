# Typy procedur

* **Bez parametrů**
* **Se vstupními parametry (IN)**
* **S výstupními parametry (OUT)**
* **S oběma typy parametrů – doporučeno pro maturitu**

---

# Příklad procedury s IN i OUT parametry (MySQL)

```sql
DELIMITER $$

CREATE PROCEDURE zvys_plat(
    IN id_zam INT, 
    IN kolik INT, 
    OUT novy_plat INT
)
BEGIN
    UPDATE zamestnanci
    SET plat = plat + kolik
    WHERE id = id_zam;

    SELECT plat INTO novy_plat 
    FROM zamestnanci 
    WHERE id = id_zam;
END$$

DELIMITER ;
```

**Volání:**

```sql
CALL zvys_plat(3, 2000, @vysledek);
SELECT @vysledek;
```

---

# Funkce

**Typy:**

* a) Agregační: `SUM()`, `COUNT()`, `AVG()`, `MAX()`, `MIN()`
* b) Systémové: `SYSDATE()`, `YEAR()`, `USER()`
* c) Uživatelské (vlastní)

**Vlastnosti:**

* mají jeden nebo více vstupních parametrů
* **vždy jen 1 návratovou hodnotu**
* lze použít za **SELECT**

---

# Uživatelsky definované funkce

## a) Skalární funkce – příklad MySQL

```sql
DELIMITER $$

CREATE FUNCTION celkem_s_dph(cena DECIMAL(10,2))
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
  RETURN cena * 1.21;
END$$

DELIMITER ;
```

**Použití:**

```sql
SELECT celkem_s_dph(100);
```

---

## b) Uživatelská funkce vracející tabulku

* Návratový typ je **tabulka** → `RETURN table` (v MySQL nelze přímo, v MSSQL/PostgreSQL ano)
* Syntaxe je:

```sql
SELECT * FROM <view> (...);
```

* Funkce **nemůže** volat procedury.

MySQL **tohle neumí přes RETURNS TABLE**, to je funkce z MSSQL/PostgreSQL.
V MySQL se místo toho používá **VIEW** nebo **procedura**, protože funkce může vrátit jen 1 skalární hodnotu.

Pro úplnost – takto vypadá styl v MSSQL:

```sql
CREATE FUNCTION seznam_zbozi()
RETURNS TABLE
AS
RETURN (
    SELECT * FROM zbozi
);
```