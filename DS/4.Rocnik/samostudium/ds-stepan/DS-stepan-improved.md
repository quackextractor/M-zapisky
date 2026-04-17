# Maturita 2026

**1 otázka na 1 minutu**

### Otázky z DS:

## 1. Relační databázové systémy

1. **Architektura klient-server**: Oddělení databázového serveru (backend) od klientské aplikace (frontend). `sqlcmd -S server`
2. **Databázový stroj (Engine)**: Jádro systému zodpovědné za ukládání, zpracování a zabezpečení dat. `services.msc`
3. **Komponenta Query Processor**: Přijímá SQL dotazy, analyzuje je a převádí na prováděcí plán. `- Optimalizace`
4. **Storage Manager**: Komponenta zajišťující nízkoúrovňový zápis dat na disk a správu bufferu. `- I/O operace`
5. **Multitasking**: Schopnost OS a DBS zpracovávat více požadavků (vláken) současně pomocí vícevláknového procesu. `SHOW PROCESSLIST`
6. **Relační DBS (RDBMS)**: Data organizovaná v tabulkách s definovanými vztahy pomocí klíčů. `SELECT * FROM tabulka`
7. **Nerelační DBS (NoSQL)**: Databáze typu Key-Value, dokumentové nebo grafové bez pevného schématu. `db.collection.find()`
8. **Schéma**: Logická struktura databáze, definující tabulky, sloupce a typy. `DESCRIBE table_name`
9. **Struktura ukládání**: Data jsou fyzicky uložena v datových souborech (např. .mdf, .ibd). `ls -lh /var/lib/mysql`
10. **Způsob ukládání (Row vs Column)**: RDBMS ukládají data po řádcích, analytické systémy často po sloupcích. `- OLTP vs OLAP`
11. **Konzistence**: Zajištění, že DB přejde z jednoho validního stavu do druhého. `- ACID`
12. **Izolace**: Schopnost DBS zajistit, aby se běžící transakce neovlivňovaly. `SET TRANSACTION ISOLATION LEVEL`
13. **Trvalost (Durability)**: Po potvrzení transakce jsou data trvale zapsána i při výpadku proudu. `- Transaction Log`
14. **Instance**: Běžící proces databázového serveru v operační paměti. `ps aux | grep mysqld`
15. **Databázový katalog**: Systémové tabulky obsahující metadata o všech objektech v DB. `SELECT * FROM information_schema.tables`

---

## 2. Modelování relační databáze

1. **Konceptuální model**: Abstraktní pohled na data, definuje entity a vztahy bez ohledu na technologii. `[ER Diagram]`
2. **Relační (logický) model**: Převod entit do tabulek, definice primárních a cizích klíčů. `[Schema]`
3. **Entita**: Objekt reálného světa (např. Zaměstnanec, Produkt), o kterém ukládáme data. `CREATE TABLE Entita`
4. **Atribut**: Vlastnost entity reprezentovaná sloupcem v tabulce. `ALTER TABLE t ADD sloupec INT`
5. **Vztah (Relationship)**: Logická vazba mezi entitami (1:1, 1:N, M:N). `- Kardinalita`
6. **Primární klíč (PK)**: Unikátní identifikátor řádku v tabulce, nesmí být NULL. `PRIMARY KEY (id)`
7. **Cizí klíč (FK)**: Odkaz na primární klíč jiné tabulky pro zajištění vazby. `FOREIGN KEY (id_ref) REFERENCES ...`
8. **Kardinalita**: Určuje počet výskytů entit ve vztahu (např. jeden autor - mnoho knih). `- 1:N`
9. **Optionalita**: Určuje, zda je účast entity ve vztahu povinná nebo volitelná. `NOT NULL / NULL`
10. **Vazební tabulka**: Nutná pro realizaci vztahu M:N, čímž dochází k jeho dekompozici na dva vztahy 1:N. `CREATE TABLE spojka (...)`
11. **Oracle DataModeler**: Nástroj pro vizuální návrh ER diagramů a generování SQL skriptů. `- CASE nástroj`
12. **Crow's Foot notace**: Grafický způsob znázornění kardinality vztahů (tzv. "vraní noha"). `[Grafika]`
13. **Identifikační vztah**: Vztah, kde PK dceřiné entity obsahuje PK rodičovské entity. `- Pevná vazba`
14. **Transformace**: Proces převodu logického modelu na fyzický (tabulky, indexy). `Engineer to Relational Model`
15. **Naming Conventions**: Pravidla pro pojmenovávání objektů (např. malá písmena, podtržítka). `tbl_zamestnanci_info`

---

## 3. Normalizace relační databáze

1. **Význam normalizace**: Proces minimalizace redundance (duplicity) dat a zajištění datové integrity. `- Clean Data`
2. **Redundance**: Nadbytečné opakování dat, které vede k problémům při aktualizaci. `- Update Anomaly`
3. **Anomálie vkládání**: Nemožnost vložit data, protože chybí jiná, nesouvisející data. `- Insert Anomaly`
4. **Anomálie mazání**: Nechtěná ztráta dat při smazání jiného záznamu. `- Delete Anomaly`
5. **První normální forma (1NF)**: Hodnoty v buňkách musí být atomické (nedělitelné), žádné duplicitní řádky. `- Atomicita`
6. **Druhá normální forma (2NF)**: Splňuje 1NF a všechny neklíčové atributy jsou plně závislé na celém PK. `- Částečná závislost`
7. **Třetí normální forma (3NF)**: Splňuje 2NF a neexistují tranzitivní závislosti (atributy závisí jen na PK). `- Tranzitivita`
8. **Boyce-Coddova NF (BCNF)**: Přísnější verze 3NF řešící problémy s více překrývajícími se kandidátními klíči. `- Strong 3NF`
9. **Dekompozice**: Rozdělení jedné široké tabulky do více menších s cílem splnit normální formy. `CREATE TABLE ... AS SELECT DISTINCT`
10. **Ukázka 1NF**: Rozdělení sloupce "Adresa" na "Ulice", "Město", "PSČ". `- Atomizace`
11. **Ukázka 2NF**: Vyčlenění údajů o výrobci z tabulky produktů do vlastní tabulky Výrobci. `- Vazba přes FK`
12. **Denormalizace**: Záměrné porušení pravidel normalizace za účelem zrychlení čtení dat. `- Výkon vs Čistota`
13. **Důvody denormalizace**: Snížení počtu JOINů u komplexních dotazů v datových skladech. `- Reportování`
14. **Cena za denormalizaci**: Zvýšené nároky na úložný prostor a riziko nekonzistence při zápisu. `- Storage cost`
15. **Funkční závislost**: Vztah, kdy hodnota jednoho atributu jednoznačně určuje hodnotu druhého. `X -> Y`

