## Datový sklad (Data warehouse DWH)

* Centrální **úložiště** dat z jednoho nebo více zdrojů, optimalizované pro analýzy, reporting a business intelligence.
* Většinou ve tvaru star DB, (snowflake DB) nebo galaxy DB.
* Základní je star DB, která se skládá z jedné fact tabulky a více dim tabulek.
* Tato DB slouží pro OLAP procesy.

Př. rozdíl mezi OLTP a OLAP

* OLTP je nad normalizovanou DB v provozu.

Diagram s PIDs
Druh < Zvíře < Adopce > Útulek > Město
![OLTP.png]

* Pro časté transakce (tzn. insert, update, delete) + velký počet.
* OLAP diagram
![OLAP.png]

## Vizualizace dat v Power BI

* Je proces grafického znázornění informací a dat.
* Využívá vizuální prvky, jako grafy a mapy, pro pochopení trendů a vzorů (patterns) v datech.
* Cílem je transformovat abstraktní data do srozumitelné formy (storytelling).
* -> Důvodem je efektivnější **rozhodování** založené na faktech (Data-driven decision making) a schopnost rychle identifikovat klíčové identifikátory **výkonnosti** (**Power** BI).

### Hlavní funkcionalita Power BI

1. **Model View** ... zobrazení dim a fact tabulek a jejich vazeb (joins, název jako ER model).
2. **Power Query** ... **umožňuje** editaci tabulek a tedy **transformaci** -> ELT proces.
3. **Dashboard** ... vizualizace dat pomocí grafů (např. tabulka, sloupec, graf).

### DAX (Data Analysis Expressions)

Jazyk pro tvorbu pokročilých výpočtů a měření.

**Import dat:**

* a) **Import** - data se nahrají přímo dovnitř, např. jako CSV soubor.
* b) **Direct Query** - připojení přímo na server (většinou na cloud).
* = (Live connection)