## Co je to View?

View v SQL Serveru je virtuální tabulka, která je výsledkem uloženého SQL dotazu. View neobsahuje vlastní data, ale dynamicky zobrazuje data z jedné nebo více podkladových tabulek.

## Vytvoření View

View se vytváří pomocí příkazu `CREATE VIEW` následovaného dotazem `SELECT`.

### Syntaxe:

```sql
CREATE VIEW nazev_view AS
SELECT sloupec1, sloupec2, ...
FROM tabulka
WHERE podmínka;
```

### Příklad:

Pokud máme tabulku `Zamestnanci` a chceme vytvořit view zobrazující pouze aktivní zaměstnance:

```sql
CREATE VIEW AktivniZamestnanci AS
SELECT EmployeeID, Jmeno, Prijmeni, Pozice
FROM Zamestnanci
WHERE Aktivni = 1;
```

## Použití View

Po vytvoření je možné view dotazovat stejným způsobem jako běžnou tabulku:

```sql
SELECT * FROM AktivniZamestnanci;
```

## Úprava View

Pokud potřebujeme změnit existující view, použijeme `ALTER VIEW`:

```sql
ALTER VIEW AktivniZamestnanci AS
SELECT EmployeeID, Jmeno, Prijmeni, Pozice, Oddeleni
FROM Zamestnanci
WHERE Aktivni = 1;
```

## Smazání View

Pro odstranění view použijeme `DROP VIEW`:

```sql
DROP VIEW AktivniZamestnanci;
```

## Výhody použití View

- **Zjednodušení složitých dotazů** – umožňuje pracovat s daty jako s tabulkou.
- **Zvýšení bezpečnosti** – uživatelé mohou přistupovat pouze k definovaným datům bez přímého přístupu k tabulkám.
- **Zlepšení výkonu** – některé optimalizace mohou být uloženy na úrovni view.
- **Opětovné použití** – view lze využívat v různých dotazech bez nutnosti opakovaného psaní složitého SQL kódu.

## Nevýhody použití View

- **Omezená editace dat** – některé view nejsou aktualizovatelné (například pokud obsahují agregované funkce).
- **Výkon může být ovlivněn složitostí view** – složitější dotazy mohou zpomalit provádění.
- **Závislost na tabulkách** – pokud se změní struktura podkladových tabulek, je nutné upravit také view.