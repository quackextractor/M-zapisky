# Příprava na test – Triggery, Procedury, Funkce, View, Etapy vývoje

Tento dokument shrnuje požadavky k testu a rozšiřuje je o informace z dostupných studijních materiálů.

---

## 1. VIEW (Pohledy)

**Co to je:**
- Uložený `SELECT` dotaz.
- Virtuální tabulka, která data fyzicky neukládá (pokud není materializovaná), ale jen zobrazuje data z jiných tabulek.

**Co má obsahovat:**
- Definici dotazu (SELECT).

**Syntaxe:**
```sql
-- Generic view creation
CREATE [OR REPLACE] VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

-- Using the view
SELECT * FROM view_name;
```


```sql
CREATE VIEW jmeno_pohledu AS
SELECT sloupec1, sloupec2
FROM tabulka
WHERE podminka;
```

**Spuštění / Použití:**
- S pohledem se pracuje jako s obyčejnou tabulkou.
```sql
SELECT * FROM jmeno_pohledu;
```

---

## 2. PROCEDURY (Uložené procedury)

**Co to je:**
- Uložený blok SQL příkazů na serveru.
- Může obsahovat logiku, cykly, podmínky.

**Parametry:**
- **IN (vstupní):** Data, která procedura přijme.
- **OUT (výstupní):** Data, která procedura vrátí (zapíše do proměnné).
- **INOUT:** Kombinace obou.

**Syntaxe (MySQL) – Příklad s IN i OUT:**
```sql
DELIMITER //

-- Generic procedure
CREATE PROCEDURE procedure_name(
    [IN param1 datatype,]
    [OUT param2 datatype,]
    [INOUT param3 datatype]
)
BEGIN
    -- SQL statements
    [SET var = value;]
    [SELECT ... INTO ...;]
    [UPDATE ...;]
    [INSERT ...;]
    [DELETE ...;]
END //

DELIMITER ;

-- Call the procedure
CALL procedure_name([param1_value, @param2_variable, param3_value]);
```


```sql
DELIMITER //

CREATE PROCEDURE zvys_plat(IN id_zam INT, IN kolik INT, OUT novy_plat INT)
BEGIN
    -- Aktualizace dat
    UPDATE zamestnanci
    SET plat = plat + kolik
    WHERE id = id_zam;

    -- Uložení nové hodnoty do výstupní proměnné
    SELECT plat INTO novy_plat
    FROM zamestnanci
    WHERE id = id_zam;
END //

DELIMITER ;
```

**Spuštění:**
- Procedura se volá klíčovým slovem `CALL`.
```sql
CALL zvys_plat(3, 2000, @vysledek); -- Volání s parametry
SELECT @vysledek;                   -- Zobrazení výstupní hodnoty
```

---

## 3. FUNKCE (Uživatelské funkce)

**Rozdělení funkcí:**
1.  **Agregační:** `COUNT`, `SUM`, `AVG`, `MAX`, `MIN` (pracují nad skupinou řádků).
2.  **Systémové:** `NOW`, `USER`, `VERSION`, `SYSDATE` (poskytuje DB systém).
3.  **Uživatelské:** Vlastní funkce definované programátorem.

**Vlastnosti uživatelských funkcí:**
- Mají vstupní parametry.
- **Musí vracet návratovou hodnotu** (`RETURNS`).
- Mohou být použity přímo v `SELECT` (např. `SELECT moje_funkce(sloupec) FROM tabulka`).
- V MySQL (na rozdíl od MSSQL) obvykle vrací skalární (jednu) hodnotu.

**Syntaxe uživatelské funkce (MySQL):**
```sql
DELIMITER //

-- Generic function
CREATE FUNCTION function_name(param1 datatype, ...)
RETURNS return_datatype
[DETERMINISTIC | NOT DETERMINISTIC]
[READS SQL DATA | MODIFIES SQL DATA]
BEGIN
    -- SQL statements
    RETURN expression;
END //

DELIMITER ;

-- Using the function
SELECT function_name(param1_value, ...);
```


```sql
DELIMITER //

CREATE FUNCTION spocitej_s_dph(cena DECIMAL(10,2))
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    RETURN cena * 1.21;
END //

DELIMITER ;
```

**Použití:**
```sql
SELECT spocitej_s_dph(100);
```

**Rozdíl oproti procedurám:**
- Funkce vrací hodnotu (`RETURN`), procedura ne (používá `OUT` parametry).
- Funkci voláme v rámci příkazu (např. `SELECT`), proceduru voláme `CALL`.

---

## 4. TRIGGERY (Spouště)

**Co to je:**
- Databázový objekt navázaný na konkrétní tabulku.
- **Spouští se automaticky** při události: `INSERT`, `UPDATE`, `DELETE`.
- Nemá vstupní parametry.

**Systémové (dočasné) tabulky v triggeru:**
Uvnitř triggeru máme přístup k původním a novým datům:
*   **MySQL:** `OLD` (původní data), `NEW` (nová data).
*   **MSSQL:** `deleted`, `inserted`.

