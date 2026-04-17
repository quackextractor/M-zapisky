### **Partially Covered Topics**
These topics are mentioned or partially explained, but are missing key requirements specified in the exam list:
 * **Relační databázové systémy:** The client-server architecture and multitasking are well documented. However, the comparison between relational and non-relational (NoSQL) databases is limited to brief mentions, such as listing hierarchical/network types and JSON support.
* **Modelování relační databáze:** Covers general conceptual vs. relational models, terminology (entities, attributes, relationships), and cardinality. It **completely misses** the required ER diagram conventions specifically for "Oracle DataModeler".
* **Export/Import dat z databáze:** Mentions importing CSVs into Power BI and the `mysqldump` utility for exporting structure vs. data. It lacks a dedicated deep dive into broader data migration processes.
* **Bezpečnost databázového systému:** Explains GRANT/DENY DCL commands, server vs. database roles, and the basic difference between MSSQL role management and MySQL accounts. It lacks a detailed exploration of authentication versus authorization.
* **Vnořené dotazy (Subqueries):** Basic subselects are explained, including execution order and operators like `=` and `<`. However, advanced operators (IN, EXISTS, ALL, ANY) and the differences between dependent (correlated) and independent subqueries are missing.
* **Transakce a transakční zpracování:** Briefly notes ACID properties, basic TCL commands (COMMIT/ROLLBACK), and isolation levels. It lacks thorough examples or deep explanations of varying isolation levels.
* **Indexy (Indexes):** Touches upon key caches, B-trees, primary keys, and unique constraints. It **totally misses** the required explanation of CLUSTERED vs. NONCLUSTERED indexes.
* **Pokročilé modelování:** Explains "Self-Reference" as a degree-1 relationship, but completely ignores the "Arc" structure.
* **SQL datové typy v různých databázových prostředích:** Mentions generic datatypes like INT, VARCHAR, DATE, and JSON, but fails to provide a comparison across different database environments.
* **Správa serveru Microsoft SQL Server & MySQL:** Mentions SQL Server Management Studio (SSMS) and MySQL Daemon/architecture, but does not provide actual software management guides for SSMS or MySQL Workbench.
* **Business Intelligence:** BI is defined generally in the context of Data Warehouses and Power BI. It lacks the specific sub-topics requested, such as "evidence verzí, změn a historických záznamů" (versioning and historical record modeling) and structural/procedural process logic.

### **Totally Missing Topics**
There is absolutely no information provided in the sources for these exam topics:
 * **Relační modely hierarchických struktur:** No mentions of Supertype/Subtype relationships or their modeling in DataModeler and SQL implementations.
* **Správa serveru Oracle:** No mentions of Oracle SQL Developer or Oracle administration whatsoever.