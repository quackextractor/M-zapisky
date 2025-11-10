Jistě, zde je dokument převeden do digitální, strukturované formy.

---

1. Jazyk SQL

a) Použití a rozdělení:
SQL(Structured Query Language) se používá pro práci s daty v relačních databázích. Dělí se na několik částí:

· DDL (Data Definition Language): Definice datových struktur (např. **CREATE, ALTER, DROP**).
· DML (Data Manipulation Language): Manipulace s daty (např. **SELECT, INSERT, UPDATE, DELETE**).
· DCL (Data Control Language): Správa práv a transakcí (např. **GRANT, REVOKE, COMMIT, ROLLBACK**).

b) Syntaxe příkazu SELECT:

```sql
SELECT [DISTINCT] sloupec1, sloupec2, ... agregační_funkce(sloupec)
FROM tabulka1 [ALIAS]
[JOIN tabulka2 ON podmínka_joinu]
[WHERE podmínka]
[GROUP BY sloupec1, sloupec2, ...]
[HAVING podmínka_na_agregaci]
[ORDER BY sloupec1 [ASC | DESC], sloupec2 [ASC | DESC], ...];
```

Popis klauzulí:

· SELECT: Určuje sloupce nebo výrazy, které se mají vrátit. DISTINCT odstraní duplicity
· FROM: Určuje tabulku(y), ze které se data čtou.
· JOIN: Spojuje data z více tabulek na základě podmínky.
· WHERE: Filtruje záznamy před agregací.
· GROUP BY: Seskupuje řádky do skupin pro agregaci (např. počty, součty).
· HAVING: Filtruje skupiny vytvořené GROUP BY (na rozdíl od WHERE filtruje po agregaci).
· ORDER BY: Řadí výslednou sadu podle zadaných sloupců.

---

2. Architektura DBS

a) Současná architektura:
U relačních DBS se používáklient-server architektura. Databázový server (např. PostgreSQL, MySQL) poskytuje služby klientským aplikacím, které se k němu připojují po síti.

b) Požadavky na DBS:

· Nezávislost dat: Logická a fyzická nezávislost dat na aplikacích.
· Abstrakce dat: Schéma, fyzické uložení a pohledy.
· Transakční zpracování: Zajištění vlastností ACID (Atomicity, Consistency, Isolation, Durability).
· Souběžný přístup: Řízení souběžných transakcí.
· Zotavení po chybě: Možnost obnovit data po selhání.
· Autorizace a autentizace: Řízení přístupu k datům.

c) Uložení a přístup k datům:
Data jsou uložena na pevném disku serveru v souborech, které spravuje DBMS. Přístup je umožněn prostřednictvím síťového připojení, kdy klient odesílá dotazy v jazyce SQL na server. Server dotaz zpracuje a vrátí klientovi pouze výsledek.

---

3. Filmová společnost – datový model

a) Logický model (Entitně-relační diagram):

· ENTITA: Film
  · id_film (PK)
  · nazev
  · id_zanr (FK)
  · delka
  · ...
· ENTITA: Žánr
  · id_zanr (PK)
  · nazev_zanru
· ENTITA: Projekce
  · id_projekce (PK)
  · id_film (FK)
  · datum_cas

b) Relační model (Tabulky):

· Film (id_film [PK], nazev, id_zanr [FK], delka, ...)
· Žánr (id_zanr [PK], nazev_zanru)
· Projekce (id_projekce [PK], id_film [FK], datum_cas)

c) SQL dotazy:

```sql
-- a) Datum nejstarší projekce
SELECT MIN(datum_cas) AS nejstarsi_projekce
FROM Projekce;

-- b) Počet filmů pro jednotlivé žánry
SELECT z.nazev_zanru, COUNT(f.id_film) AS pocet_filmu
FROM Zanr z
LEFT JOIN Film f ON z.id_zanr = f.id_zanr
GROUP BY z.nazev_zanru;

-- c) Filmy, které nebyly promítány (seřazené)
SELECT f.nazev, z.nazev_zanru
FROM Film f
JOIN Zanr z ON f.id_zanr = z.id_zanr
WHERE f.id_film NOT IN (SELECT DISTINCT id_film FROM Projekce)
ORDER BY z.nazev_zanru, f.nazev;
```

---

4. Integrita databáze

Integrita databáze znamená správnost a konzistenci uložených dat.

Referenční integritní omezení je pravidlo, které zajišťuje, že hodnota cizího klíče v jedné tabulce musí odkazovat na existující řádek v druhé tabulci (nebo být NULL). Zabraňuje vzniku "sirotčích" záznamů.

Příklad:
Máme tabulkyZakaznik (id, jmeno) a Objednavka (id, zakaznik_id, ...).

· zakaznik_id v Objednavka je cizí klíč odkazující na Zakaznik(id).
· Referenční integrita zabrání vytvoření objednávky s zakaznik_id = 999, pokud zákazník s id = 999 neexistuje.

---

5. Normalizace databáze

Normalizace je proces odstraňování redundance (nadbytečnosti) a nekonzistence dat z databázové struktury. Cílem je snížit duplikaci, usnadnit údržbu a zabránit anomáliím při vkládání, mazání a úpravách.

1. normální forma (1NF):
Tabulka je v 1NF,pokud:

2. Všechny atributy mají atomické (nerozložitelné) hodnoty.
3. Každý záznam je jedinečný.

Normalizace zadané tabulky:
Původní tabulka obsahuje redundanci v údajích o parkovišti(parkovište, umístění, kapacita, pocet_pater se opakují pro každého zaměstnance na stejném parkovišti).

Návrh do 3NF:

· Zamestnanec (cislo_zam [PK], jmeno_zam, cislo_mista [FK])
· Parkoviste (parkoviste_id [PK], nazev, umisteni, kapacita, pocet_pater)
· ParkovaciMisto (cislo_mista [PK], parkoviste_id [FK])

Relační schéma:

```
Zamestnanec (
  cislo_zam INTEGER PRIMARY KEY,
  jmeno_zam VARCHAR(100) NOT NULL,
  cislo_mista INTEGER,
  FOREIGN KEY (cislo_mista) REFERENCES ParkovaciMisto(cislo_mista)
)

Parkoviste (
  parkoviste_id INTEGER PRIMARY KEY,
  nazev VARCHAR(50) UNIQUE NOT NULL, -- 'Yellow', 'Green'
  umisteni VARCHAR(50), -- 'Blok A', 'Blok B'
  kapacita INTEGER,
  pocet_pater INTEGER
)

ParkovaciMisto (
  cislo_mista INTEGER PRIMARY KEY,
  parkoviste_id INTEGER NOT NULL,
  FOREIGN KEY (parkoviste_id) REFERENCES Parkoviste(parkoviste_id)
)
```

---

6. SQL dotaz – Dopravní společnosti

```sql
SELECT
  ds.nazev AS spolecnost,
  ds.zeme,
  SUM(t.pocet_vozu) AS celkovy_pocet_vozu
FROM
  DopravniSpolecnost ds
JOIN
  Trasa t ON ds.id = t.spolecnost_id
JOIN
  DopravniVuz dv ON t.vuz_id = dv.id
WHERE
  dv.vyrobce = 'Mercedes'
GROUP BY
  ds.nazev, ds.zeme;
```