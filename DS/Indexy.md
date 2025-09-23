# Dokumentace k Indexům v MSSQL

## Co je to Index?

Index v SQL Serveru je databázová struktura, která zrychluje vyhledávání dat v tabulkách. Funguje podobně jako rejstřík v knize – místo prohledávání celé tabulky umožňuje rychlý přístup k požadovaným řádkům.

## Vytvoření Indexu

Indexy se vytvářejí pomocí příkazu `CREATE INDEX`.

### Syntaxe:

```sql
CREATE INDEX nazev_indexu
ON tabulka (sloupec1, sloupec2, ...);
```

### Příklad:

Pokud máme tabulku `Zamestnanci` a chceme vytvořit index na sloupci `Prijmeni` pro rychlejší hledání podle příjmení:

```sql
CREATE INDEX idx_prijmeni
ON Zamestnanci (Prijmeni);
```

## Typy Indexů

### 1. **Clustered Index (Klastrovaný index)**

- Určuje fyzické uspořádání dat v tabulce.
- Každá tabulka může mít maximálně **jeden** klastrovaný index.
- Pokud není explicitně vytvořen, primární klíč tabulky obvykle tvoří klastrovaný index.
- **Vytvoření klastrovaného indexu:**
    
    ```sql
    CREATE CLUSTERED INDEX idx_zamestnanci_id
    ON Zamestnanci (EmployeeID);
    ```
    

### 2. **Non-Clustered Index (Neklastrovaný index)**

- Ukládá ukazatele na skutečné řádky tabulky.
- Lze vytvořit více neklastrovaných indexů na jednu tabulku.
- **Vytvoření neklastrovaného indexu:**
    
    ```sql
    CREATE NONCLUSTERED INDEX idx_pozice
    ON Zamestnanci (Pozice);
    ```
    

### 3. **Unique Index (Unikátní index)**

- Zajišťuje, že hodnota v indexovaném sloupci je jedinečná.
- **Příklad:**
    
    ```sql
    CREATE UNIQUE INDEX idx_email
    ON Zamestnanci (Email);
    ```
    

### 4. **Filtered Index (Filtrováný index)**

- Obsahuje pouze určitou část dat podle filtru.
- **Příklad:**
    
    ```sql
    CREATE INDEX idx_aktivni_zamestnanci
    ON Zamestnanci (Prijmeni)
    WHERE Aktivni = 1;
    ```
    

### 5. **Full-Text Index (Fulltextový index)**

- Používá se pro fulltextové vyhledávání v textových sloupcích.
- **Příklad:**
    
    ```sql
    CREATE FULLTEXT INDEX ON Produkty(Nazev)
    KEY INDEX pk_produkty;
    ```
    

## Odstranění Indexu

Index lze odstranit pomocí `DROP INDEX`:

```sql
DROP INDEX idx_prijmeni ON Zamestnanci;
```

## Výhody použití Indexů

- **Zrychlení dotazů** – indexy umožňují rychlé vyhledávání dat.
- **Optimalizace výkonu** – méně zpracovávaných řádků znamená menší zatížení serveru.
- **Zajištění jedinečnosti** – unikátní indexy zabraňují duplicitním hodnotám.

## Nevýhody použití Indexů

- **Zpomalení operací `INSERT`, `UPDATE`, `DELETE`** – při změně dat je nutné index aktualizovat.
- **Zvýšené nároky na úložiště** – každý index zabírá místo v databázi.
- **Komplexita správy** – příliš mnoho indexů může vést k neefektivnímu výkonu.

## Nejlepší praktiky pro indexování

- Používat indexy na sloupce, které se často používají ve `WHERE`, `JOIN` nebo `ORDER BY`.
- Nepoužívat indexy na sloupce s nízkou kardinalitou (např. pohlaví, boolean hodnoty).
- Pravidelně analyzovat a optimalizovat indexy pomocí `sys.dm_db_index_usage_stats`.

Indexy jsou klíčovým nástrojem pro optimalizaci výkonu v MSSQL a správné použití může výrazně zrychlit databázové operace.