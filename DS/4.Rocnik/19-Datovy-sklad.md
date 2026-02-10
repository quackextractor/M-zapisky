## Datový sklad (Data warehouse DWH)
- centralni **uloziste** dat z jednoho nebo vice zdroju, optimalizovane pro ??? analyzy, reportingu a buisiness intelligence.
- vetsinou ve tvaru star db, (snowflake db) nebo galaxy db 
- zakladni je star db, ktera se sklada z jedne facy tabulky a vice dim tabulek
- tato db slouzi pro OLAP procesy
-

Pr. rozdil mezi OLTP a OLAP 
- OLTP je nad normalizovanou db v provozu

diagram s PIDs
druch < zvire < adopce > utulek > mesto
![[OLTP.png]]

- pro caste transakce (tzn insert, update, delete) + velky pocet
- OLAP diagram
![[OLAP.png]]

## Vizualizace dat v Power BI
- je proces grafického znazorneni informaci a dat
- vyuziva vizualni prvky jako grafy a mapy pro pochopeni trendu a vzoru (patterns) v datech
- cilem je transformovat  abstrakni data do srozumitelny formy (storytelling)
- -> duvodem je efektivnejsi ??? ??? zalozene na faktech (Data-driven decision making) a schopmost rychle identifikovat klicove identifikatory **vykonnosti** (**power** BI)

### Hlavní funkcionalita PowerBI
1. **Model View** ... zobrazeni dim a fact tabulek a jejich vazeb (joins, název jako ER model)
2. **Power Query** ... **umoznuje** editaci tabulek a tedy **transformaci** -> ELT process
3. **Dashboard** ... vizualizace dat pomoci grafu (napr. tab, sloupec, graf)
### DAX (Data Analysis Expressions)
jazyk pro tvorbu pokrocilych vypoctu a mereni

**Import dat:**
- a) **import** - data se nahraji primo dovnitr napr. jako csv soubor
- b) **direct query** - pripojeni primo na serveru (vestsinou na cloud)
- = (live connection) 