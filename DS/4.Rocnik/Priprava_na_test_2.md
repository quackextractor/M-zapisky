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

## 4. GROUP BY a HAVING

Slouží k seskupování řádků a agregaci dat.

**GROUP BY:**
- Seskupí řádky se stejnou hodnotou ve vybraném sloupci.
- Povinné, pokud chceme ve výpisu kombinovat agregační funkce (např. `COUNT`) a neagregované sloupce.

**HAVING:**
- Filtruje výsledky **až po seskupení** (po GROUP BY).
- Používá se pro podmínky na agregační funkce (což `WHERE` neumí).

**Pořadí vyhodnocení dotazu:**
1.  `FROM` + `JOIN` (načtení dat)
2.  `WHERE` (filtrace řádků)
3.  `GROUP BY` (seskupení)
4.  `HAVING` (filtrace skupin)
5.  `SELECT` (výběr sloupců)
6.  `ORDER BY` (řazení)

**Příklad:**
*Vypsat oddělení, která mají více než 5 zaměstnanců.*
```sql
SELECT oddeleni, COUNT(*) as pocet
FROM zamestnanci
GROUP BY oddeleni       -- Seskupit podle oddělení
HAVING COUNT(*) > 5;    -- Vybrat jen ta, kde je počet > 5
```

---

## 5. TRIGGERY (Spouště)

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

## 6. Etapy vývoje databáze

Pro zkoušku je nutné znát posloupnost a obsah jednotlivých etap.

## Důležité diagramy
### 1) fáze: vytváření db

![[1-faze.svg]]

### 2) fáze: provoz db

![[faze-2.svg]]
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
