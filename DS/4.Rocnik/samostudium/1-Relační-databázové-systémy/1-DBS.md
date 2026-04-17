# Teoretický list: Relační databázové systémy

### 1. Relační databázové systémy a jejich základy

### 2. Architektura Klient-Server
V současnosti se u relačních databázových systémů používá primárně architektura klient-server. Účelem této architektury je oddělení databázových služeb od klientských aplikací.
* **Klient:** Je to aplikace, pomocí které se uživatel připojuje k serveru a posílá požadavky ve formě SQL dotazů. Klientem může být program v C#, Javě, webová stránka, management studio nebo příkazový řádek. Klient nemá nikdy přímý přístup k fyzickým datům na serveru.
* **Server:** Představuje databázovou instanci, kde jsou fyzicky uložena data. Server přijme požadavky od klienta, zpracuje je a klientovi vrátí pouze hotový výsledek. Veškerá data zůstávají uložena v bezpečí na serveru. Management studio tvoří rozhraní pro přístup, hlídá práva a zabezpečuje databázi.

### 3. Komponenty databázového systému a jejich činnost (na příkladu MySQL)
Databázový server se skládá z fyzické struktury (základní a datový adresář) a logické struktury procesů. Logické bloky zpracovávají SQL dotazy následovně:
 * **mysqld (daemon):** Hlavní vícevláknový proces (program) běžící na pozadí, který spravuje všechny příchozí a odchozí požadavky klientů.
* **Parser (analyzátor):** Program, který kontroluje správnost syntaxe SQL příkazů a ověřuje uživatelská oprávnění k datům.
* **Optimizer:** Modul, který připraví a následně provede prováděcí plán přístupu na konkrétní oblast na disku (Storage Engine), čímž optimalizuje pomalou práci s diskem.
* **Paměť (Cache):** Pro urychlení práce systém využívá Query Cache (paměť pro předchozí provedené příkazy), Metadata Cache (paměť pro statistiky, struktury a přístupová práva) a Key Cache (paměť pro vyhledávací B-stromy a indexy).
* **Storage Engines (Úložiště):** Oblasti na disku spravující fyzické soubory. Zodpovídají za načítání a ukládání dat. Příkladem je transakční "InnoDB" využívající zamykání na úrovni řádků nebo netransakční "MyISAM" určený pro velmi rychlé čtení velkých objemů dat.

### 4. Multitasking a transakční zpracování
Aby mohla databáze plynule obsluhovat mnoho klientů najednou, využívá multitaskingový přístup a řídí souběžné transakce.
* Proces `mysqld` je vícevláknový, což mu umožňuje pracovat s požadavky souběžně.
* Doba od úspěšného připojení klienta až po jeho odpojení se nazývá session. Po celou tuto dobu má dané připojení přiděleno své unikátní `thread_id`.
* Systém musí při multitaskingu zajistit vlastnosti ACID (Atomicity, Consistency, Isolation, Durability) a řídit úrovně izolace transakcí.

### 5. Rozdíl mezi relačním a nerelačním DBS, struktura a ukládání
Základní srovnání spočívá v odlišném způsobu definice struktury a ukládání informací.
* **Relační DBS:** Ukládá data do pevně dané struktury tabulek, které jsou navzájem logicky propojeny vazbami přes primární a cizí klíče. Využívá normalizaci k odstranění redundancí a klade důraz na integritní omezení a konzistenci.
* **Nerelační (NoSQL) DBS:** Nabízí variabilnější strukturu a různé způsoby uložení dat, které nevyužívají standardní tabulky a vazby. Systémy jako MySQL jsou sice primárně relační, ale dokáží spravovat i data v nerelačních formátech, například NoSQL formát JSON nebo uložení ve formátu CSV.
* Různé typy nerelačních struktur zmiňovaných pro uchování dat zahrnují: Flat databáze (založené na plochých CSV souborech), Síťové databáze (data uspořádaná jako uzly grafu), Hierarchické databáze (data uspořádaná do stromové struktury) a Objektové databáze (data ukládána jako objekty se svými vlastnostmi).

********************************************************************************

# Cvičení k maturitní otázce

Vypracujte odpovědi na následující otázky. Pokud si nejste jisti, vraťte se k teoretickému listu výše.

**1. Analýza architektury Klient-Server**
Vysvětlete na jakém principu funguje architektura klient-server v kontextu databází. Z jakého důvodu je výhodné, že klient odesílá pouze SQL dotazy a nemá k dispozici přímý přístup k datovým souborům uloženým na pevném disku?

