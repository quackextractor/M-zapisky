
# Storage Engines

- oblasti na disku vymezené pro uložení dat různého typu (MySQL je multiplatformní, může ukládat i NoSQL data, např. JSON)
- => spravují fyzická data (file management)
- software pro storage engine je zodpovědný za provedení SQL příkazů pro načítání a ukládání dat

## Př. 1: InnoDB

- používání transakcí a ACID při načítání a ukládání dat
- logická struktura objektů (metadata schématu)
- zamykání nízké úrovně (řádkové zamykání)

## Př. 2: NDB (Network Database)

- umožňuje spravovat data sdílená více MySQL servery

## Př. 3: MyISAM

- netransakční engine
- rychlé čtení
- úložiště pro data používaných klíčů (indexy) a data pro query cache

## Př. 4: Memory

- netransakční engine
- neindexovaná data
- table-level zamykání
- nelze zde použít DELETE a UPDATE (pouze INSERT, SELECT a REPLACE)

## Př. 5: CSV

- uložení dat v CSV formátu

# Data Pipeline

- OLTP, OLAP, ELT/ETL

- OLTP = **Online Transaction Processing**
- OLAP = **Online Analytical Processing**
- ETL = **Extract → Transform → Load**
- ELT = **Extract → Transform → Load**