---

## 4. Integrita dat relační databáze

1. **Význam integrity**: Zajištění přesnosti, úplnosti a konzistence dat po celou dobu životnosti. `- Data Quality`
2. **Entitní integrita**: Každá tabulka musí mít primární klíč a ten nesmí být NULL. `PRIMARY KEY`
3. **Referenční integrita**: Cizí klíč musí vždy odkazovat na existující primární klíč nebo být NULL. `REFERENCES`
4. **Doménová integrita**: Definice přípustných hodnot pro daný sloupec (typ, rozsah, formát). `CHECK (plat > 0)`
5. **Uživatelská integrita**: Specifická pravidla definovaná triggerem nebo procedurou. `CREATE TRIGGER ...`
6. **NOT NULL**: Omezení, které zakazuje prázdnou hodnotu v daném sloupci. `ALTER TABLE t MODIFY c NOT NULL`
7. **UNIQUE**: Zajišťuje, že všechny hodnoty ve sloupci (nebo kombinaci) jsou unikátní. `CONSTRAINT uq_email UNIQUE(email)`
8. **CHECK Constraint**: Logický výraz, který musí každý řádek splňovat (např. věk > 18). `ADD CONSTRAINT chk_vek`
9. **DEFAULT**: Automatické dosazení hodnoty, pokud není při INSERTu zadána. `DEFAULT GETDATE()`
10. **ON DELETE CASCADE**: Při smazání rodiče se automaticky smažou i všichni potomci. `ON DELETE CASCADE`
11. **ON DELETE SET NULL**: Při smazání rodiče se hodnota cizího klíče u potomků změní na NULL. `ON DELETE SET NULL`
12. **ON UPDATE CASCADE**: Změna primárního klíče se promítne do všech navázaných cizích klíčů. `ON UPDATE CASCADE`
13. **Deklarativní integrita**: Integrita definovaná přímo v DDL schématu tabulky. `CONSTRAINT fk_...`
14. **Procedurální integrita**: Zajištění pravidel pomocí kódu (triggery, uložené procedury). `IF NOT EXISTS ...`
15. **Validace dat**: Proces kontroly integrity před samotným uložením do databáze. `- Data Validation`

---

## 5. Etapy vývoje databázových systémů

1. **Sběr požadavků**: Analýza potřeb uživatelů, definice procesů a datových entit. `- Analýza`
2. **Konceptuální návrh**: Tvorba vysokoúrovňového ER diagramu bez ohledu na konkrétní DB. `[ERD]`
3. **Logický návrh**: Mapování entit na tabulky a definice integritních omezení. `- Schema Design`
4. **Fyzický návrh**: Výběr datových typů, indexace, rozdělení na disky a nastavení HW. `- Implementation`
5. **Implementace**: Vlastní vytvoření databáze pomocí DDL skriptů na serveru. `CREATE DATABASE ...`
6. **Migrace dat**: Importování dat ze starých systémů nebo externích souborů do nové DB. `BULK INSERT`
7. **Testování**: Ověření funkčnosti, integrity, bezpečnosti a výkonu (Load testing). `- Quality Assurance`
8. **Nasazení (Deployment)**: Překlopení systému do produkčního prostředí. `GO LIVE`
9. **Provoz a údržba**: Monitoring výkonu, opravy chyb a pravidelné zálohování. `maintenance plans`
10. **Životní cyklus DB (DBLC)**: Neustálý proces od návrhu přes úpravy až po vyřazení (Decommissioning). `- Lifecycle`
11. **Technická dokumentace**: Popis struktury tabulek, relací a datových typů (Data Dictionary). `- Dokumentace`
12. **Uživatelská dokumentace**: Návody pro obsluhu aplikací nad databází. `- Manual`
13. **Dokumentace změn**: Vedení záznamů o všech úpravách schématu (Versioning). `Liquibase / Flyway`
14. **Optimalizace**: Ladění dotazů a indexů na základě reálného provozu. `SQL Profiler`
15. **Vyřazení (Archivace)**: Bezpečné odstranění databáze a archivace dat pro budoucí potřeby. `- Drop Database`

---

## 6. Úpravy a údržba dat v databázi

1. **Důvody údržby**: Změna business pravidel, oprava chyb nebo zvyšování výkonu. `- Maintenance`
2. **ETL (Extract, Transform, Load)**: Data se extrahují, upraví v mezivrstvě a pak vloží do cíle. `SSIS`
3. **ELT (Extract, Load, Transform)**: Data se vloží do cílové DB v surovém stavu a transformují se tam. `- Modern DWH`
4. **Transformace**: Čištění dat, agregace, spojování a změna formátů během přenosu. `CAST / CONVERT`
5. **Inkrementální plnění**: Nahrávání pouze nových nebo změněných záznamů (místo celé DB). `MERGE`
6. **Aktualizace statistik**: Pomáhá optimalizátoru dotazů volit nejlepší prováděcí plány. `UPDATE STATISTICS`
7. **Reorganizace indexů**: Odstranění fragmentace indexů bez jejich úplného přebudování. `ALTER INDEX REORGANIZE`
8. **Rebuild indexů**: Kompletní znovuvytvoření indexu pro maximální výkon. `ALTER INDEX REBUILD`
9. **Data Cleansing**: Identifikace a oprava neúplných nebo nesprávných záznamů. `DELETE WHERE ...`
10. **Monitoring volného prostoru**: Sledování velikosti datových souborů a logů. `DBCC SQLPERF(LOGSPACE)`
11. **Shrink databáze**: Zmenšení fyzických souborů DB (nedoporučuje se dělat často). `DBCC SHRINKDATABASE`
12. **Patching**: Pravidelná aktualizace samotného databázového engine (security záplaty). `- Update`
13. **Auditování**: Sledování, kdo a kdy měnil jaká data. `SELECT * FROM sys.fn_get_audit_file`
14. **Správa uživatelů**: Pravidelná revize přístupových práv a rolí. `REVOKE ...`
15. **Health Check**: Pravidelná kontrola konzistence databáze. `DBCC CHECKDB`

---

## 7. Zálohování a archivace dat

