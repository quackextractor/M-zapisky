**2. krok OLAP** (Online Analytics Processing)
- proces efektivniho ziskavani dat z databaze
- pouzivaji se databaze data warehouse, star db -> vsechny tyto pojmy odpovidaji strukture db
Tato db se sklada:
- a) z FACT tabulek "obsahuje klice, ktere odkazuji na DIM table + udaje, ktere lze merit, pouzit atd."
- b) z DIM tabulek "opakuje udaje kdo, co, kde, kdy (ciselniky)"
Prechod mezi OLTP (plne normalizovane db) a OLAP (FACT + DIM tabulky) se provadi ELT/ETL procesy

Př. star db:

Mermaid diagram star db. jeden FACT T. ze ktery vychazi vice povinnych vazeb na ruzne DIM T1, DIM T2 ... do hvezdy
DIM tabulka ... vychazejici z DIM T
útulek ... adopce zvirat
DIM T" zvire, chovatel, utulek, novy majitel
- poplatek za adopci
- naklady
- dat. prichodu
- dat. odchodu

Nové atributy:
poplatek za adopci + naklady -> zisk
 dat. prichodu + dat. odchodu -> delka pobytu

Problem + Reseni:
Kdyby chybeli udaje povinne, tak data z utulku musime poslat zpatky s chybovou hlaskou, nemuzeme si vymyslet povinne udaje, ktere nam neprisli

!!
Přímý přechod z normalizovany db do DIM tab je pomoci VIEWS. 
- a) view pro spojeni druh, zvire, rasa
- b) insert into dim_zvire tabulky
- c) + vytvorenich novych unikatnich SKs a ulozeni PKs + NKs k zaznamu OLAP pouzva vlastni unikatni klice **Surrogatekeys**
- SKs misto puvodnich PKs
- Naturalkeys (NKs) ... prirazene unikatni cislo (napr rodne cislo, čip id...)