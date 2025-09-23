Nize naleznete kompletní script (vsechny prikazy jsou v lowercase, komentare jsou velmi stručne v ceste bez diakritiky). Script obsahuje vlozeni ukazkovych dat (pro overeni select prikazu), nastaveni domenove integrity, select s case, ulozenou proceduru, view, trigger se zalohovaci a log tabulkou, vytvoreni indexu a vytvoreni noveho usera s pravem pouze ke cteni na tabulku osivo.

---

## -- vytvoreni databaze a nastaveni pripojeni

```sql
-- vytvoreni databaze poleplodiny
create database poleplodiny;
go

-- nastaveni uziti databaze
use poleplodiny;
go
```

---

## -- nastaveni domenove integrity

```sql
-- overeni, ze cena za hodinu v tabulce pole je kladna
alter table dbo.pole add constraint chk_cenazahod_positive check (cenazahod > 0);
go
```

---

## -- vlozeni ukazkovych dat (pro overeni select prikazu)

```sql
-- vlozeni dat do tabulky druzstvo
insert into dbo.druzstvo (nazev, rozloha, oblast) values ('druzstvo a', 100, 'sever');
insert into dbo.druzstvo (nazev, rozloha, oblast) values ('druzstvo b', 150, 'jih');
go

-- vlozeni dat do tabulky pole
insert into dbo.pole (cis_pole, majitel, rozloha_po, nazev, id_dr, cenazahod) 
values (1, 'majitel1', 50, 'pole 1', 1, 100);
insert into dbo.pole (cis_pole, majitel, rozloha_po, nazev, id_dr, cenazahod) 
values (2, 'majitel2', 75, 'pole 2', 1, 150);
go

-- vlozeni dat do tabulky osivo
insert into dbo.osivo (nazev, cis_uzn_osiva, kod, pozn) 
values ('osivo1', 101, 111, 'poznamka1');
insert into dbo.osivo (nazev, cis_uzn_osiva, kod, pozn) 
values ('osivo2', 102, 112, 'poznamka2');
go

-- vlozeni dat do tabulky oseti
insert into dbo.oseti (idosivo, idpole, datum, mnozstvi_osiva, id_zam, pocethod) 
values (1, 1, '2023-04-01', 20, 1, 2);
insert into dbo.oseti (idosivo, idpole, datum, mnozstvi_osiva, id_zam, pocethod) 
values (2, 2, '2023-04-02', 30, 2, 3);
go

-- vlozeni dat do tabulky zamestnanci
insert into dbo.zamestnanci (prijmeni, imeno, rod_cis, id_dr) 
values ('novak', 'petr', '123456789', 1);
insert into dbo.zamestnanci (prijmeni, imeno, rod_cis, id_dr) 
values ('svoboda', 'jana', '987654321', 1);
go
```

---

## -- select prikaz s case pro overeni

```sql
-- select s case na tabulce pole, overeni ukazkovymi daty
select cis_pole, nazev, 
       case when cenazahod > 120 then 'drazsi' else 'levnejsi' end as kategorie_ceny
from dbo.pole;
go
```

---

## -- ulozena procedura (spocet rozlohy, celkova cena oseti a zlevneni ceny u pole s nejvetsi rozlohou)

```sql
-- 1. Ulozena procedura: Spocita rozlohu vsech poli urciteho druzstva
create procedure sp_scitat_rozlohu_druzstva
  @id_druzstva int
as
begin
  select sum(rozloha_po) as celkova_rozloha
  from dbo.pole
  where id_dr = @id_druzstva;
end;
go

-- Volani procedury pro druzstvo s ID 1
exec sp_scitat_rozlohu_druzstva @id_druzstva = 1;
go

-- 2. Ulozena procedura: Secte celkovou cenu oseti za jednotliva osiva
create procedure sp_scitat_cenu_oseti
  @idosivo int
as
begin
  select 
    o.idosivo,
    sum(ot.pocethod * p.cenazahod) as celkova_cena
  from dbo.oseti ot
  join dbo.pole p on ot.idpole = p.idpole
  join dbo.osivo o on ot.idosivo = o.idosivo
  where o.idosivo = @idosivo
  group by o.idosivo;
end;
go

-- Volani procedury pro osivo s ID 1
exec sp_scitat_cenu_oseti @idosivo = 1;
go

-- 3. Ulozena procedura: Zlevni cenu za hodinu u pole s nejvetsi rozlohou
create procedure sp_zlevnit_pole
  @id_druzstva int,
  @sleva_procent int
as
begin
  declare @max_idpole int;

  -- Najdi pole s nejvetsi rozlohou v druzstvu
  select top 1 @max_idpole = idpole
  from dbo.pole
  where id_dr = @id_druzstva
  order by rozloha_po desc;

  -- Aplikuj slevu na cenu za hodinu
  update dbo.pole
  set cenazahod = cenazahod * (1 - @sleva_procent / 100.0)
  where idpole = @max_idpole;

  -- Vrat upravene pole pro kontrolu
  select idpole, cis_pole, rozloha_po, cenazahod
  from dbo.pole
  where idpole = @max_idpole;
end;
go

-- Volani procedury: druzstvo 1, sleva 10%
exec sp_zlevnit_pole @id_druzstva = 1, @sleva_procent = 10;
go

-----------

-- Overeni

-- Kontrola rozlohy druzstva
select * from dbo.pole where id_dr = 1;

-- Kontrola ceny oseti
select * from dbo.oseti where idosivo = 1;

-- Kontrola upravene ceny pole
select * from dbo.pole where idpole = (select top 1 idpole from dbo.pole where id_dr = 1 order by rozloha_po desc);
```

