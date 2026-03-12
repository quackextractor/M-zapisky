## **1. Architektura MySQL**

### **Jaká je logická struktura MySQL a co dělají jednotlivé bloky?**

* **Klient:** Aplikace, pomocí které se uživatel připojuje k serveru.
* **Server:** Samotná MySQL instance, kde jsou uložena data.
* **mysqld (daemon):** Vícevláknový proces běžící na pozadí, který spravuje příchozí a odchozí požadavky a přiděluje připojení unikátní **thread_id**.
* **Parser (analyzátor):** Kontroluje syntaxi SQL příkazů, generuje **sql_id** a ověřuje uživatelská oprávnění.
* **Optimizer:** Připravuje **execution plan** (prováděcí plán) pro přístup na disk.
* **Metadata cache:** Paměť pro metadata, jako jsou názvy tabulek, procedur a uživatelská práva.
* **Query Cache:** Uchovává předchozí analyzované příkazy pro zrychlení zpracování.
* **Key Cache:** Paměť pro indexy, u velkých indexů obsahuje B-strom.

### **Jak vypadá fyzická struktura a co obsahují hlavní adresáře?**

* **MySQL base directory:** Obsahuje programové soubory (knihovny, dokumenty) a spustitelné soubory jako `mysql`, `mysqld` nebo `mysqldump`.
* **MySQL data directory:** Obsahuje systémová data (logy, status file) a podadresáře pro jednotlivé databáze s daty a strukturami objektů (.frm soubory).

### **Co je to systémový katalog?**

* Systémový katalog udržuje logickou strukturu objektů a metadata schématu, jako jsou názvy atributů a omezení.

---

## **2. Data Pipeline**

### **Co jsou OLTP a OLAP, jaký je mezi nimi rozdíl a význam?**

* **OLTP (Online Transaction Processing):** Systém nad plně normalizovanou databází optimalizovaný pro časté transakce (INSERT, UPDATE, DELETE) a běžný provoz.
* **OLAP (Online Analytical Processing):** Proces pro efektivní získávání dat z datového skladu pro pokročilé analýzy.
* **Rozdíl:** OLTP zajišťuje operativní chod a konzistenci bez redundancí, zatímco OLAP data denormalizuje pro rychlé čtení rozsáhlých statistik.

### **Jak fungují procesy ETL/ELT a proč se provádí čištění dat?**

* **Definice:** Jsou to procesy zajišťující přechod dat z OLTP do analytického OLAP skladu.
* **Čištění dat:** Provádí se k vyřešení chybějících údajů a navázání unikátních klíčů (Surrogate Keys) pro analytické potřeby.

---

## **3. Datový sklad (DWH)**

### **Jaký je rozdíl mezi DWH a normalizovanou databází a proč se DWH používá?**

* **Rozdíl:** DWH je centrální úložiště optimalizované pro reporting a Business Intelligence, zatímco normalizovaná DB slouží pro běžný provoz.
* **Důvody použití:** DWH využívá denormalizaci a předpočítané agregace ke zrychlení složitých vyhledávání a minimalizaci počtu spojování tabulek (JOINů).

### **Jaké jsou typy DWH schémat a jak se liší?**

Skládají se z **FACT tabulek** (měřitelné údaje) a **DIM tabulek** (číselníky).

* **Star Schema (Hvězda):** Jedna centrální FACT tabulka a okolní denormalizované DIM tabulky. Je nejjednodušší a nejrychlejší pro dotazování.
* **Snowflake Schema (Vločka):** DIM tabulky jsou normalizované (rozvětvené). Odstraňuje redundanci, ale vede ke složitějším dotazům a pomalejšímu výkonu.
* **Galaxy Schema (Galaxie):** Obsahuje více FACT tabulek sdílejících stejné DIM tabulky. Vhodné pro sledování více nezávislých procesů.

[Image comparing Star schema, Snowflake schema, and Galaxy schema]

---

## **4. Vizualizace dat**

### **Jaký je princip a důvod vizualizace dat?**

* **Princip:** Grafické znázornění informací pomocí vizuálních prvků jako jsou grafy nebo mapy.
* **Důvod:** Transformace dat do srozumitelné formy pro efektivnější rozhodování založené na faktech (Data-driven decision making).

### **Co představují datové modely ve vizualizaci?**

* Zobrazují propojení DIM a FACT tabulek a tvorbu jejich vzájemných vazeb.

### **Jaká je hlavní funkcionalita v Power BI?**

* **Model View:** Pohled na schéma a vytváření vazeb mezi tabulkami.
* **Power Query:** Nástroj pro editaci a transformaci tabulek (zajišťuje proces ELT).
* **Dashboard:** Vizualizační plátno s grafy pro prezentaci výsledků.

### **Jaké jsou způsoby importu dat?**

* **Import:** Fyzické nahrání dat do paměti aplikace (např. z .csv nebo Excelu).
* **Direct Query (Live connection):** Připojení naživo přímo ke zdrojovému serveru nebo cloudu.

---

## **5. Zálohování a archivace**

### **Jaký je rozdíl mezi archivací a zálohou dat?**

* **Archivace:** Dlouhodobé uložení dat (10+ let) v jednoduchém formátu (csv, json) pro audity. Přístup je málo častý.
* **Záloha:** Krátkodobé uložení v plném formátu pro rychlou obnovu dat při ztrátě. Probíhá pravidelně.

### **Jaké existují typy záloh?**

* Lze zálohovat celou databázi, její část, pouze změny, nebo jednotlivé soubory včetně transakčního logu.

### **K čemu slouží obnova dat?**

* Slouží k nápravě po selhání disku, uživatelských chybách (smazání tabulky) nebo pro administrativní přenosy mezi servery.

### **Jaký je rozdíl mezi MSSQL a MySQL zálohováním?**


!!!! DODAT INFO, nemám zdroj !!!!

* MySQL využívá pro export vestavěný nástroj `mysqldump`.
* Archivní soubory obecně nelze použít jako přímou zálohu kvůli absenci systémových souborů.