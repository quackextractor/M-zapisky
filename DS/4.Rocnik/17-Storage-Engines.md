
# Storage Engines

- oblasti na disku vymezené pro uložení dat různého typu (MySQL je multiplatformní - může ukládat i NoSQL data = např.. JSON)
=> spravuji fyzická data (file managment)
- software pro storage engine je zodpovědný za provedeni SQL příkazů pro načítaní a ukládaní dat

Př. 1: Inno DB
- pouzivani transakce a ACID pri nacitani a ukladani dat
- logicka struktura objektu (metadata schematu)
- zamykani nizke urovne (**radkove zamykani**)

Pr. 2.: NDB (network database)
- umoznuje spravovat data sdilena vice MySQL servery

Pr. 3.: MyISAM
- non-transakcni engine
- rychle cteni
- uloziste pro data pouzivanych klicu (indexy) a data pro query cache
Pr. 4.: Memory
- ne-transakcni engine
- neindexovana data
- table-level zamykani
- nelze zde pouzit delete a update (pouze INSERT, SELECT a REPLACE)
Pr. 5: CSV
- ulozeni dat v csv formatu

# Data Pipeline

- OLTP, OLAP, ELT/ETL

- OLTP = **Online Transaction Processing**
- OLAP = **Online Analytical Processing**
- ETL = **Extract → Transform → Load**
- ELT = **Extract → Transform → Load**
    

