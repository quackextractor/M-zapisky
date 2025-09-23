= Speciální druh uložené procedury

Př.: Zajistěte, aby při evidenci nového výrobku do logu přidali potřebné informace.

| *vyrobky* |
| --------- |
| id_vyr    |
| nazev     |
| popis     |

```sql
create trigger tr_vlozZazVyrobky on vyrobky
after insert
as
declare @idv int
select @idv from inserted;

```

### Základní rozdělení trigger
- DML trigger: automaticky odpovídá na danou událost nad tabulkou nebo view -`INSERT, UPDATE, DELETE`
- DDL trigger: spouští se při CREATE, DROP, ALTER, GRANT, DENY, REVOKE
- Lock-On trigger: spouští se při vytvoření uživatelské session.

## DML
- Trigger se automaticky vytvoří v RDBMS při def. události
- V rámci jednoho triggeru existují 2 pseudotabulky, které zpřístupňují nová a stará data
- V rámci jednoho triggeru se pomocí ROLLBACK zruší operaci, která ho spustila 
- Jeden trigger lze použít i pro více akcí na jednou

Upozornění:
- Pokud jsou nadměrně využíváni, mohou vést k problémy s výkonem (např. blokování)
- Pokud nejsou správně napsány, může vést k ztrátám dat