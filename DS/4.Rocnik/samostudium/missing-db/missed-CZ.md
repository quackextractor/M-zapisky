### **Částečně pokrytá témata**
Tato témata jsou zmíněna nebo částečně vysvětlena, ale chybí jim klíčové požadavky specifikované v seznamu ke zkoušce:
* **Relační databázové systémy:** Architektura klient-server a multitasking jsou dobře zdokumentovány. Nicméně srovnání mezi relačními a nerelačními (NoSQL) databázemi je omezeno na stručné zmínky, jako je výčet hierarchických/síťových typů a podpora JSON.
* **Modelování relační databáze:** Pokrývá obecné konceptuální versus relační modely, terminologii (entity, atributy, vztahy) a kardinalitu. **Zcela vynechává** požadované konvence ER diagramů specificky pro "Oracle DataModeler".
* **Export/Import dat z databáze:** Zmiňuje import souborů CSV do Power BI a utilitu `mysqldump` pro export struktury oproti datům. Chybí vyhrazený hlubší pohled do širších procesů migrace dat.
* **Bezpečnost databázového systému:** Vysvětluje příkazy DCL GRANT/DENY, role serveru versus databáze a základní rozdíl mezi správou rolí v MSSQL a účty v MySQL. Postrádá detailní prozkoumání autentizace versus autorizace.
* **Vnořené dotazy (Subqueries):** Základní vnořené dotazy jsou vysvětleny, včetně pořadí provádění a operátorů jako `=` a `<`. Chybí však pokročilé operátory (IN, EXISTS, ALL, ANY) a rozdíly mezi závislými (korelovanými) a nezávislými vnořenými dotazy.
* **Transakce a transakční zpracování:** Krátce zmiňuje vlastnosti ACID, základní příkazy TCL (COMMIT/ROLLBACK) a úrovně izolace. Chybí důkladné příklady nebo hluboká vysvětlení různých úrovní izolace.
* **Indexy (Indexes):** Dotýká se mezipaměti klíčů, B-stromů, primárních klíčů a omezení jedinečnosti. **Zcela opomíjí** požadované vysvětlení indexů CLUSTERED versus NONCLUSTERED.
* **Pokročilé modelování:** Vysvětluje "Self-Reference" jako vztah prvního stupně, ale zcela ignoruje strukturu "Arc".
* **SQL datové typy v různých databázových prostředích:** Zmiňuje obecné datové typy jako INT, VARCHAR, DATE a JSON, ale neposkytuje srovnání napříč různými databázovými prostředími.
* **Správa serveru Microsoft SQL Server & MySQL:** Zmiňuje SQL Server Management Studio (SSMS) a MySQL Daemon/architekturu, ale neposkytuje skutečné návody pro správu softwaru v SSMS nebo MySQL Workbench.
* **Business Intelligence:** BI je definováno obecně v kontextu datových skladů (Data Warehouses) a Power BI. Postrádá konkrétní požadovaná podtémata, jako je "evidence verzí, změn a historických záznamů" a strukturální/procedurální procesní logika.

### **Zcela chybějící témata**
V materiálech nejsou poskytnuty naprosto žádné informace pro tato zkušební témata:
* **Relační modely hierarchických struktur:** Žádné zmínky o vztazích Supertyp/Subtyp nebo jejich modelování v DataModeler a SQL implementacích.
* **Správa serveru Oracle:** Vůbec žádné zmínky o Oracle SQL Developer nebo administraci Oracle.