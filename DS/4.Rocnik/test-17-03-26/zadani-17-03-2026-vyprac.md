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

**1. Architektura MySQL**

* Popište **fyzickou strukturu** MySQL (význam datového adresáře a typy souborů).

**1. MySQL base directory (Základní adresář)**
Adresář programu MySQL:
* **Program files:** Obsahuje systémové knihovny, dokumenty a specifické soubory (např. pro systém UNIX).
* **Executables (Spustitelné soubory):** Obsahuje důležité spouštěcí programy a nástroje, jako jsou 
	* `mysql` (klient), 
	* `mysqld` (hlavní proces neboli daemon běžící na pozadí), 
	* `mysqladmin`
	* a `mysqldump`

**2. MySQL data directory (Datový adresář)**
* **Systémová data:** Obsahují soubory nezbytné pro globální správu a chod serveru. Patří sem 
	* logovací soubory serveru (server log file)
	* stavový soubor (status file)
	* transakční `.ib` log 
	* soubory
	* systémový tablespace
* **Datové podadresáře (Data subdirectories):** Pro každou vytvořenou databázi existuje uvnitř datového adresáře samostatný podadresář. Tyto složky uvnitř ukrývají katalogy, indexy, samotná data a soubory definující strukturu databázových objektů (jako jsou například soubory s příponou `.frm`).


* Jak MySQL pracuje s pamětí a proč je tato komponenta zásadní pro výkon?
* K čemu slouží **Systémový katalog** z pohledu administrátora a jaká metadata obsahuje?

**2. Datové sklady (DWH)**

* Definujte **datový sklad (DWH)**, popište jeho typickou strukturu a hlavní důvod použití.
* Vysvětlete, proč se do vizualizací obvykle nepřenášejí data **přímo z provozních (OLTP)** databází.
* Popište rozdíl mezi architekturou **Star Schema** (hvězda) a **Snowflake** (vločka).
* Vysvětlete, co je to **faktová tabulka** a **dimenze**.

**3. Zálohování a archivace**

* Proč používáme **archivaci dat** a jaké typy souborových formátů jsou pro ni vhodné?
* Co je to **diferenciální záloha** a v čem je její výhoda oproti plné záloze?
* K čemu se v databázi používá **transakční log** při výpadku systému?

**4. Vizualizace a Power BI**

* Popište hlavní **funkcionalitu** Power BI.
* Popište proces **čištění dat (Power Query)** a uveďte 3 příklady transformací.
* Uveďte 3 základní **typy vizualizací** a vysvětlete, jaký typ dat/analýzy na nich zobrazujeme.