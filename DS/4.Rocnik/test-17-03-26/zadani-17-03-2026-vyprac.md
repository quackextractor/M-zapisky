# Test A

Zde je vypracování zadaných otázek pro **Test A** přesně podle požadovaného formátu, struktury a hloubky, která odpovídá vypracování Testu B.

### Test A

#### 1. Architektura MySQL

##### 1.1 Popište logickou strukturu MySQL (jednotlivé bloky).
Logické hledisko MySQL architektury představuje blokové schéma zpracování připojení a příkazů. Skládá se z těchto klíčových komponent:
*   **Klient:** Aplikace (rozhraní), pomocí které se uživatel připojuje k serveru a odesílá požadavky.
*   **Server (mysqld / daemon):** Hlavní vícevláknový proces na pozadí, který obsluhuje příchozí připojení (vytváří *session* s unikátním `thread_id`) a spravuje data.
*   **Parser (Analyzátor):** Modul kontrolující SQL syntaxi a oprávnění. Každému příkazu přidělí jedinečné `sql_id`.
*   **Cache a Buffery:** Paměťové bloky určené pro optimalizaci. Patří sem **Query Cache** (předpřipravené a již zkontrolované dotazy), **Metadata Cache** (struktury, názvy a omezení) a **Key Cache** (vyhledávací stromy a indexy).
*   **Optimizer:** Modul zodpovědný za sestavení nejefektivnějšího prováděcího plánu (Execution plan) přístupu na fyzický disk pro každé úložiště zvlášť, čímž minimalizuje pomalou práci s diskem.
*   **Storage Engine:** Různé softwarové nástavby spravující samotné fyzické ukládání, I/O operace a zabezpečení dat na disku.

![mysql-logical-architecture](mysql-logical-architecture.png)


##### 1.2 Vysvětlete, jak probíhá zpracování dotazu.
Zpracování SQL dotazu probíhá v několika fázích pro zajištění maximální rychlosti a bezpečnosti:
1.  **Příjem a syntaktická analýza:** Klient odešle SQL dotaz, který zachytí proces *mysqld*. Předá jej **Parseru**, který zkontroluje správnost syntaxe a oprávnění uživatele.
2.  **Hledání v Query Cache:** Server se podívá do rychlé mezipaměti (Query Cache), zda se v ní již nachází výsledek shodného dotazu z předchozích volání. Pokud ano, Parser mu pouze přiřadí nové `sql_id` a systém ihned vrací hotová data bez další práce (využije předpřipravená data).
3.  **Optimalizace:** Pokud dotaz v cache není, předá se **Optimizeru**, který s ohledem na velikost tabulek a dostupnost indexů z *Key Cache* navrhne optimální cestu (Execution plan) pro čtení z disku.
4.  **Provedení ve Storage Engine:** Optimizer tento plán předá konkrétnímu úložišti (Storage Engine), které načte a zpracuje fyzická data z disku a vrátí je klientovi.

##### 1.3 Co je to Storage Engine a jaký je hlavní rozdíl mezi InnoDB a MyISAM?
**Storage Engine** je specializovaný softwarový modul v MySQL, který má na starosti fyzický *file management* – tedy provádí vlastní SQL příkazy pro načítání, ukládání dat a obsluhu určité oblasti na pevném disku.

**Hlavní rozdíly:**
*   **InnoDB:** Je **transakční engine**, který plně podporuje principy ACID (spolehlivost transakcí) a pro zajištění bezpečnosti v multithreadovém provozu provádí přesné **zamykání na úrovni jednotlivých řádků** (low-level locking).
*   **MyISAM:** Je **netransakční engine**, který poskytuje velmi **rychlé čtení velkých objemů dat** na úkor transakčního zabezpečení. Místo řádků zamyká při zápisech celé tabulky. Často se využívá jako rychlé úložiště pro Query cache nebo pro zpracování předpřipravených indexů.

#### 2. Data Pipeline & DWH

