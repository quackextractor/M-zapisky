# **Test A**

**1. Architektura MySQL**

* Popište **logickou strukturu** MySQL (jednotlivé bloky).
* Vysvětlete, jak probíhá **zpracování dotazu**.
* Co je to **Storage Engine** a jaký je hlavní rozdíl mezi **InnoDB** a **MyISAM**?

**2. Data Pipeline & DWH**

* Vysvětlete rozdíl mezi systémy **OLTP a OLAP** a uveďte příklad použití pro každý z nich.
* Jaký je rozdíl mezi **ETL a ELT** procesy? Stručně popište jednotlivé fáze.
* Vysvětlete pojem **Surrogate Keys** (náhradní klíče) a proč se používají v DWH.

**3. Zálohování a archivace**

* Vysvětlete rozdíl mezi **zálohou (backup)** a **archivací dat** (uveďte příklad pro obojí).
* Jaké základní **typy záloh** znáte a jaký je význam **transakčního logu**.
* Popište proces **obnovy dat (recovery)** – co je jeho cílem?

**4. Vizualizace a Power BI**

* Popište hlavní komponenty **Power BI Desktop**.
* Co jsou **relace** v datovém modelu a proč jsou nezbytné pro správnou vizualizaci?
* K čemu se v Power BI používá jazyk **DAX**?
* Vyjmenujte 3 základní **typy grafů** a uveďte, pro jaký účel se hodí.


# **Test B**

## **1. Architektura MySQL**

#### 1.1 Popište **fyzickou strukturu** MySQL (význam datového adresáře a typy souborů).

Fyzická struktura MySQL se skládá ze dvou hlavních částí:

**1. Základní adresář (Base directory)**
Obsahuje systémové knihovny a **hlavní spustitelné programy**.
* **mysqld:** Hlavní proces serveru běžící na pozadí.
* **mysql:** Klientská aplikace.
* Pomocné nástroje: mysqladmin a mysqldump.

**2. Datový adresář (Data directory)**
Zajišťuje **ukládání skutečných dat a chod serveru**.
* **Systémová data:** Obsahují globální soubory pro správu, jako jsou **logy serveru, transakční logy a systémový tablespace**.
* **Datové podadresáře:** Každá databáze má vlastní složku, která ukrývá její **samotná data, indexy a definiční soubory struktury (.frm)**.


#### 1.2 Jak MySQL pracuje s pamětí a proč je tato komponenta zásadní pro výkon?

**MySQL využívá paměť primárně k minimalizaci pomalých operací na fyzickém disku.**
	Paměť se dělí do dvou hlavních úrovní:
	
**1. Cache (Mezipaměť na úrovni serveru)**
	Uchovává menší informace pro rychlou přípravu dotazů.
- **Query Cache:** Ukládá **již provedené a zkontrolované SQL dotazy**.	
- **Metadata Cache:** Uchovává **definice struktury databáze** (tabulky, práva), nikoliv uživatelská data.
- **Key Cache:** Ukládá **indexy** k právě zpracovávaným tabulkám.
	    
**2. Buffer (Vyrovnávací paměť na úrovni Storage Engines)**
Obsluhuje přímou komunikaci s fyzickým diskem.
- Načítá a uchovává **větší objemy skutečných datových bloků**.
- Umožňuje (například u jádra InnoDB) **efektivní a rychlé transakční zpracování (ACID)**.
- Je **kapacitně větší, ale mírně pomalejší** než cache.

**Proč je paměť zásadní pro výkon?**
* Výkon databáze je limitován rychlostí přístupu k datům, přičemž **čtení z disku je nejpomalejší operací**.
* Optimalizátor se proto snaží **minimalizovat přístupy na disk** při sestavování prováděcího plánu.
* Ukládání dotazů, struktury a indexů do rychlé paměti **drasticky snižuje zátěž disku a šetří procesorový čas**.
* Výsledkem je **mnohonásobně rychlejší odbavování požadavků klientů**.

 #### 1.3 K čemu slouží **Systémový katalog** z pohledu administrátora a jaká metadata obsahuje?

## **2. Datové sklady (DWH)**

#### 2.1 Definujte **datový sklad (DWH)**, popište jeho typickou strukturu a hlavní důvod použití.
#### 2.2 Vysvětlete, proč se do vizualizací obvykle nepřenášejí data **přímo z provozních (OLTP)** databází.
#### 2.3 Popište rozdíl mezi architekturou **Star Schema** (hvězda) a **Snowflake** (vločka).
#### 2.4 Vysvětlete, co je to **faktová tabulka** a **dimenze**.

## **3. Zálohování a archivace**

#### 3.1 Proč používáme **archivaci dat** a jaké typy souborových formátů jsou pro ni vhodné?
#### 3.2 Co je to **diferenciální záloha** a v čem je její výhoda oproti plné záloze?
#### 3.3 K čemu se v databázi používá **transakční log** při výpadku systému?

## **4. Vizualizace a Power BI**

#### 4.1 Popište hlavní **funkcionalitu** Power BI.
#### 4.2 Popište proces **čištění dat (Power Query)** a uveďte 3 příklady transformací.
#### 4.3 Uveďte 3 základní **typy vizualizací** a vysvětlete, jaký typ dat/analýzy na nich zobrazujeme.