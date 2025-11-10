**1. K čemu je určen jazyk SQL a jak se rozděluje? Vysvětlete kompletní příkaz SELECT, včetně všech klauzulí, a podrobně je popište.**

**2. Databázové systémy (DBS) – Jaké architektury se v současnosti používají u databázových systémů a jaké požadavky by měly splňovat? Jakým způsobem je možno s daty pracovat?**

**3. Vytvořte logický (ER) model pro filmovou společnost, která se zabývá projekcí filmů. Pro potřeby evidence ukládá data o zaměstnancích, filmech, projekcích atd. Dále vytvořte následující dotazy:**

a) **Datum nejstarší projekce v evidenci.**
b) **Počet filmů v evidenci pro jednotlivé žánry.**
c) **Filmy, které nebyly dosud promítány, seřazené podle žánru a názvu filmu.**

**4. Vysvětlete pojem integrita dat v databázi. Popište a vysvětlete referenční integritu a uveďte jednoduchý příklad.**

**5. Proč provádíme normalizaci databáze? Co to znamená, že je databáze v 1. normální formě (1NF)?**

Normalizujte následující tabulku tak, aby výsledná databáze splňovala 1. až 3. normální formu (3NF). Nakreslete nové relační schéma se všemi potřebnými tabulkami, včetně klíčů a omezení.

*Popis tabulky: Organizace má několik parkovišť, které používají zaměstnanci. Tabulka ukazuje zaměstnance, kterým bylo přiděleno parkovací místo. Každé parkovací místo je jedinečně identifikováno pomocí čísla parkovacího místa.*

| číslo_zam | jmeno_zam        | parkovište | umístění | kapacita | pocet_pater | číslo_mista |     |
| --------- | ---------------- | ---------- | -------- | -------- | ----------- | ----------- | --- |
| 1156      | Jane Jones       | Yellow     | Blok A   | 120      | 3           | 123         |     |
| 2311      | Karen Gilmore    | Yellow     | Blok B   | 120      | 3           | 145         |     |
| 1167      | Richard Bilgitt  | Yellow     | Blok B   | 120      | 3           | 156         |     |
| 2345      | Guy Ritchie      | Green      | Blok D   | 45       | 2           | 26          |     |
| 3434      | Stephen Williams | Green      | Blok D   | 45       | 2           | 34          |     |

**6. Pro dané tři tabulky sestavte příkaz SQL, který vypíše dopravní společnosti, které mají na své trase vozy Mercedes. Výpis obsahuje název společnosti, zemi a celkový počet vozů.**

**Dopravní_vůz** (id, vyrobce, typ_vozu, najeto_km, kapacita, vozidlo_v_provozu_od)
**Dopravní_společnost** (id, nazev, zeme, svetadil, zalozeno)
**Trasa** (id, společnost_id, vuz_id, pocet_vozu)