1. **Plná záloha (Full)**: Kompletní kopie celé databáze včetně všech objektů a dat. `BACKUP DATABASE ...`
2. **Diferenciální záloha**: Obsahuje pouze změny provedené od poslední plné zálohy. `WITH DIFFERENTIAL`
3. **Záloha transakčního logu**: Záloha všech operací, umožňuje obnovu k určitému času (PITR). `BACKUP LOG ...`
4. **Obnova dat (Restore)**: Proces nahrání zálohy zpět do databáze po havárii. `RESTORE DATABASE ...`
5. **Recovery Point Objective (RPO)**: Maximální přípustná ztráta dat měřená v čase. `- Business Goal`
6. **Recovery Time Objective (RTO)**: Maximální přípustný čas na obnovu systému do provozu. `- Business Goal`
7. **Záloha vs Archivace**: Záloha je pro obnovu při chybě, archivace je pro dlouhodobé uložení starých dat. `- Rozdíl`
8. **Archivační soubory**: Často formáty .bak, .sql, .csv nebo cloudová úložiště (S3 Glacier). `mysqldump`
9. **Off-site zálohování**: Ukládání kopií dat na fyzicky jiné místo (jiná budova, cloud). `- Bezpečí`
10. **Testování obnovy**: Pravidelné zkoušení, zda jsou zálohy čitelné a funkční. `- Kritický krok`
11. **Rotace záloh**: Pravidla pro mazání starých záloh (např. schéma GFS - Grandfather-Father-Son). `- Retence`
12. **Komprese záloh**: Snížení velikosti souborů zálohy pro úsporu místa. `WITH COMPRESSION`
13. **Šifrování záloh**: Ochrana obsahu zálohy heslem nebo certifikátem. `WITH ENCRYPTION`
14. **Studená záloha (Cold)**: Záloha prováděná při vypnuté databázi. `- Offline`
15. **Horká záloha (Hot)**: Záloha prováděná za plného provozu databáze. `- Online`

---

## 8. Export/Import dat z databáze

1. **Export dat**: Proces vytažení dat z DB do externího souboru (CSV, XML, JSON). `SELECT ... INTO OUTFILE`
2. **Import dat**: Nahrání dat z externího zdroje do tabulek DB. `LOAD DATA INFILE`
3. **Export struktury**: Vygenerování DDL skriptů (CREATE tabulky) bez samotných dat. `- Metadata export`
4. **Export struktury i dat**: Kompletní SQL dump umožňující rekonstrukci celé DB. `mysqldump --all-databases`
5. **BACPAC / DACPAC**: Formáty pro export schématu a dat v prostředí MS SQL Server. `- Visual Studio`
6. **Migrace dat**: Přenos dat mezi různými verzemi nebo typy serverů (např. Oracle do MSSQL). `- Migration`
7. **Mapping**: Definice, který sloupec ze zdroje patří do kterého sloupce v cíli. `- Mapování`
8. **Validace po importu**: Kontrola, zda se importovalo všech 100 % záznamů a jsou správně. `SELECT COUNT(*)`
9. **Bulk Insert**: Rychlé vkládání velkých objemů dat (tisíce až miliony řádků). `BULK INSERT MyTable FROM 'c:\\data.csv'`
10. **Oddělovače (Delimiters)**: Znaky určující konce polí a řádků v souborech (čárka, středník, tabulátor). `- CSV`
11. **Kódování (Encoding)**: Nutnost dodržet správné kódování (UTF-8) pro zachování diakritiky. `- UTF-8`
12. **Datové pumpy**: Specializované nástroje pro vysokorychlostní přenosy (Oracle Data Pump). `expdp / impdp`
13. **Transformace při importu**: Úprava formátů (např. data z MM/DD/YYYY na YYYY-MM-DD). `- Pre-processing`
14. **Dočasné tabulky (Staging)**: Místo, kam se data nahrají před finálním zpracováním. `CREATE TABLE #staging`
15. **Význam migrace**: Modernizace HW, konsolidace serverů nebo přechod do cloudu. `- Upgrade`

---

## 9. Architektura databázových systémů

1. **Fyzická struktura MySQL**: Dělí se na Base directory (spustitelné soubory) a Data directory (logy a data pro DB). `ls -lh /var/lib/mysql`
2. **Logická úroveň**: Jak uživatel vidí data (tabulky, pohledy, vztahy). `- Schema`
3. **Externí úroveň**: Uživatelské pohledy na data, omezené oprávněními. `- Views`
4. **Database Engine**: Hlavní služba zpracovávající požadavky. `sqlservr.exe`
5. **Buffer vs Cache**: Cache slouží pro načítání metadat a dotazů, Buffer obsluhuje fyzické datové bloky z disku. `- Memory`
6. **Transaction Log**: Soubor, kam se sekvenčně zapisují všechny změny (Write-Ahead Logging). `LDF soubor`
7. **Query Optimizer**: Komponenta, která hledá nejlevnější cestu k datům. `- Execution Plan`
8. **Lock Manager**: Spravuje zámky na tabulkách/řádcích pro zajištění izolace transakcí. `- Locking`
9. **Systémový katalog**: Metadata o všech objektech, uživatelích a právech. `sysobjects`
10. **Data Dictionary**: Slovník definující strukturu každého datového elementu. `- Metadata`
11. **Služba SQL Server Agent**: Plánovač úloh pro zálohy a údržbu. `msdb.dbo.sysjobs`
12. **Analysis Services (SSAS)**: Komponenta pro OLAP a datové sklady. `- Multidimenzionální data`
13. **Integration Services (SSIS)**: Nástroj pro ETL procesy a integraci dat. `- Data Flow`
14. **Reporting Services (SSRS)**: Nástroj pro tvorbu a publikaci reportů. `- Reporting`
15. **Síťový protokol**: Způsob komunikace (TCP/IP, Named Pipes, Shared Memory). `port 1433`

---

## 10. Bezpečnost databázového systému