---

## -- vytvoreni view, ktere zobrazuje, ktere osivo bylo oseto na jakych polech urcitym zamestnancem

```sql
-- vytvoreni view view_osivo_oseti pro prehled oseti
create view view_osivo_oseti as
select o.idosivo, o.nazev as osivo_nazev, ot.idpole, p.nazev as pole_nazev, z.id_zam, z.prijmeni, z.imeno, ot.datum
from dbo.oseti ot
join dbo.osivo o on ot.idosivo = o.idosivo
join dbo.pole p on ot.idpole = p.idpole
join dbo.zamestnanci z on ot.id_zam = z.id_zam;
go

-- select z view pro overeni, napr. pro zamestnance s id 1
select *
from view_osivo_oseti
where id_zam = 1;
go
```

---

## -- vytvoreni triggeru, ktery po vlozeni osiva do tabulky osivo zapise data do zalohove tabulky a logu

```sql
-- vytvoreni zalohove tabulky pro osivo
create table dbo.osivo_zal (
  idosivo int,
  nazev nvarchar(45),
  cis_uzn_osiva int,
  kod int,
  pozn nchar(80)
);
go

-- vytvoreni log tabulky pro zaznamy o vkladech
create table dbo.log_osivo (
  idosivo int,
  nazev nvarchar(45),
  cis_uzn_osiva int,
  datum datetime,
  cinnost nvarchar(50)
);
go

-- vytvoreni triggeru na tabulce osivo, ktery provede zalohu a log vklad
create trigger trg_osivo_insert
on dbo.osivo
after insert
as
begin
  set nocount on;
  
  -- zalohovani vlozeneho osiva
  insert into dbo.osivo_zal (idosivo, nazev, cis_uzn_osiva, kod, pozn)
  select idosivo, nazev, cis_uzn_osiva, kod, pozn
  from inserted;
  
  -- zapis do logu
  insert into dbo.log_osivo (idosivo, nazev, cis_uzn_osiva, datum, cinnost)
  select idosivo, nazev, cis_uzn_osiva, getdate(), 'vklad'
  from inserted;
end;
go

-- overeni triggeru vlozenim noveho osiva
insert into dbo.osivo (nazev, cis_uzn_osiva, kod, pozn) 
values ('osivo3', 103, 113, 'poznamka3');
go

-- overeni zalohy
select * from dbo.osivo_zal;
go

-- overeni logu
select * from dbo.log_osivo;
go
```

---

## -- vytvoreni indexu pro zrychleni dotazu na sloupci cis_pole v tabulce pole

```sql
-- vytvoreni indexu na sloupci cis_pole
create index idx_cis_pole on dbo.pole (cis_pole);
go

-- overeni existence indexu
select name, object_id 
from sys.indexes 
where name = 'idx_cis_pole';
go
```

---

## -- vytvoreni noveho usera s pravem pouze na cteni tabulky osivo

```sql
-- vytvoreni loginu a usera pro cteni
create login citac with password = 'heslo123';
go

create user citac for login citac;
go

-- prirazeni prava select na tabulku osivo
grant select on dbo.osivo to citac;
go

-- overeni selectu a pokus o insert (insert by mel selhat)
exec as user = 'citac';
select * from dbo.osivo;

begin try
  insert into dbo.osivo (nazev, cis_uzn_osiva, kod, pozn)
  values ('osivo_fail', 104, 114, 'poznamka_fail');
  print 'insert byl povolen, co je chybne';
end try
begin catch
  print 'insert neni povolen, jak se ocekava';
end catch;
revert;
go
```