##### 2.1 Vysvětlete rozdíl mezi systémy OLTP a OLAP a uveďte příklad použití pro každý z nich.
Rozdíl spočívá v cílovém zaměření a struktuře databáze:
*   **OLTP (Online Transaction Processing):** Systém určený pro běžný každodenní chod aplikace. Je **plně normalizovaný (např. do 3. NF)**, zaměřuje se na bezpečnost a co nejrychlejší provádění ohromného množství jednoduchých transakcí (INSERT, UPDATE, DELETE).
    *   *Příklad použití:* Provozní systém zvířecího útulku, kam operátor v reálném čase zadává informace o přijetí a adopci zvířat.
*   **OLAP (Online Analytical Processing):** Systém optimalizovaný pro analýzu masivních historických dat a tvorbu reportů, tedy pro intenzivní operace čtení. Databáze je cíleně **denormalizovaná** (např. Star Schema) do podoby datového skladu, aby odpadlo zdržování složitým spojováním tabulek.
    *   *Příklad použití:* Business Intelligence nástroj managementu útulku, který z datového skladu najednou analyzuje trendy zisků a průměrnou délku pobytu jednotlivých ras za posledních pět let.

##### 2.2 Jaký je rozdíl mezi ETL a ELT procesy? Stručně popište jednotlivé fáze.
Oba procesy zajišťují extrakci, transformaci a nahrání dat (typicky při přesunu dat z produkčních OLTP databází do datového skladu), liší se však pořadím operací.

*   **ETL (Extract → Transform → Load):** Data se ze zdroje *extrahují*, následně se ihned *transformují* v mezikroku (např. pomocí dočasných staging tabulek, kde se data očistí od šumu a překalkulují), a až jako čistá normalizovaná data jsou *nahrána* do cílového systému.
*   **ELT (Extract → Load → Transform):** Data jsou ze zdroje nejprve *extrahována a rovnou nahrána* v surovém stavu do cílového systému (např. datového skladu či nástroje Power Query v Power BI). K jejich *transformaci* dochází až na úrovni tohoto finálního cílového nástroje.

##### 2.3 Vysvětlete pojem Surrogate Keys (náhradní klíče) a proč se používají v DWH.
**Surrogate Keys (SKs)** jsou uměle vygenerované, zcela nové unikátní klíče vytvořené speciálně pro potřeby datového skladu (OLAP). Zcela nahrazují původní přirozené klíče, popř. primární klíče produkční databáze (Natural Keys, PKs). 

**Důvody použití v DWH:**
*   Chrání analytický systém před neočekávanými změnami klíčů v původní produkční databázi.
*   Zjednodušují a sjednocují datový model, zejména pak tehdy, pokud datový sklad čerpá data z více nezávislých zdrojů, kde by mohlo docházet ke křížení různých formátů primárních klíčů.
*   Zrychlují výkon celého datového skladu, protože generovaný celočíselný klíč se velmi rychle porovnává při spojování (JOIN) velkých faktových a dimenzních tabulek.

#### 3. Zálohování a archivace

##### 3.1 Vysvětlete rozdíl mezi zálohou (backup) a archivací dat (uveďte příklad pro obojí).
*   **Záloha (Backup):** Znamená uchovávání plného databázového formátu a struktury za účelem rychlé obnovy dat po havárii. Jde typicky o krátkodobé zachování dat (1 minuta až 1 rok) na aktivním serveru a provádí se opakovaně v pravidelných frekvencích.
    *   *Příklad:* Každonoční plná záloha kompletní provozní databáze pro případ neplánovaného pádu disku serveru během následujícího dne.
*   **Archivace dat:** Jde o proces vyjmutí historických dat z databáze a jejich zmrazení do jednoduchého, univerzálního formátu (např. CSV, JSON v kódování UTF-8). Uchovává se dlouhodobě (10 a více let) na odlehlém, bezpečném serveru s předpokladem velmi zřídkavého přístupu.
    *   *Příklad:* Extrakce prodejních faktur a jejich uložení do CSV souboru pro možný účetní audit starší než 5 let. Z databáze jsou z důvodu úspory místa odmazány.

##### 3.2 Jaké základní typy záloh znáte a jaký je význam transakčního logu.
**Základní typy záloh:**
Zálohovat můžeme plně **celou databázi**, vybranou **část databáze**, zaznamenávat **změny v databázi** (tzv. diferenciální záloha), nebo pracovat s **jednotlivými soubory a transakčním logem**.

