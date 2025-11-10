# 8. Subquery, Podselecty

- lze použít ve všech DML příkazech
- musí být uzavřen v kulatých závorkách
- počet podselectů **není omezen**
- nejdříve se vykoná nejvíce vnořený podselect
- pokud vrátí 1 hodnotu, lze použít matematické operandy: =, !=, <, >, atd... 

```sql
-- DML prikazy

-- Zvýší cenu lístkù o 20% u všech filmù v kinì "blanik".  
update film set cena_listek = cena_listek * 1.2
	where kino_id = (
	select id from kino
	where nazev = 'kino city'
	)

-- Smaže všechny lístky, u kterých je film typu "reklamni".
delete from listek 
where film_id = (
select id from film 
where typ = 'reklamni'
)

-- Vypíše údaje zákazníkù, kteøí mají alespoò jednu objednávku za více než 500 Kè.
select distinct z.* 
from zakaznik z
where z.id in (select zak_id from objednavka where cena_objednavky > 500);


-- Do nové tabulky "premiovy_zakaznik" vložte všechny zákazníky, kteøí mají alespoò jednu objednávku za více než 1 000,-Kè.
insert into premiovy_zakaznik
select distinct z.* 
from zakaznik z
where z.id in (select zak_id from objednavka where cena_objednavky > 1000);
```