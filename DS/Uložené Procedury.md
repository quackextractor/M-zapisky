Uloženou proceduru je možno si představit jako metodu na straně SQL serveru a nebo jako dávkový příkaz, který můžeme vyvolat a uložit. Pak ho vyvolám pomocí jména.

![[Pasted image 20250312095323.png]]
### Výhody
Umožní provádět opakovaně určité činnosti:
- předkompilované prostředí
- server sestavuje proceduru a execution plan, následkem je velké zvýšení výkonu
- snížení komunikace klient-server v provozu
- efektivní opětovné využití kódu jak pro více uživatelů tak pro více klientů
- zvýšená bezpečnostní kontrola:
	- uživateli můžete udělit oprávnění k výkonu procedury nezávisle na tabulce

### Nevýhody
- V některých DS se používá jazyk CLON, neplatí pro Python a Javu
- Pro procedury některých DS existuje debugging, ale chybí Profilování (= sledování a analýza výkonu)
- Procedury nejsou přenositelné mezi DS
- Uložené procedury mají uložený přístupový kód (není vhodné pro dodavatele softwaru)
- Přesouvání aplikační logiky na DB vrstvu se aplikace znepřehledňuje 
- Pokud používáme uložené procedury na všechno (login, vytvoření tabulky, nastavení vazby), bude jich velmi mnoho

### Druhy uložených procedur
- vstupní
- výstupní
- vstupní i výstupní



```sql
CREATE PROCEDURE p_PrumernaCenaZaDruh
    @hodnota FLOAT OUTPUT,
    @id INT
AS
BEGIN
    DECLARE @naz NVARCHAR(50);
    DECLARE @hodn FLOAT;

    -- Compute the average price of products for the given category
    SELECT @hodn = AVG(v.cena)
    FROM vyrobky v
    INNER JOIN druhy d ON v.id_druh = d.id_druh
    WHERE d.id_druh = @id;

    -- Get the category name
    SELECT @naz = d.nazev FROM druhy d WHERE d.id_druh = @id;

    -- Set output value
    SET @hodnota = @hodn;

    -- Print statements with proper syntax
    PRINT 'Průměrná cena výrobků za druh = ' + CAST(@hodn AS NVARCHAR(10));
    PRINT 'Druh = ' + CAST(@id AS NVARCHAR(10));
    PRINT 'Název druhu = ' + @naz;
END;

```

```sql
CREATE TABLE druhy (
    id_druh INT PRIMARY KEY IDENTITY(1,1),
    nazev NVARCHAR(50) NOT NULL
);

CREATE TABLE vyrobky (
    id_vyrobek INT PRIMARY KEY IDENTITY(1,1),
    id_druh INT FOREIGN KEY REFERENCES druhy(id_druh),
    cena FLOAT NOT NULL
);
```

```sql
INSERT INTO druhy (nazev) VALUES
('Elektronika'),
('Nábytek'),
('Kuchyňské potřeby');

INSERT INTO vyrobky (id_druh, cena) VALUES
(1, 999.99),
(1, 1200.50),
(1, 1100.75),
(2, 5000.00),
(2, 4500.50),
(3, 150.00),
(3, 200.75),
(3, 175.50);

```

```sql
DECLARE @vysledek FLOAT;

EXEC p_PrumernaCenaZaDruh @hodnota = @vysledek OUTPUT, @id = 1;

SELECT @vysledek AS Prumerna_Cena;

```