**Dostupnost dat podle operace:**
*   **INSERT:** `NEW` obsahuje vkládaná data, `OLD` je prázdná.
*   **DELETE:** `OLD` obsahuje mazaná data, `NEW` je prázdná.
*   **UPDATE:** `OLD` obsahuje star data, `NEW` nová data.
*   *Poznámka:* Tyto tabulky jsou Read-Only.

**Typy triggerů (kdy se spouští):**
*   `BEFORE` – před provedením akce (kontrola dat, úprava před uložením).
*   `AFTER` – po provedení akce (logování, kaskádové změny).
*   `INSTEAD OF` – místo akce (často u pohledů).

**Syntaxe (MySQL) – Příklad:**
```sql
DELIMITER //

-- Generic trigger
CREATE TRIGGER trigger_name
{BEFORE | AFTER} {INSERT | UPDATE | DELETE} ON table_name
FOR EACH ROW
BEGIN
    -- Trigger logic using OLD and NEW
    [IF condition THEN
        SET NEW.column = value;
     END IF;]
    [INSERT INTO log_table(...) VALUES(...);]
END //

DELIMITER ;
```


```sql
DELIMITER //

CREATE TRIGGER trg_kontrola_plat
BEFORE INSERT ON zamestnanci
FOR EACH ROW
BEGIN
    -- Pokud je vkládaný plat menší než 0, nastaví se na 0
    IF NEW.plat < 0 THEN
        SET NEW.plat = 0;
    END IF;
END //

DELIMITER ;
```

---

## 5. Etapy vývoje databáze

Pro zkoušku je nutné znát posloupnost a obsah jednotlivých etap.

## Důležité diagramy
### 1) fáze: vytváření db

![[1-faze.svg]]

### 2) fáze: provoz db

![[faze-2.svg]]

## Otázky z [prezentace](https://moodle.spsejecna.cz/pluginfile.php/14379/mod_resource/content/1/DS%20%C5%BDivotn%C3%AD%20cyklus%20datab%C3%A1ze.pdf) a odpovědi

### **1. Co je životní cyklus databáze**

- šest fází:  
    – analýza  
    – návrh  
    – implementace  
    – testování  
    – provoz  
    – údržba

- popisuje celý proces vzniku, používání a konce databáze  

---

### **2. Nej­důležitější fáze životního cyklu**

- analýza
- rozhoduje o pochopení organizace, dat, problémů, požadavků
- špatná analýza = špatný návrh i celá databáze  
---

### **3. Co prozradí datová analýza**

- definuje potřebná data a jejich vazby
- určuje datové toky (vstupy, výstupy, transformace)
- vytváří konceptuální model, např. E-R diagram
- slouží jako most mezi uživatelem a tvůrcem databáze  

---

### **4. Příčina ukončení životního cyklu databáze**

- údržba se stane dražší než vytvoření nové databáze
- typicky kvůli nárůstu objemu dat nebo novým zdrojům dat
- následuje zánik staré a začátek nové ve fázi analýzy  

---

## Fáze podrobně

### 1. Analýza
*   Zjišťování požadavků (konzultace s klientem/firmou).
*   Analýza organizace (HW/SW), analýza dat (vstupy, výstupy).
*   Určení rolí a práv.

#### a) analýza organizace
- analýza HW + SW, případně návrh nového HW + SW
- nastavení účtů, rolí a práv: **konzultace s firmou**
- analýza typů datových souborů (.csv) + četnost vstupů
- analýza typů záloh, čas zálohy
#### b) analýza db (nová, stávající)
- nová: sledujeme požadavky firmy
- stávající: sledujeme problémy a chyby existující db

### 2. Návrh (Design)
*   **a) Logické schéma:**
    *   Určení entit a vazeb (ER diagram).
    *   Normalizace (převedení do normálních forem k odstranění redundance).
    *   Dekompozice vztahů M:N (vazební tabulky).
*   **b) Relační schéma:**
    *   Konkrétní tabulky, sloupce.
    *   Primární (PK) a cizí (FK) klíče (integritní omezení).
    *   Datové typy (doménová integrita).

### 3. Implementace
*   Vytvoření fyzické DB na serveru (DDL příkazy).
*   Tvorba tabulek, nastavení klíčů.
*   Tvorba procedurální části: View, procedury, funkce, triggery, indexy.

### 4. Testování
*   Vložení testovacích dat (mock data).
*   Ověření integrity, test redundance.
*   Test funkčnosti procedur a dotazů.
*   Ověření zálohování.

### 5. Nasazení do provozu (Deployment)
*   Nahrání finální struktury DB k uživateli.
*   Import ostrých (živých) dat.
*   Otestování v reálném provozu.
*   Předání zákazníkovi.

### 6. Údržba a optimalizace
*   Správa uživatelů.
*   Monitorování výkonu, přidávání indexů (optimalizace).
*   Pravidelné zálohování.
*   Archivace starých dat.