1. **Autentizace**: Ověření identity uživatele (Windows Auth vs SQL Server Auth). `- Přihlášení`
2. **Autorizace**: Přidělení konkrétních práv přihlášenému uživateli. `GRANT SELECT ...`
3. **Serverové role**: Práva na úrovni celého serveru (např. sysadmin, backupoperator). `sysadmin`
4. **Databázové role**: Práva v rámci jedné DB (např. db_datareader, db_datawriter). `db_owner`
5. **Jazyk DCL (Data Control Language)**: Podmnožina SQL pro správu přístupových práv. `GRANT / REVOKE`
6. **Příkaz GRANT**: Udělení oprávnění uživateli nebo roli. `GRANT UPDATE ON tabulka TO uzivatel`
7. **Příkaz REVOKE**: Odebrání dříve uděleného oprávnění. `REVOKE INSERT ON tabulka FROM uzivatel`
8. **Příkaz DENY**: Explicitní zákaz oprávnění (má přednost před GRANT). `DENY DELETE TO uzivatel`
9. **Schéma (Schema-based security)**: Seskupení tabulek pod vlastníka, přidělování práv na celé schéma. `GRANT SELECT ON SCHEMA::dbo`
10. **SQL Injection**: Útok vložením škodlivého SQL kódu; obrana je parametrizace dotazů. `- Security Risk`
11. **Šifrování dat (TDE)**: Transparent Data Encryption - šifrování celé DB na disku. `- Encryption`
12. **Dynamic Data Masking**: Skrytí citlivých dat (např. čísla karet) pro uživatele bez oprávnění. `- Maskování`
13. **Audit Log**: Záznam o úspěšných i neúspěšných pokusech o přístup k datům. `sys.server_audits`
14. **MSSQL vs MySQL bezpečnost**: MSSQL má hlubší integraci s Active Directory, MySQL používá kombinaci 'user'@'host'. `- Porovnání`
15. **Princip nejnižších privilegií**: Uživatel by měl mít jen ta práva, která nezbytně potřebuje. `- Best Practice`

---

## 11. Jazyk SQL, DDL, DML příkazy

1. **DDL (Data Definition Language)**: Příkazy pro definici struktury (tabulky, indexy). `CREATE, ALTER, DROP`
2. **DML (Data Manipulation Language)**: Příkazy pro manipulaci s daty. `SELECT, INSERT, UPDATE, DELETE`
3. **CREATE TABLE**: Vytvoření nové tabulky s definicí sloupců a typů. `CREATE TABLE t (id INT)`
4. **ALTER TABLE**: Úprava existující tabulky (přidání sloupce, změna typu). `ALTER TABLE t ADD x VARCHAR(50)`
5. **TRUNCATE vs DELETE**: Truncate smaže vše rychle a bez logování řádků, Delete maže po jednom. `TRUNCATE TABLE t`
6. **SELECT**: Základní příkaz pro čtení dat z jedné nebo více tabulek. `SELECT * FROM tabulka`
7. **WHERE**: Klauzule pro filtrování řádků na základě podmínky. `WHERE cena > 100`
8. **GROUP BY**: Seskupení řádků se stejnými hodnotami pro agregační funkce. `GROUP BY kategorie`
9. **HAVING**: Podmínka pro filtrování skupin (používá se po GROUP BY). `HAVING COUNT(*) > 5`
10. **ORDER BY**: Seřazení výsledku (ASC - vzestupně, DESC - sestupně). `ORDER BY datum DESC`
11. **JOIN**: Spojení tabulek (INNER, LEFT, RIGHT, FULL). `SELECT * FROM A JOIN B ON A.id = B.id`
12. **Agregační funkce**: Výpočty nad množinou (SUM, AVG, MIN, MAX, COUNT). `SELECT SUM(plat)`
13. **INSERT INTO**: Vložení nového záznamu do tabulky. `INSERT INTO t (col) VALUES ('val')`
14. **UPDATE**: Změna existujících dat v tabulce. `UPDATE t SET col = 'val' WHERE id = 1`
15. **VIEW**: Uložený SELECT dotaz, který se chová jako virtuální tabulka. `CREATE VIEW v AS SELECT ...`

---

## 12. Vnořené dotazy

1. **Vnořený dotaz (Subquery)**: SELECT příkaz uvnitř jiného DML příkazu (SELECT, INSERT, UPDATE, DELETE). `(SELECT ...)`
2. **Nezávislý dotaz (Self-contained)**: Vnitřní dotaz lze spustit samostatně, provede se jen jednou. `WHERE id IN (SELECT ...)`
3. **Závislý dotaz (Correlated)**: Vnitřní dotaz odkazuje na sloupce z vnějšího dotazu, běží pro každý řádek. `WHERE EXISTS (SELECT ...)`
4. **Operátor IN**: Kontrola, zda se hodnota nachází v seznamu vráceném subquery. `WHERE id IN (1, 2, 3)`
5. **Operátor EXISTS**: Vrací TRUE, pokud subquery vrátí alespoň jeden řádek. `WHERE EXISTS (SELECT 1 FROM ...)`
6. **Operátor ALL**: Porovnání hodnoty se všemi hodnotami v seznamu (musí splnit pro všechny). `WHERE plat > ALL (SELECT ...)`
7. **Operátor ANY / SOME**: Porovnání hodnoty, stačí shoda s alespoň jednou hodnotou v seznamu. `WHERE plat > ANY (SELECT ...)`
8. **Skalární subquery**: Vrací právě jednu hodnotu (jeden řádek a jeden sloupec). `SELECT (SELECT MAX(plat) FROM ...)`
9. **Subquery ve FROM**: Použití výsledku dotazu jako dočasné tabulky (Derived Table). `FROM (SELECT ...) AS temp`
10. **Subquery v SELECT**: Používá se pro výpočet hodnoty pro každý řádek výsledku. `- Sloupcový subquery`
11. **Subquery v UPDATE**: Aktualizace dat na základě hodnot z jiné tabulky. `UPDATE t SET x = (SELECT ...)`
12. **Subquery v DELETE**: Smazání řádků, které splňují podmínku definovanou v jiném dotazu. `DELETE FROM t WHERE id NOT IN (...)`
13. **Limitace subquery**: Některé DB systémy mají omezený počet úrovní vnoření. `- Nesting limit`
14. **Subquery vs JOIN**: JOIN je často výkonnější pro velké objemy dat díky optimalizaci. `- Performance`
15. **Čitelnost**: Subquery mohou být čitelnější pro logiku typu "najdi vše, co není v...". `- Readable`

---

## 13. Transakce a transakční zpracování