**Význam transakčního logu:**
Je kritickým prvkem při obnově do konzistentního stavu (např. po náhlém výpadku proudu). Eviduje veškeré operace, díky čemuž umožňuje záchranu potvrzených transakcí pomocí mechanismu **Redo** (vložení dat, co se nestihla propast na disk) a odvolání neúplných chybových dat pomocí **Undo** (návrat nekompletní transakce zpět).

##### 3.3 Popište proces obnovy dat (recovery) – co je jeho cílem?
Cílem obnovy dat (recovery) je **záchrana a návrat databáze ze zálohy do posledního známého bezchybného, a navíc konzistentního stavu** po různých krizových událostech. Obnova se typicky provádí za účelem záchrany provozních dat z těchto důvodů:
*   Po selhání a chybě fyzického úložného média (havárie pevného disku).
*   Po chybě ze strany uživatele (např. po omylném spuštění destrukčního příkazu jako smazání důležité tabulky).
*   Při nečekaném výpadku operačního systému či pádu MySQL daemona.

#### 4. Vizualizace a Power BI

##### 4.1 Popište hlavní komponenty Power BI Desktop.
Power BI Desktop obsahuje tři stěžejní moduly zajišťující proces od importu až po vizualizaci dat:
*   **Model View:** Modul sloužící pro zobrazení, organizaci a spojování (Joiny) **faktových a dimenzních tabulek**. Sestavuje se zde relační podoba podobná ER modelu.
*   **Power Query:** Nástroj určený pro přímou **transformaci a čištění dat** (tzv. ELT proces). Umožňuje z importovaných dat odstranit nepotřebné znaky, ošetřit chyby či vytvořit dodatečné atributy.
*   **Dashboard (Zobrazení sestavy):** Finální vrstva sloužící pro interaktivní vizualizaci. Pomocí nejrůznějších vizuálních prvků (mapy, sloupcové grafy, koláče) se tvoří reporty usnadňující rozhodování.

##### 4.2 Co jsou relace v datovém modelu a proč jsou nezbytné pro správnou vizualizaci?
Relace jsou vazby tvořené pomocí primárních (PK) a cizích klíčů (FK), které propojují centrální analytické tabulky (Faktové) s příslušnými číselníky (Dimenze) typicky ve schématu hvězdy nebo vločky.

Tyto propojení (Joiny) v **Model View** jsou naprosto nezbytné pro správnou vizualizaci, protože umožňují systému logicky pochopit kontext a provést správné křížové filtrování. Například aby systém dokázal posčítat agregovaná čísla jako *zisk* (z faktové tabulky) rozdělená podle popisků jako *jméno pobočky útulku* nebo *rasa zvířete* (z dimenzních tabulek).

##### 4.3 K čemu se v Power BI používá jazyk DAX?
**DAX (Data Analysis Expressions)** je specializovaný jazyk určený pro datové modelování. Využívá se k návrhu a sestavování **pokročilých výpočtů, logických pravidel a takzvaných měřítek (measures)** přímo nad existujícím modelem, které pouhé SQL a standardní agregační modely bez obtíží nedokážou obsáhnout.

##### 4.4 Vyjmenujte 3 základní typy grafů a uveďte, pro jaký účel se hodí.
*   **Karta (Card):** Ideální nástroj pro zvýraznění nejdůležitější **jediné agregované hodnoty**, například celkových tržeb či zisků, která funguje jako hlavní klíčový ukazatel výkonnosti (KPI) na vrchu Dashboardu.
*   **Koláčový graf (Pie chart):** Vhodný pro vizualizaci **procentuálního podílu částí na celku**, kde chceme porovnat malý počet odlišných kategorií a zjistit, která z nich tvoří největší objem dat.
*   **Sloupcový graf (Column chart):** Hodí se na přehledné **porovnávání konkrétních hodnot a metrik napříč různými kategoriemi** či na zobrazování jejich přesných trendů vyvíjejících se v čase (např. zobrazení fluktuace obratu napříč ročními obdobími).

---

# Test B

## 1. Architektura MySQL

### 1.1 Popište fyzickou strukturu MySQL (význam datového adresáře a typy souborů).

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

### 1.2 Jak MySQL pracuje s pamětí a proč je tato komponenta zásadní pro výkon?