**2. Životní cyklus SQL dotazu**
Klient napíše příkaz `SELECT * FROM zamestnanci` a stiskne tlačítko pro spuštění. Popište chronologicky, přes které logické moduly a paměti uvnitř databázového serveru tento dotaz projde (od kontroly až po fyzické načtení z disku). Zahrňte do odpovědi pojmy: Parser, Query Cache, Optimizer a Storage Engine.

**3. Multitasking a session**
Jakým způsobem databázový server MySQL řeší situaci, kdy se na něj současně připojí stovka různých uživatelů? Vysvětlete pojmy "vícevláknový proces" (daemon), "session" a "thread_id".

**4. Rozdělení databázových systémů**
Uveďte hlavní rozdíl ve struktuře ukládání dat mezi klasickou relační databází a nerelačními systémy. Jmenujte alespoň 3 typy nerelačních (nebo historických) architektur ukládání dat a stručně popište jejich logické uspořádání.

**5. Úloha paměti v DBS**
Práce s pevným diskem je v databázích vždy ta nejpomalejší operace. Vysvětlete, jaké tři konkrétní mezipaměti (Cache) používá logická architektura k urychlení své činnosti a co přesně se v každé z nich ukládá. Který modul rozhoduje o tom, jak se k datům na disku bude přistupovat?

********************************************************************************

# Řešení cvičení

**1. Analýza architektury Klient-Server** Architektura klient-server odděluje klientské aplikace od samotných databázových služeb. Klient (například webová stránka nebo program) pouze odesílá požadavky ve formě SQL dotazů. Server tyto požadavky přijme, zpracuje a vrátí klientovi hotová data. Výhodou absence přímého přístupu klienta k fyzickým datovým souborům je především bezpečnost a ochrana datové integrity. Veškerá data zůstávají na serveru, což zabraňuje jejich neoprávněné manipulaci nebo poškození ze strany klienta.

**2. Životní cyklus SQL dotazu**
Proces zpracování dotazu probíhá v následujících krocích:
1. **Parser (analyzátor)** zkontroluje správnost syntaxe SQL příkazu a ověří, zda má uživatel příslušná oprávnění k datům. Následně dotazu vygeneruje jedinečné `sql_id`.
2. Systém zkontroluje paměť **Query Cache**. Pokud se v ní nachází již předpřipravený výsledek z předchozího volání, ihned jej vrátí.
3. Pokud dotaz v mezipaměti není, vstupuje do hry **Optimizer**. Ten sestaví optimální prováděcí plán (execution plan) pro přístup na disk, aby byla operace co nejrychlejší.
4. **Storage Engine** (například InnoDB) na základě tohoto plánu provede fyzické načtení požadovaných dat z disku a vrátí je klientovi.

**3. Multitasking a session** MySQL využívá pro zpracování požadavků proces `mysqld` (takzvaný daemon), který je vícevláknový (multithreadový). To znamená, že dokáže obsluhovat mnoho klientů současně. Doba od úspěšného připojení klienta až po jeho odpojení se označuje jako **session**. Po celou tuto dobu má dané připojení přidělen svůj unikátní identifikátor, který se nazývá **thread_id**.

**4. Rozdělení databázových systémů** Hlavní rozdíl spočívá v tom, že relační databáze ukládají data do pevně dané struktury tabulek, které jsou logicky propojeny vazbami pomocí primárních a cizích klíčů. Nerelační databáze (NoSQL) naproti tomu nabízejí variabilnější strukturu a nevyužívají standardní tabulky a vazby.
Příklady nerelačních architektur:
 * **Flat databáze:** Data jsou ukládána do plochých souborů, například ve formátu CSV.
* **Hierarchická databáze:** Uspořádání dat připomíná stromovou strukturu s rodičovskými a dceřinými uzly.
* **Síťová databáze:** Data jsou uspořádaná jako uzly grafu, což umožňuje složitější propojení než hierarchický model.
* **Objektová databáze:** Data jsou ukládána jako objekty se svými vlastnostmi.

**5. Úloha paměti v DBS**
Logická architektura využívá k urychlení práce následující tři mezipaměti:
 * **Query Cache:** Uchovává předchozí, již zkontrolované a provedené SQL příkazy (předpřipravená data).
* **Metadata Cache:** Slouží k uložení metadat, jako jsou názvy tabulek, struktury, statistiky a uživatelská oprávnění.
* **Key Cache:** Obsahuje indexy (například vyhledávací B-stromy) ke zpracovávaným tabulkám pro rychlejší vyhledávání. Modul, který rozhoduje o tom, jak se bude přistupovat k datům na disku, se nazývá **Optimizer**. Sestavuje takzvaný prováděcí plán pro Storage Engine.