1. **Definice transakce**: Logická jednotka práce, která musí být provedena celá nebo vůbec. `- Transaction`
2. **ACID - Atomicity**: "Vše nebo nic" - pokud jedna část selže, celá transakce se zruší. `ROLLBACK`
3. **ACID - Consistency**: Transakce převede DB z jednoho konzistentního stavu do druhého. `- Pravidla`
4. **ACID - Isolation**: Souběžně běžící transakce se vzájemně neovlivňují. `- Izolace`
5. **ACID - Durability**: Po COMMIT jsou změny trvale uloženy i při pádu systému. `- Trvalost`
6. **Příkaz BEGIN TRANSACTION**: Zahájení transakčního bloku. `BEGIN TRAN`
7. **Příkaz COMMIT**: Úspěšné ukončení a trvalé uložení změn. `COMMIT TRAN`
8. **Příkaz ROLLBACK**: Zrušení všech změn provedených v aktuální transakci. `ROLLBACK TRAN`
9. **Savepoint**: Bod uvnitř transakce, ke kterému se lze vrátit bez zrušení celé transakce. `SAVE TRANSACTION bod1`
10. **Úroveň Read Uncommitted**: Nejnižší izolace, dovoluje čtení nepotvrzených dat (Dirty Read). `SET ISOLATION LEVEL ...`
11. **Úroveň Read Committed**: Čte pouze potvrzená data (výchozí v MSSQL). `- Standard`
12. **Úroveň Repeatable Read**: Zaručuje, že opakované čtení stejných dat v transakci vrátí stejný výsledek. `- No non-repeatable read`
13. **Úroveň Serializable**: Nejpřísnější izolace, transakce se chovají, jako by běžely po sobě. `- No phantoms`
14. **Dirty Read**: Čtení dat, která jiná transakce změnila, ale ještě nepotvrdila (může je vzít zpět). `- Problém`
15. **Deadlock**: Situace, kdy dvě transakce čekají na zámky té druhé, systém musí jednu ukončit. `- Uváznutí`

---

## 14. Indexy

1. **Význam indexu**: Datová struktura (obvykle B-strom), která zrychluje vyhledávání dat. `- Speed`
2. **Vliv na výkon**: Zrychluje čtení (SELECT), ale zpomaluje zápis (INSERT, UPDATE, DELETE). `- Trade-off`
3. **Clustered Index**: Určuje fyzické pořadí dat na disku (v tabulce může být jen jeden, obvykle PK). `PRIMARY KEY`
4. **Non-Clustered Index**: Samostatná struktura s ukazateli na reálná data (může jich být mnoho). `CREATE INDEX`
5. **Unique Index**: Zajišťuje unikátnost hodnot ve sloupci, podobně jako UNIQUE constraint. `CREATE UNIQUE INDEX`
6. **Composite Index**: Index vytvořený nad více sloupci současně. `CREATE INDEX idx_jmeno_prijmeni ON t(prijmeni, jmeno)`
7. **Covering Index**: Index, který obsahuje všechny sloupce požadované dotazem (není třeba sahat do tabulky). `- Optimization`
8. **Full-Text Index**: Speciální index pro rychlé vyhledávání v dlouhých textech. `CONTAINS`
9. **Filtrovaný index**: Index vytvořený pouze nad částí dat splňujících podmínku (např. WHERE platba IS NULL). `WHERE ...`
10. **Fragmentace indexu**: Rozdrobení dat v indexu, které snižuje výkon; řeší se reorganizací. `- Fragmentation`
11. **Index Seek**: Efektivní operace, kdy SQL hledá konkrétní hodnotu v indexu. `- Fast`
12. **Index Scan**: Méně efektivní operace, kdy SQL musí projít celý index. `- Slower`
13. **Primary Key vs Unique Index**: PK automaticky vytváří unikátní index a nesmí být NULL. `- Klíče`
14. **Zahrnuté sloupce (Included columns)**: Sloupce přidané k listům non-clustered indexu pro lepší krytí dotazů. `INCLUDE (col)`
15. **Smazání indexu**: Pokud se index nepoužívá, je lepší ho smazat pro zrychlení zápisu. `DROP INDEX idx_name ON table`

---

## 15. Datové sklady

1. **Definice DWH**: Centralizované úložiště dat optimalizované pro analýzu a reportování. `- Data Warehouse`
2. **OLTP (Online Transaction Processing)**: Běžné provozní DB (mnoho malých transakcí, aktuální data). `- E-shop`
3. **OLAP (Online Analytical Processing)**: Analytické DB (komplexní dotazy, historická data). `- Reporty`
4. **Fakta (Facts)**: Kvantitativní údaje v DWH (např. cena, množství), uloženy ve faktových tabulkách. `- Metriky`
5. **Dimenze (Dimensions)**: Popisné atributy (např. čas, místo, produkt) pro filtrování faktů. `- Kontext`
6. **Schéma Star (Hvězda)**: Faktová tabulka uprostřed, přímo napojená na denormalizované dimenze. `- Jednoduchost`
7. **Schéma Snowflake (Vločka)**: Normalizované dimenze (dimenze odkazuje na další dimenzi). `- Úspora místa`
8. **Schéma Galaxy (Galaxie)**: Více faktových tabulek sdílejících společné dimenze (Conformed Dimensions). `- Fact Constellation`
9. **Staging Area**: Dočasné úložiště, kde se čistí data před vstupem do DWH. `- ETL Buffer`
10. **Granularita**: Úroveň detailu dat uložených ve faktové tabulce (např. prodej po dnech vs po sekundách). `- Detail`
11. **Surrogate a Natural Keys**: V OLAP se používají umělé náhradní klíče (Surrogate) místo přirozených (Natural) pro sjednocení. `- SK a NK`
12. **Historizace (SCD)**: Slowly Changing Dimensions - techniky pro sledování změn v dimenzích v čase. `- Historie`
13. **Agregace**: Předpočítané souhrny dat pro bleskové reportování. `SUM, GROUP BY`
14. **Metadata v DWH**: Informace o původu dat (lineage), transformacích a struktuře skladu. `- Katalog`
15. **Business Intelligence (BI)**: Nástroje pro analýzu dat z DWH (Power BI, Tableau). `- Vizualizace`

---

## 16. Vizualizace dat

1. **Princip vizualizace**: Převod číselných a textových dat do grafické podoby pro snadné pochopení. `- Insight`
2. **Power BI Desktop**: Hlavní nástroj pro tvorbu datových modelů a vizuálních reportů. `- Microsoft`
3. **Import dat**: Power BI podporuje SQL, Excel, Web, Azure a stovky dalších zdrojů. `Get Data`
4. **Power Query (M language)**: Nástroj pro transformaci, čištění a přípravu dat v Power BI. `- ETL`
5. **Datový model v Power BI**: Definice vztahů mezi tabulkami (schéma hvězda). `Manage Relationships`
6. **DAX (Data Analysis Expressions)**: Jazyk pro tvorbu výpočtů, měřítek a vypočtených sloupců. `Total Sales = SUM(...)`
7. **Měřítko (Measure)**: Dynamický výpočet, který se mění podle filtrů v reportu. `- Dynamic`
8. **Vizuály**: Jednotlivé grafy, mapy, tabulky a karty na stránce reportu. `- Grafy`
9. **Slicery**: Interaktivní filtry, které umožňují uživateli měnit zobrazená data (např. výběr roku). `- Filtry`
10. **Dashboard**: Přehled nejdůležitějších vizuálů z různých reportů na jedné stránce. `- Nástěnka`
11. **Drill-down**: Možnost jít z celkového pohledu (rok) do detailu (měsíc, den) kliknutím na graf. `- Detail`
12. **Publikování**: Nahrání reportu na Power BI Service pro sdílení s ostatními uživateli. `Publish`
13. **Gateway**: Služba pro automatickou aktualizaci dat z on-premise DB do cloudu. `- Refresh`
14. **Data Storytelling**: Schopnost sestavit report tak, aby logicky odpovídal na business otázky. `- Příběh`
15. **Rychlost odezvy**: Klíčový parametr; report musí reagovat na filtry okamžitě. `- Výkon`