**MySQL využívá paměť primárně k minimalizaci pomalých operací na fyzickém disku.**
Paměť se dělí do dvou hlavních úrovní:
	
**1. Cache (Mezipaměť na úrovni serveru)**
Uchovává menší informace pro rychlou přípravu dotazů.
* **Query Cache:** Ukládá **již provedené a zkontrolované SQL dotazy**.	
* **Metadata Cache:** Uchovává **definice struktury databáze** (tabulky, práva), nikoliv uživatelská data.
* **Key Cache:** Ukládá **indexy** k právě zpracovávaným tabulkám.
	    
**2. Buffer (Vyrovnávací paměť na úrovni Storage Engines)**
Obsluhuje přímou komunikaci s fyzickým diskem.
* Načítá a uchovává **větší objemy skutečných datových bloků**.
* Umožňuje (například u jádra InnoDB) **efektivní a rychlé transakční zpracování (ACID)**.
* Je **kapacitně větší, ale mírně pomalejší** než cache.

**Proč je paměť zásadní pro výkon?**
* Výkon databáze je limitován rychlostí přístupu k datům, přičemž **čtení z disku je nejpomalejší operací**.
* Optimalizátor se proto snaží **minimalizovat přístupy na disk** při sestavování prováděcího plánu.
* Ukládání dotazů, struktury a indexů do rychlé paměti **drasticky snižuje zátěž disku a šetří procesorový čas**.
* Výsledkem je **mnohonásobně rychlejší odbavování požadavků klientů**.

### 1.3 K čemu slouží Systémový katalog z pohledu administrátora a jaká metadata obsahuje?

**Systémový katalog je centrální informační registr o celé databázi.** Fyzicky je uložen v datových podadresářích spolu s daty a indexy.
Je nezbytný pro **správu, údržbu a zabezpečení**. Databázový systém z něj získává informace pro **kontrolu syntaxe, ověřování práv a tvorbu prováděcích plánů**.

Katalog slouží jako **úložiště metadat (definice a data o datech)**, neobsahuje uživatelská data. Konkrétně uchovává:
* **Definice struktury objektů:** Názvy tabulek, vlastnosti sloupců a celkové schéma.
* **Integritní omezení:** Pravidla pro konzistenci a správnost dat (primární a cizí klíče).
* **Programové objekty:** Definice uložených procedur a podobných objektů.
* **Bezpečnostní nastavení:** Uživatelské účty, role a přístupová práva.
* **Statistiky o objektech:** Informace pro optimalizaci a efektivní zpracování dotazů.

Pro zrychlení systému se často využívaná metadata **načítají přímo do operační paměti do Metadata Cache**, aby se předešlo pomalému vyhledávání na pevném disku.

## 2. Datové sklady (DWH)

### 2.1 Definujte datový sklad (DWH), popište jeho typickou strukturu a hlavní důvod použití.

**Definice datového skladu (DWH)**
Datový sklad (z anglického *Data Warehouse*) je centrální úložiště dat, která jsou shromažďována z jednoho nebo vícero nezávislých zdrojů. Je primárně **optimalizovaný pro potřeby analýzy, reportingu a business intelligence** a na rozdíl od běžných provozních databází slouží pro analytické procesy typu OLAP (Online Analytical Processing).

**Typická struktura**
Struktura datového skladu se liší od běžných plně normalizovaných databází. Zpravidla je organizována do specifických schémat, přičemž nejzákladnějším je **Star Schema (Hvězda)**. Dalšími variantami jsou *Snowflake Schema* (Vločka) nebo *Galaxy Schema* (Galaxie). 

Základní struktura se skládá ze dvou hlavních typů tabulek:
* **Faktové tabulky (FACT):** Tvoří střed schématu a obsahují měřitelné, kvantitativní údaje (např. tržby, náklady, délka pobytu) a klíče, které odkazují na tabulky dimenzí.
* **Dimenzní tabulky (DIM):** Obklopují faktovou tabulku a obsahují popisné údaje a číselníky (odpovídají na otázky "kdo, co, kde, kdy"). V nejběžnějším schématu hvězdy jsou dimenze **denormalizované**, což znamená, že záměrně obsahují redundantní (opakující se) data, aby se urychlilo vyhledávání. 

