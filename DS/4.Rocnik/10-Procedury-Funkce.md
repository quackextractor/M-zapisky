Typy:
- bez paramaetri
- se vstupnimi  IN(INPUT) nebo vystupnimi OUT(OUTPUT) parametri
- s oběma (doporuceno pro maturitu)

Příklad procedury s oběma v MySQL

PRIDAT PRIKLAD

## Funkce
- a) agregacni funkce sum(), count()
- b) systémové fce sysdate(), year(), check(), ...
- c) uživatelsky def. fce

Vlastnosti:
- mají jeden nebo více vstupních parametrů
- **vždy pouze 1** výstupní hodnostu
- => lze použít za klauzulí **SELECT**

Syntaxe uživatelsky def. fce:
 a) skalární

PRIDAT PRIKLAD MYSQL

b) uživatelská fce, která **vrací hodnoty v tabulce** (1 výstupní hodnota = tabulka)
-> returns table (return select * from zbozi;)

```mysql
DELIMITER $$

CREATE FUNCTION vek(par DATE)
RETURNS INT
DETERMINISTIC
BEGIN
  RETURN DATEDIFF(SYSDATE(), par);
END$$

DELIMITER ;

```


	ll  