---

## 17. Uložené procedury a funkce

1. **Uložená procedura (Stored Proc)**: Pojmenovaný blok SQL kódu uložený na serveru pro opakované použití. `CREATE PROCEDURE`
2. **Výhody procedur**: Snížení síťového provozu, vyšší bezpečnost, předkompilovaný plán. `- Efektivita`
3. **Parametry**: Vstupní (INPUT) pro předání dat a výstupní (OUTPUT) pro vrácení výsledků. `@param INT`
4. **Spuštění procedury**: Provádí se pomocí klíčového slova EXEC nebo EXECUTE. `EXEC sp_MojeProc 10`
5. **Úprava procedury**: Provádí se příkazem ALTER bez nutnosti mazat původní práva. `ALTER PROCEDURE`
6. **Uživatelská funkce (UDF)**: Vrací buď skalární hodnotu, nebo tabulku. `CREATE FUNCTION`
7. **Skalární funkce**: Vrací právě jednu hodnotu (např. výpočet DPH). `RETURNS INT`
8. **Tabulková funkce (TVF)**: Vrací množinu řádků (v MSSQL/PostgreSQL); MySQL toto přímo nepodporuje a využívá pohledy. `RETURNS TABLE`
9. **Rozdíl Procedura vs Funkce**: Procedura se volá pomocí EXEC, funkce přímo v SELECTu. `- Rozdíl`
10. **Omezení funkcí**: Funkce nesmí měnit stav databáze (např. volat INSERT/UPDATE). `- Side effects`
11. **Systémové funkce**: Vestavěné funkce serveru (např. GETDATE(), LEN(), ISNULL()). `SELECT GETDATE()`
12. **Parametr DEFAULT**: Možnost definovat výchozí hodnotu parametru, pokud není zadán. `@id INT = 0`
13. **Návratová hodnota (RETURN)**: Procedura může vrátit celočíselný status (obvykle 0 pro úspěch). `RETURN 0`
14. **Zabezpečení**: Uživatel může mít právo spustit proceduru, aniž by měl přístup k tabulkám. `GRANT EXECUTE`
15. **Smazání**: Odstranění procedury/funkce ze serveru. `DROP PROCEDURE proc_name`

---

## 18. Triggery (Spouště)

1. **Definice triggeru**: Speciální typ uložené procedury, která se spustí automaticky při DML akci. `CREATE TRIGGER`
2. **Typy triggerů**: DML triggery (INSERT, UPDATE, DELETE) a DDL triggery (CREATE TABLE...). `- Typy`
3. **AFTER Trigger**: Spustí se až po úspěšném provedení akce a kontrole integrity. `AFTER INSERT`
4. **INSTEAD OF Trigger**: Spustí se místo původní akce (často pro pohledy). `INSTEAD OF UPDATE`
5. **Dočasné tabulky/proměnné**: INSERTED/DELETED v MSSQL a NEW/OLD v MySQL pro nová a stará data. `NEW.sloupec`
6. **Využití triggerů**: Auditování změn, složité integritní kontroly, automatické výpočty. `- Audit`
7. **Rekurzivní trigger**: Situace, kdy trigger vyvolá akci, která spustí ten samý trigger znovu. `- Pozor`
8. **Aktualizace (UPDATE())**: Funkce v triggeru zjišťující, zda byl změněn konkrétní sloupec. `IF UPDATE(sloupec)`
9. **Výkon**: Triggery mohou výrazně zpomalit hromadné operace, protože běží nad každou dávkou. `- Performance`
10. **Zakázání triggeru**: Možnost dočasně vypnout trigger bez jeho smazání. `DISABLE TRIGGER trg_name ON tabulka`
11. **Povolení triggeru**: Opětovná aktivace vypnutého triggeru. `ENABLE TRIGGER trg_name ON tabulka`
12. **Úprava triggeru**: Změna logiky pomocí ALTER. `ALTER TRIGGER trg_name ...`
13. **Smazání triggeru**: Odstranění spouště. `DROP TRIGGER trg_name`
14. **Multi-row operace**: Trigger musí být napsán tak, aby zvládl zpracovat více řádků najednou v inserted/deleted. `- Best Practice`
15. **Kaskádové operace**: Automatické změny v jiných tabulkách vyvolané triggerem. `- Cascade`

---

## 19. Pokročilé modelování

1. **Self-Reference**: Vztah tabulky k sobě samé (např. Zaměstnanec má nadřízeného, který je také Zaměstnanec). `FK k téže tabulce`
2. **Implementace Self-Ref**: Sloupec ManagerID odkazuje na EmployeeID ve stejné tabulce. `REFERENCES Zamestnanci(ID)`
3. **Hierarchie**: Self-reference umožňuje vytvářet stromové struktury (organizační grafy). `- Strom`
4. **Arc (Oblouk)**: Exkluzivní vztah, kde entita může být navázána právě na jednu z několika jiných entit. `- Exclusive OR`
5. **Implementace Arc**: Pomocí sady cizích klíčů, kde vždy právě jeden musí být NOT NULL (řešeno CHECKem). `CHECK (Klic1 IS NOT NULL OR Klic2 IS NOT NULL)`
6. **Supertype**: Obecná entita obsahující společné atributy (např. Osoba). `- Rodič`
7. **Subtype**: Specifická entita dědící od supertypu (např. Student, Učitel). `- Potomek`
8. **Generalizace**: Proces hledání společných prvků a tvorba supertypu. `- Top-down`
9. **Specializace**: Rozdělení supertypu na detailnější subtypy. `- Bottom-up`
10. **Diskriminátor**: Sloupec v supertypu, který určuje, o jaký subtype se jedná. `typ_osoby CHAR(1)`
11. **Subtype Cluster**: Skupina subtypů patřících k jednomu supertypu. `- Seskupení`
12. **Exkluzivní subtypy**: Instance může být právě jedním subtypem (buď muž, nebo žena). `- XOR`
13. **Inkluzivní subtypy**: Instance může být více subtypy zároveň (např. student i zaměstnanec). `- AND`
14. **Implementace 1:1**: Každý subtype má svou tabulku, PK je zároveň FK do tabulky supertypu. `- Mnoho tabulek`
15. **Implementace "Jedna tabulka"**: Všechny atributy v jedné tabulce (hodně NULL hodnot). `- Jedna tabulka`