**Hlavní důvod použití**
Získávat komplexní byznysové informace a statistiky přímo z běžné provozní databáze (OLTP) je výkonnostně velmi náročné a pomalé, protože plně normalizovaná struktura vyžaduje pro získání výsledku spojování velkého množství tabulek (pomocí operací JOIN) a složité agregace. 

Hlavním důvodem nasazení DWH je tedy **rychlé a efektivní čtení rozsáhlých historických dat pro tvorbu přehledů a statistik**. V datovém skladu se data předem transformují a spojují (pomocí procesů ETL/ELT), čímž se radikálně snižuje nutnost spojování tabulek při samotném dotazování a analytické dotazy nad jedinou faktovou tabulkou jsou tak mnohonásobně rychlejší.

![star-generic](star-generic.png)
![star-example](star-example.png)

![snowflake-generic](snowflake-generic.png)
![snowflake-example](snowflake-example.png)

![galaxy-generic](galaxy-generic.png)
![galaxy-example](galaxy-example.jpg)

### 2.2 Vysvětlete, proč se do vizualizací obvykle nepřenášejí data přímo z provozních (OLTP) databází.

#### Proč se OLTP data nevizualizují přímo
* **OLTP databáze jsou navrženy pro rychlé transakce a zápisy**, nikoliv pro hromadné čtení.
* Z důvodu prevence redundance jsou **data vysoce normalizovaná a roztříštěná do mnoha tabulek**.
* Analytika přímo nad OLTP znamená **neúnosnou výkonnostní zátěž a pomalé dotazy**, protože databáze musí v reálném čase provádět složité agregace a spojování tabulek.

#### Standardní řešení
* Data se přesouvají do **datových skladů (DWH) nebo systémů OLAP**.
* Zde probíhá **denormalizace dat (jejich cílené sloučení do menšího počtu tabulek a předpočítání hodnot)**.
* Výsledkem je **výrazné zrychlení a zjednodušení analytických dotazů i vizualizací**.

### 2.3 Popište rozdíl mezi architekturou Star Schema (hvězda) a Snowflake (vločka).

#### Star Schema (Hvězda)
* **Charakteristika**: Nejjednodušší struktura s **přímým napojením dimenzí** na centrální faktovou tabulku.
* **Data**: Využívá **denormalizaci**, což znamená, že obsahuje redundantní (opakující se) data pro vyšší rychlost.
* **Výhody**: Nabízí **nejvyšší výkon při dotazování** a jednoduchost díky minimu spojování (JOIN) tabulek.

#### Snowflake Schema (Vločka)
* **Charakteristika**: Varianta hvězdy, kde se **dimenze dále větví** do podtabulek.
* **Data**: Využívá **normalizaci**, která odstraňuje duplicitu dat a šetří místo, ale zvyšuje strukturální složitost.
* **Nevýhody**: Vyžaduje **vícenásobné spojování tabulek (JOIN)**, což může vést ke **zpomalení výkonu** u rozsáhlých analýz.

### 2.4 Vysvětlete, co je to faktová tabulka a dimenze.

#### Faktová tabulka (FACT)
* Obsahuje **ústřední měřitelné metriky a číselné údaje** (např. cena, počet, zisk).
* Skládá se z **cizích klíčů odkazujících na dimenze** a samotných faktů.
* Představuje konkrétní událost nebo proces (např. prodej, adopce).

#### Dimenze (DIM)
* Poskytují **kontext k faktům** a obsahují **popisné atributy** (odpovídají na „kdo, co, kde, kdy“).
* Slouží jako číselníky pro filtrování a seskupování dat.
* V **Star Schema jsou denormalizované** (rychlost), v **Snowflake Schema jsou normalizované** (úspora místa).

![fact-dim-example](fact-dim-example.png)

## 3. Zálohování a archivace

### 3.1 Proč používáme archivaci dat a jaké typy souborových formátů jsou pro ni vhodné?

Archivace slouží k **dlouhodobému ukládání historických dat** (10+ let) pro účely **zpětného auditu** nebo **analýzy trendů**. Data jsou uložena na zabezpečeném serveru s předpokladem **nízké frekvence přístupu**.

Pro archivaci jsou ideální **jednoduché souborové formáty** a standardizované kódování:

* **CSV, SQL, JSON**
* **UTF-8** (případně Windows-1250)

### 3.2 Co je to diferenciální záloha a v čem je její výhoda oproti plné záloze?

#### Diferenciální záloha
**Diferenciální záloha** zálohuje pouze data změněná nebo přidaná **od poslední plné zálohy**.

#### Výhody oproti plné záloze
* **Šetří místo na disku**: Neukládá se znovu celý objem dat, pouze přírůstky.
* **Vyšší rychlost**: Proces zálohování trvá kratší dobu.
* **Efektivní obnova**: K obnově dat stačí pouze **poslední plná záloha a nejaktuálnější diferenciální záloha**.

### 3.3 K čemu se v databázi používá transakční log při výpadku systému?

Transakční log (Write-Ahead Log) je soubor, který obsahuje provedené příkazy, slouží k **zajištění integrity dat** po výpadku systému pomocí dvou mechanismů:
* **Redo (Znovudokončení):** Systém znovu aplikuje změny z **potvrzených transakcí (COMMIT)**, které se před pádem nestihly zapsat z paměti na disk.
* **Undo (Vracení zpět):** Systém **odstraní změny z neukončených transakcí**, které v momentě výpadku nebyly potvrzeny, a vrátí databázi do konzistentního stavu.

## 4. Vizualizace a Power BI

### 4.1 Popište hlavní funkcionalitu Power BI.

Power BI slouží k **transformaci dat do srozumitelné formy (storytelling)** pro efektivní rozhodování založené na faktech a identifikaci **klíčových indikátorů výkonnosti (KPI)**.

* **Model View:** Slouží k zobrazení **dimenzních (DIM) a faktových (FACT) tabulek** a k nastavení **vazeb (JOINů)** mezi nimi. Funguje na principu klasického **ER modelu**.

![model-view](model-view.png)

* **Power Query:** Modul určený pro **přímou editaci tabulek a čištění dat** v rámci procesu ELT/ETL.

![power-query](power-query.png)

* **DAX (Data Analysis Expressions):** Specializovaný jazyk pro tvorbu **pokročilých výpočtů a měření** v datových modelech.
* **Import dat:** Podporuje buď **klasický import** (např. nahrání CSV), nebo **Direct Query (Live connection)** pro přímé živé napojení na cloudové servery.
* **Dashboard:** Finální nástroj pro **vizualizaci dat** (grafy, mapy, tabulky), který pomáhá odhalovat trendy a vzory.

![dashboard](dashboard.png)

### 4.2 Popište proces čištění dat (Power Query) a uveďte 3 příklady transformací.

Hlavním účelem je **transformovat surová data do čisté, strukturované a normalizované podoby** pro analýzu.

* **Rozdělení dat a odstranění znaků:** Očištění dat a tvorba normalizovaných tabulek (např. rozdělení jedné tabulky na samostatné tabulky "autorů" a "knih").
* **Výpočet nových (kalkulovaných) atributů:** Vytváření nových údajů z původních dat (např. výpočet zisku nebo délky pobytu).
* **Zpracování chybějících hodnot:** Ošetření chyb v datech – při absenci povinných údajů se **data vrací zpět do zdroje s chybovou hláškou** (systém si nesmí data vymýšlet).

### 4.3 Uveďte 3 základní typy vizualizací a vysvětlete, jaký typ dat/analýzy na nich zobrazujeme.

* **Karta (Card)**: Zobrazuje **jedinou klíčovou hodnotu** (např. celkové tržby). Slouží pro okamžitý přehled o **hlavních ukazatelích výkonnosti (KPI)**.
* **Průřez (Slicer)**: Funguje jako **interaktivní filtr** přímo na ploše reportu. Umožňuje **dynamicky omezit data** podle dimenzí, jako je čas nebo kategorie.
* **Koláčový graf (Pie chart)**: Zobrazuje **procentuální podíl částí na celku**. Je vhodný pro vizualizaci **struktury a rozložení dat** u menšího počtu kategorií.
* **Sloupcový graf (Column chart)**: Slouží k **porovnání hodnot napříč různými kategoriemi**. Je ideální pro zobrazení **změn v čase** (např. tržby po měsících) nebo pro **srovnání velikosti** jednotlivých položek mezi sebou.