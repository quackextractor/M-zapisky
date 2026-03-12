### **1. Architektura MySQL**
##### **Logická struktura, popis bloků**
*  **Klient:** Aplikace, pomocí které se uživatel připojuje k serveru.
*  **Server:** Samotná MySQL instance, kde jsou uložena data.
*  **mysqld (daemon):** Vícevláknový proces běžící na pozadí, který spravuje příchozí a odchozí požadavky. Přiděluje připojení unikátní **thread_id** po celou dobu trvání *session*.
*  **Parser (analyzátor):** Kontroluje syntaxi SQL příkazů, generuje jedinečné **sql_id** a ověřuje uživatelská oprávnění.
*  **Optimizer:** Připravuje *execution plan* (prováděcí plán přístupu na disk). Pracuje multisessionově pro každý storage engine zvlášť, protože práce s diskem je nejpomalejší.
*  **Metadata cache:** Paměť pro metadata (názvy tabulek, procedur, uživatelská práva) a statistiky.
*  **Query Cache:** Uchovává předchozí, již zanalyzované příkazy. Zrychluje zpracování pomocí "předpřipravených dat".
*  **Key Cache:** Paměť pro indexy. U malých indexů načte i data, u velkých je zde pouze B-strom.

##### **Fyzická struktura, adresář a jejich obsah**
Představuje vlastní realizaci systému jako souborový systém rozdělený do dvou hlavních složek:
1.  **MySQL base directory:**
    *  **Program files:** Knihovny, dokumenty.
    *  **Executables:** Spustitelné soubory jako `mysql`, `mysqld`, `mysqladmin`, `mysqldump`.
2.  **MySQL data directory:**
    *  **Systémová data:** Server log file, status file, system tablespace.
    *  **Data subdirectories:** Složky pro každou databázi obsahující data, indexy a struktury objektů (.frm soubory).

##### **Systémový katalog: Stručný popis**
*  Udržuje logickou strukturu objektů a metadata schématu (např. názvy atributů, omezení, struktury) uložených v rámci paměti *metadata cache* a v datových podsložkách.

---

### **2. Data Pipeline**
##### **OLTP/OLAP ... popis, rozdíl, význam**
*  **OLTP (Online Transaction Processing):** Systém běžící nad plně normalizovanou databází v běžném provozu. Je optimalizovaný pro časté transakce (velký počet operací INSERT, UPDATE, DELETE).
*  **OLAP (Online Analytical Processing):** Proces pro efektivní získávání dat z databáze (datového skladu). Skládá se z FACT a DIM tabulek a používá se pro pokročilé analýzy.
*  **Význam a rozdíl:** Zatímco OLTP slouží k operativnímu zajištění chodu organizace (konzistence, žádné redundance), OLAP denormalizuje data pro rychlé čtení rozsáhlých historických statistik a přehledů.

##### **ELT/ETL ... čištění dat, důvod použití, rozdíl ETL/ELT**
*  **ELT/ETL (Extract, Transform, Load / Extract, Load, Transform):** Procesy, které zajišťují přechod dat z plně normalizované databáze (OLTP) do analytické databáze (OLAP).
*  **Důvod použití a čištění dat:** Data se musí před analýzou očistit a transformovat, například se řeší chybějící povinné údaje (ty je nutné vrátit zpět ke zdroji) a navazují se unikátní klíče (Surrogate Keys) pro analytické potřeby.

---

### **3. Datový sklad (DWH): struktura, důvod použití**
##### **Rozdíl od normalizované databáze, použití v provozu, důvody**
*  Datový sklad je centrální úložiště dat z jednoho nebo více zdrojů optimalizované pro reporting a Business Intelligence, zatímco normalizovaná DB slouží pro běžný provoz a prevenci redundance dat.
*  DWH využívá denormalizaci (záměrné duplikování dat, předpočítané agregace), aby se minimalizoval počet spojování tabulek (JOINů) a razantně se zrychlilo složité vyhledávání a čtení přehledů.

##### **Typy DWH: Star DB, Snowflake, Galaxie DB: formát, rozdíly**
Skládají se z **FACT tabulek** (měřitelné údaje a cizí klíče) a **DIM tabulek** (číselníky jako kdo, co, kde, kdy).
1.  **Star Schema (Hvězda):** Nejjednodušší a nejrychlejší pro dotazování. Skládá se z jedné centrální FACT tabulky a okolních DIM tabulek, které jsou denormalizované (obsahují redundanci).
2.  **Snowflake Schema (Vločka):** Varianta hvězdy, kde jsou DIM tabulky naopak normalizované (rozvětvené do dalších podtabulek). Odstraňuje redundanci, ale znamená složitější dotazy (více JOINů) a pomalejší výkon.
3.  **Galaxy Schema (Galaxie / Fact Constellation):** Obsahuje více FACT tabulek, které navzájem sdílejí stejné DIM tabulky (*Conformed Dimensions*). Vhodné pro sledování vícero nezávislých procesů najednou.

---

### **4. Vizualizace dat**
##### **Princip a důvod**
*  **Princip:** Grafické znázornění informací a dat pomocí vizuálních prvků (grafy, mapy).
*  **Důvod:** Transformace abstraktních dat do srozumitelné formy (storytelling) za účelem efektivnějšího rozhodování založeného na faktech (*Data-driven decision making*) a pochopení trendů.

##### **Datové modely**
*  Zobrazení propojení dimenzionálních (DIM) a faktových (FACT) tabulek a tvorba jejich vzájemných vazeb.

##### **Tvorba vizualizací / Hlavní funkcionalita v Power BI**
1.  **Model View:** Pohled na schéma, vytváření vazeb mezi tabulkami (obdoba ER diagramu).
2.  **Power Query:** Nástroj umožňující editaci a transformaci databázových tabulek (zajišťuje proces ELT).
3.  **Dashboard:** Samotné vizualizační plátno s grafy, sloupci a tabulkami pro prezentaci výsledků.

##### **Import datové typy: csv, excel nebo online přímo ze serveru**
*  **Import:** Data se fyzicky nahrají do paměti aplikace (například jako nahrání textového `.csv` souboru).
*  **Direct Query (Live connection):** Připojení naživo přímo ke zdrojovému serveru nebo cloudu.

---

### **5. Zálohování a archivace**
##### **Rozdíl mezi archivací a zálohou dat**
*  **Archivace:** Uložení dat v co nejjednodušším formátu (csv, json) na dlouhou dobu (10+ let) většinou na jiný, zabezpečený server. Důvodem je ukládání historických dat pro pozdější audity, přístup k nim je málo častý.
*  **Záloha:** Uložení dat v plném formátu na aktivní server na krátkou dobu (1 minuta až 1 rok). Frekvence je pravidelná a slouží k rychlé obnově ztracených dat.

##### **Typy záloh**
*  Lze zálohovat celou databázi, část databáze, pouze provedené změny v databázi, nebo jednotlivé soubory včetně transakčního logu.

##### **Obnova dat**
*  Zálohy slouží k obnově po chybách úložného média (selhání disku), po uživatelských chybách (omylem smazaná tabulka) či výpadcích celého systému. Lze je také užít k administrativním přenosům mezi servery.

##### **Rozdíl mezi MSSQL a MySQL zálohováním**
*  *(Poznámka: Dodané materiály se explicitně nevěnují přímému srovnání procesů zálohování mezi MSSQL a MySQL. Text pouze uvádí, že pro MySQL lze pro uložení/export využít vestavěný spustitelný soubor `mysqldump` v základním adresáři a že archivní soubory obecně nelze jednoduše použít jako zálohu kvůli chybějícím systémovým souborům.)*