---

## 20. Business Intelligence

1. **Strukturální část BI**: Datové sklady, ETL procesy a datové modely. `- Data Architecture`
2. **Procedurální část BI**: Reportování, dolování dat (Data Mining) a vizualizace. `- Analytics`
3. **Význam BI**: Podpora strategického rozhodování na základě reálných faktů, ne pocitů. `- Decision Support`
4. **Analýza zadání**: Rozdělení na datový model (co ukládáme) a procesní logiku (co s tím děláme). `- Analýza`
5. **Evidence verzí**: Ukládání změn objektů v čase pomocí verzování. `verze_id INT`
6. **Historické záznamy**: Uchovávání smazaných nebo starých dat pro potřeby auditu. `platnost_od, platnost_do`
7. **Sledování změn (Change Tracking)**: Lehký mechanismus pro identifikaci změněných řádků. `- Monitoring`
8. **Relační modely historie**: Tabulka pro aktuální data + stínová tabulka pro historické záznamy. `- Shadow tables`
9. **Temporal Tables**: Systémem řízené tabulky historie v MSSQL. `PERIOD FOR SYSTEM_TIME`
10. **Klíčové ukazatele (KPI)**: Měřitelné hodnoty ukazující úspěšnost businessu. `- KPI`
11. **Datové kostky**: Multidimenzionální datové struktury pro rychlou analýzu. `- Cubes`
12. **Data Mining**: Hledání skrytých vzorů a korelací ve velkých datech. `- Vzorce`
13. **Prediktivní analýza**: Předpovídání budoucích trendů na základě historických dat. `- Forecast`
14. **Self-Service BI**: Umožnění běžným uživatelům tvořit vlastní reporty bez IT. `- Power BI`
15. **Datová kvalita**: Klíčový předpoklad; špatná data vedou k chybným rozhodnutím (GIGO - Garbage In, Garbage Out). `- Quality`

---

## 21. Relační modely hierarchických struktur

1. **Hierarchie**: Uspořádání dat, kde prvky jsou podřízeny jiným (nadřízený-podřízený). `- Strom`
2. **Supertype/Subtype v DataModeleru**: Modeluje se pomocí entity, která má uvnitř vnořené subentity. `- Design`
3. **Transformace Hierarchie**: Převod logického modelu na fyzické tabulky (jedna tabulka vs. tabulka pro každou entitu). `- Physical`
4. **Table-per-Hierarchy (TPH)**: Celá hierarchie v jedné tabulce s diskriminátorem. `- 1 Table`
5. **Table-per-Type (TPT)**: Každý typ má svou tabulku spojenou vazbou 1:1 k rodiči. `- Normalized`
6. **Recursive JOIN**: SQL dotaz pro procházení hierarchií (spojení tabulky se sebou samou). `JOIN t t2 ON t.id = t2.parent_id`
7. **CTE (Common Table Expressions)**: Rekurzivní dotazy pro procházení stromových struktur. `WITH r_cte AS (...)`
8. **HierarchyID**: Speciální datový typ v MSSQL pro efektivní správu stromových struktur. `HIERARCHYID`
9. **Kořenový prvek (Root)**: Prvek na vrcholu hierarchie (nemá rodiče). `WHERE parent_id IS NULL`
10. **Listový prvek (Leaf)**: Prvek na konci větve (nemá potomky). `- Konec`
11. **Hloubka hierarchie**: Počet úrovní od kořene k listu. `- Depth`
12. **Ancestors**: Všichni předci daného prvku v hierarchii. `- Předci`
13. **Descendants**: Všichni potomci daného prvku. `- Potomci`
14. **Traverzování**: Proces procházení stromu (do hloubky vs do šířky). `- Procházení`
15. **Udržování integrity**: Zajištění, aby v hierarchii nevznikl cyklus (A je rodič B a B je rodič A). `- No cycles`

---

## 22. Správa serverů a nástroje

1. **SQL Server Management Studio (SSMS)**: Hlavní GUI pro správu Microsoft SQL Serveru. `- MSSQL`
2. **Object Explorer**: Stromová struktura v SSMS pro přístup k tabulkám, procedurám a bezpečnosti. `- GUI`
3. **Query Window**: Okno pro psaní a spouštění T-SQL dotazů v SSMS. `F5`
4. **SQL Server Profiler**: Nástroj pro sledování a ladění aktivity na serveru. `- Debug`
5. **Oracle SQL Developer**: Zdarma dostupný grafický nástroj pro správu Oracle Database. `- Oracle`
6. **Connections**: Správa připojení k různým Oracle instancím pomocí TNS nebo EZConnect. `- Link`
7. **Worksheet**: Prostředí pro psaní SQL a PL/SQL v SQL Developeru. `- SQL`
8. **MySQL Workbench**: Vizuální nástroj pro návrh, vývoj a správu MySQL/MariaDB. `- MySQL`
9. **Server Administration**: Modul ve Workbench pro start/stop serveru a kontrolu logů. `- Admin`
10. **Data Modeling Tool**: Vestavěný ER diagrammer v MySQL Workbench. `- Modeling`
11. **Příkazová řádka (CLI)**: Správa serverů přes textové konzole (sqlcmd, sqlplus, mysql). `mysql -u root -p`
12. **Porty**: Standardní porty: MSSQL (1433), MySQL (3306), Oracle (1521). `- Networking`
13. **Logy serveru**: Sledování chybových logů pro diagnostiku problémů se startem. `- Error Log`
14. **Resource Governor**: Nástroj v MSSQL pro omezení CPU a RAM pro konkrétní uživatele. `- Quota`
15. **Instance Configuration**: Nastavení paměti, kolace (jazyka) a paralelismu serveru. `sp_configure`

---

## 23. SQL Datové typy

