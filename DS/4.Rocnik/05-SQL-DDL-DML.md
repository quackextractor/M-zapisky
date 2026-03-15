# 5. SQL, DDL, DML, joins, agregační funkce

## SQL
= **Structured Query Language** = dotazovací jazyk, interpretovaný jazyk.
- Spravován **Managment Studiem** daného DB serveru.
- (MS = udržuje syntaxi a provádí příkazy SQL nad databází (úložištěm))
## SQL DDL
= **Data Definition Language**
- příkazy pro práci s objekty (např: database, table, view, index, constraint, ...)

jsou:
- **create** = vtytváření, 
- **alter** = změna struktury,
- **drop** = smazání

```sql
-- CREATE
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    hire_date DATE
);

-- ALTER
ALTER TABLE employees
ADD COLUMN salary DECIMAL(10,2);

-- DROP
DROP TABLE employees;
```

- pokud nejde smazat, tak **jde o tabulku na straně 1**, na které závisí tabulka na straně N

## SQL DML
= **Data Manipulation Language**
- příkazy pro práci s **daty** (hodnotami)
jsou:
- **insert** = vložení 
- **update** = změna,
- **delete** = smazání
- **select** = výpis

```sql
-- INSERT
INSERT INTO Employees (FirstName, LastName, Position, Salary)
VALUES ('John', 'Doe', 'Developer', 60000);

-- UPDATE
UPDATE Employees
SET Salary = 65000
WHERE EmployeeID = 1;

-- DELETE
DELETE FROM Employees
WHERE EmployeeID = 1;

-- SELECT
SELECT EmployeeID, FirstName, LastName, Salary
FROM Employees
WHERE Salary > 50000;
```

pokud chceme pro určité záznamy použijeme podmínku 

```sql
-- Zvýšení platu jen pro zaměstnance ve vývojovém oddělení
UPDATE Employees
SET Salary = Salary + 5000
WHERE Position = 'Developer';
```

```sql
-- Pridani platu vsem IT
UPDATE zam SET plat = plat + 1000
WHERE pozice_id = (SELECT id FROM pozice WHERE nazev = 'IT');

-- Vymazani oddeleni IT ze Zamestnancu
DELETE FROM zam
WHERE pozice_id = (SELECT id FROM pozice WHERE nazev = 'IT')

-- plný select
SELECT [DISTINCT | ALL] atr1, atr2, ...
FROM table_name
[INNER | LEFT | RIGHT | FULL OUTER JOIN another_table
    ON table_name.atr = another_table.atr]
WHERE condition
GROUP BY atr1, atr2, ...
HAVING condition
ORDER BY atr1 [ASC | DESC], atr2 [ASC | DESC]
LIMIT number_of_rows;
```