1. **INT (Integer)**: Celá čísla (obvykle 4 bajty). `id INT`
2. **VARCHAR / NVARCHAR**: Proměnlivá délka textu (N značí podporu Unicode - diakritiky). `jmeno NVARCHAR(50)`
3. **CHAR**: Pevná délka textu (doplňuje se mezerami). `kod CHAR(3)`
4. **DECIMAL / NUMERIC**: Přesná čísla s plovoucí čárkou (vhodné pro peníze). `cena DECIMAL(10, 2)`
5. **FLOAT / REAL**: Přibližná čísla pro vědecké výpočty. `pi FLOAT`
6. **DATE**: Uloží pouze datum (RRRR-MM-DD). `narozeni DATE`
7. **DATETIME / TIMESTAMP**: Uloží datum i čas. `vytvoreno DATETIME`
8. **BOOLEAN / BIT**: Logická hodnota (Pravda/Nepravda). `je_aktivni BIT`
9. **BLOB / VARBINARY(MAX)**: Velké binární objekty (obrázky, soubory). `obrazek VARBINARY(MAX)`
10. **CLOB / TEXT**: Velké textové bloky (dlouhé popisy). `poznamka TEXT`
11. **UUID / GUID**: Unikátní identifikátor (36 znaků). `uid UNIQUEIDENTIFIER`
12. **ENUM**: Výčtový typ (pouze v MySQL) - výběr z pevného seznamu. `barva ENUM('cervena', 'modra')`
13. **JSON**: Speciální typ pro ukládání strukturovaných dokumentů (moderní SQL). `data JSON`
14. **Money**: Specifický typ pro měnu v MSSQL. `plat MONEY`
15. **Přelévání typů (Casting)**: Převod mezi typy pomocí funkcí. `CAST(sloupec AS VARCHAR)`

---

## 24. Správa serveru MySQL

1. **MySQL Workbench Connections**: Nastavení připojení k serveru pomocí parametrů Hostname, Port a Username. `Port 3306`
2. **SQL Editor**: Hlavní pracovní okno pro psaní dotazů, zvýraznění syntaxe a prohlížení výsledků. `Ctrl+Enter`
3. **Administration Tab**: Modul pro monitorování stavu serveru (Server Status) a správu běžících spojení. `Client Connections`
4. **Data Export/Import**: Nástroj pro vytváření a obnovu dump souborů celé databáze nebo tabulek. `mysqldump`
5. **Startup / Shutdown**: Funkce pro bezpečné spuštění nebo zastavení databázové služby mysqld z GUI. `Stop Server`
6. **Users and Privileges**: Grafické rozhraní pro správu uživatelských účtů a přidělování práv na objekty. `Add Account`
7. **Schema Inspector**: Nástroj pro detailní analýzu struktury tabulek, indexů a využití místa na disku. `- Maintenance`
8. **Visual Design (EER)**: Tvorba a úprava datových modelů (Enhanced Entity-Relationship) s možností synchronizace. `Ctrl+M`
9. **Forward Engineering**: Automatické vygenerování SQL skriptů na základě vytvořeného vizuálního modelu. `Database -> Forward Engineer`
10. **Reverse Engineering**: Vytvoření vizuálního ER diagramu z již existující fyzické databáze. `Database -> Reverse Engineer`
11. **Server Logs**: Přístup k logům (Error log, General log) přímo z prostředí Workbench pro diagnostiku. `- Diagnostic`
12. **Performance Dashboard**: Grafické znázornění vytížení CPU, sítě a diskových operací v reálném čase. `- Monitoring`
13. **SQL Snippets**: Ukládání a správa často používaných úseků kódu pro zrychlení vývoje. `- Snippets`
14. **Table Editor**: Vizuální editor pro změnu struktury tabulek (ALTER) bez nutnosti psát ručně SQL kód. `Right-click -> Alter Table`
15. **Query Optimizer Visualizer**: Zobrazení vysvětlení (EXPLAIN) dotazu v grafické podobě pro ladění výkonu. `EXPLAIN format=json`

---

## 25. SQL datové typy v různých prostředích

1. **VARCHAR2**: Datový typ v Oracle DB; na rozdíl od standardního VARCHAR lépe optimalizuje místo. `VARCHAR2(50)`
2. **NUMBER**: Univerzální číselný typ v Oracle (místo INT/DECIMAL); umožňuje definovat přesnost i měřítko. `NUMBER(10,2)`
3. **SERIAL**: Datový typ v PostgreSQL pro automaticky se zvyšující celočíselný identifikátor. `id SERIAL`
4. **IDENTITY**: Vlastnost sloupce v MSSQL (obdoba AUTO_INCREMENT v MySQL) pro generování unikátních klíčů. `ID INT IDENTITY(1,1)`
5. **BIT**: Logický typ v MSSQL (0 nebo 1); v MySQL je BOOLEAN pouze synonymem pro TINYINT(1). `is_active BIT`
6. **UNIQUEIDENTIFIER**: Datový typ v MSSQL pro GUID; v MySQL se UUID ukládá jako BINARY(16) nebo VARCHAR. `NEWID()`
7. **BFILE**: Datový typ v Oracle pro ukládání odkazů na soubory uložené mimo databázi v OS. `BFILE`
8. **AUTO_INCREMENT**: Vlastnost v MySQL zajišťující automatické číslování PK; u Oracle dříve přes SEQUENCE. `id INT AUTO_INCREMENT`
9. **DATE Formáty**: V MySQL standardně RRRR-MM-DD; v Oracle závisí na nastavení NLS_DATE_FORMAT. `YYYY-MM-DD`
10. **TEXT vs VARCHAR(MAX)**: MySQL používá TEXT/LONGTEXT; MSSQL preferuje VARCHAR(MAX) pro neomezený text. `VARCHAR(MAX)`
11. **MONEY**: Specifický typ pro měnu v MSSQL; v MySQL se doporučuje DECIMAL pro zachování přesnosti. `plat MONEY`
12. **NVARCHAR**: Unicode text v MSSQL/MySQL; v Oracle je ekvivalentem NCHAR/NVARCHAR2. `NVARCHAR(100)`
13. **TINYINT**: Malé celé číslo v MySQL (1 bajt); v MSSQL se pro stejný účel často používá SMALLINT (2 bajty). `TINYINT UNSIGNED`
14. **JSON Support**: MySQL má nativní typ JSON s validací; MSSQL používá NVARCHAR s JSON funkcemi. `data JSON`
15. **Type Compatibility**: Při migraci je nutné mapovat typy (např. Oracle NUMBER(10) na MySQL INT). `- Migrace`