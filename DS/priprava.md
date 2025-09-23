

# Dokumentace pro Databázové Systémy

## Uložené procedury

### Procedura pro získání informací o výrobcích

Tato procedura vybírá informace o výrobcích z tabulky `tvyrobek`.

```sql
create procedure get_vyrobky
as
begin
    select nazevvyr, cenajvyr, danvyr, popisvyr from tvyrobek;
end;

exec get_vyrobky;
```

---

### Procedura pro zobrazení detailu faktury

Procedura zobrazuje kompletní detaily faktury včetně informací o zákazníkovi, dodavateli, zaměstnanci, výrobku a počtu kusů.

```sql
create procedure get_faktura_detail @idf int
as
begin
    select f.cisfakt, d.nazevdod, z.nazevzak, zam.jmenozam, v.nazevvyr, r.pocetks 
    from tfaktura f
    join tzakaznik z on f.zakid = z.idzak
    join tzamestnanec zam on f.zamid = zam.idzam
    join tdodavatel d on f.dodid = d.iddod
    join trozpis r on f.idf = r.faktid
    join tvyrobek v on r.vyrid = v.idvyr
    where f.idf = @idf;
end;

exec get_faktura_detail @idf = 100;
```

---

### Procedura pro výpočet průměrné ceny faktur

Procedura spočítá průměrnou cenu ze všech faktur pomocí funkce `avg()`.

```sql
create procedure prumerna_cena_faktur
as
begin
    select avg(celkem) as prumer from tfaktura;
end;

exec prumerna_cena_faktur;
```

---

### Procedura pro vyhledání faktur dle zaměstnance

Procedura vrací faktury, které byly zpracovány konkrétním zaměstnancem.

```sql
create procedure faktury_podle_zamestnance @zamid int
as
begin
    select * from tfaktura where zamid = @zamid;
end;

exec faktury_podle_zamestnance @zamid = 1;
```

---

### Procedura pro změnu DPH výrobku

Procedura umožňuje aktualizovat sazbu DPH u vybraného výrobku.

```sql
create procedure update_dph @idvyr int, @nova_dan smallint
as
begin
    update tvyrobek set danvyr = @nova_dan where idvyr = @idvyr;
end;

exec update_dph @idvyr = 3, @nova_dan = 15;
```

---

### Procedura pro výpočet faktur dle města zákazníka

Tato procedura seskupí a spočítá počet faktur podle města zákazníka.

```sql
create procedure faktury_podle_mesta
as
begin
    select z.mestozak, count(f.idf) as pocet 
    from tfaktura f
    join tzakaznik z on f.zakid = z.idzak
    group by z.mestozak;
end;

exec faktury_podle_mesta;
```

---

## Definice tabulek a inicializační skripty

Níže jsou uvedeny vytvořené tabulky v databázi a příklady vkládání dat.

### Tabulka `log`

Tabulka slouží k zaznamenávání operací prováděných nad ostatními tabulkami.

```sql
create table log (
    log_id int primary key identity(1,1),
    tabulka varchar(50) not null,
    operace varchar(10) not null,
    zaznam_id int not null,
    cas datetime not null
);
```

---

### Tabulka `dodavatel`

Tabulka obsahuje informace o dodavatelích.

```sql
create table dodavatel (
    dodavatel_id int primary key identity(1,1),
    jmeno varchar(100) not null,
    adresa varchar(200),
    telefon varchar(20),
    email varchar(100)
);
```

---

### Tabulka `vyrobek`

Tabulka slouží pro evidenci výrobků.

```sql
create table vyrobek (
    vyrobek_id int primary key identity(1,1),
    nazev varchar(100) not null,
    cena decimal(10,2) not null,
    dodavatel_id int foreign key references dodavatel(dodavatel_id)
);
```

---

### Tabulka `zakaznik`

Tabulka obsahuje informace o zákaznících.

```sql
create table zakaznik (
    zakaznik_id int primary key identity(1,1),
    jmeno varchar(100) not null,
    adresa varchar(200),
    telefon varchar(20),
    email varchar(100)
);
```

---

### Tabulka `zamestnanec`

Tabulka evidující zaměstnance.

```sql
create table zamestnanec (
    zamestnanec_id int primary key identity(1,1),
    jmeno varchar(100) not null,
    pozice varchar(50),
    plat decimal(10,2),
    datum_nastupu date
);
```

---

### Tabulka `rozpis`

Tabulka pro plánování projektů, která odkazuje na zaměstnance a zákazníky.

```sql
create table rozpis (
    rozpis_id int primary key identity(1,1),
    projekt_nazev varchar(150) not null,
    zamestnanec_id int foreign key references zamestnanec(zamestnanec_id),
    zakaznik_id int foreign key references zakaznik(zakaznik_id),
    datum_zacatku date,
    datum_konce date
);
```

---

## Ukázky vkládání dat a aktualizací

### Vkládání záznamů

Příklady vkládání dat do tabulek `dodavatel`, `vyrobek`, `zakaznik`, `zamestnanec` a `rozpis`.

```sql
insert into dodavatel (jmeno, adresa, telefon, email) 
values 
    ('Tech Supplies s.r.o.', 'Praha 5', '777123456', 'tech@supplies.cz'),
    ('Material Plus a.s.', 'Brno', '555987654', 'info@materialplus.cz');

insert into vyrobek (nazev, cena, dodavatel_id) 
values 
    ('Kancelarska zidle', 2499.99, 1),
    ('Pracovni stul', 3599.00, 1),
    ('LED svitidlo', 899.50, 2);
	
insert into zakaznik (jmeno, adresa, telefon, email) 
values 
    ('Jan Novak', 'Ostrava', '603112233', 'novak@email.cz'),
    ('Eva Svobodova', 'Plzen', '606445566', 'eva.svobodova@post.cz');

insert into zamestnanec (jmeno, pozice, plat, datum_nastupu) 
values 
    ('Petr Cerny', 'Manager', 55000, '2020-05-01'),
    ('Anna Kralova', 'Asistent', 32000, '2023-02-15');

insert into rozpis (projekt_nazev, zamestnanec_id, zakaznik_id, datum_zacatku, datum_konce) 
values 
    ('Rekonstrukce kancelare', 1, 1, '2024-03-01', '2024-06-30');

insert into rozpis (projekt_nazev, zamestnanec_id, zakaznik_id, datum_zacatku) 
values ('Marketingova kampan', 2, 2, '2024-04-10');

-- Vložíme testovací dodavatele
insert into dodavatel (jmeno) values ('Testovaci dodavatel X');
```

### Ukázky aktualizací a mazání

```sql
delete from vyrobek where vyrobek_id = 3;

delete from zamestnanec where zamestnanec_id = 2;

update vyrobek set cena = 2699.99 where vyrobek_id = 1;

update zakaznik set adresa = 'Praha 1, Nové Město' where zakaznik_id = 2;

select * from log;
```

---

## Trigger – logování akcí

Vytvořené triggery logují operace INSERT, DELETE a UPDATE do informační tabulky `log`. Díky nim je vždy vidět, která tabulka byla ovlivněna, jaká operace byla provedena, které záznamy a kdy.

### Trigger pro logování INSERT do `rozpis`

```sql
create trigger trg_rozpis_insert
on rozpis
after insert
as
begin
    insert into log (tabulka, operace, zaznam_id, cas)
    select 'rozpis', 'insert', i.rozpis_id, getdate()
    from inserted i;
end;
```

---

### Trigger pro logování INSERT do `dodavatel`

```sql
create trigger trg_dodavatel_insert
on dodavatel
after insert
as
begin
    insert into log (tabulka, operace, zaznam_id, cas)
    select 'dodavatel', 'insert', i.dodavatel_id, getdate()
    from inserted i;
end;
```

---

### Trigger pro logování DELETE z `vyrobek`

```sql
create trigger trg_vyrobek_delete
on vyrobek
after delete
as
begin
    insert into log (tabulka, operace, zaznam_id, cas)
    select 'vyrobek', 'delete', d.vyrobek_id, getdate()
    from deleted d;
end;
```

---

### Trigger pro logování DELETE z `zamestnanec`

```sql
create trigger trg_zamestnanec_delete
on zamestnanec
after delete
as
begin
    insert into log (tabulka, operace, zaznam_id, cas)
    select 'zamestnanec', 'delete', d.zamestnanec_id, getdate()
    from deleted d;
end;
```

---

### Trigger pro logování UPDATE v `vyrobek`

```sql
create trigger trg_vyrobek_update
on vyrobek
after update
as
begin
    insert into log (tabulka, operace, zaznam_id, cas)
    select 'vyrobek', 'update', d.vyrobek_id, getdate()
    from deleted d;
end;
```

---

### Trigger pro logování UPDATE v `zakaznik`

```sql
create trigger trg_zakaznik_update
on zakaznik
after update
as
begin
    insert into log (tabulka, operace, zaznam_id, cas)
    select 'zakaznik', 'update', d.zakaznik_id, getdate()
    from deleted d;
end;
```

---

## Cvičení s uživatelskými právy a přidělováním privilegíí

Cvičení zahrnuje vytvoření databáze, tabulky a příslušných uživatelů s různými právy. Uživatelé jsou například:

- **cteAAA** – uživatel s právem pouze číst data.
- **insAAA** – uživatel s právem vkládání dat.
- **updAAA** – uživatel s právem aktualizace dat.

### Vytvoření databáze a tabulky `osoby`

```sql
create database prijmeni;
go

use prijmeni;
go

create table osoby (
    prijmeni varchar(50),
    jmeno varchar(50),
    datum_narozeni date
);
go

insert into osoby values ('Novak','Petr','1980-05-12');
insert into osoby values ('Svoboda','Jana','1992-10-01');
insert into osoby values ('Polak','Jan','2000-12-12');
go

select * from osoby;
go
```

---

### Testování přístupových práv pomocí `EXECUTE AS`

Níže jsou ukázky, jak se mění práva uživatelů pomocí příkazu `execute as` a následně operace (čtení, vkládání, aktualizace) ověřují odpovídající omezení.

#### Čtení pod uživatelem cteAAA

```sql
execute as user = 'cteaaa';
select * from osoby;  -- Očekávaný výsledek: úspěšné vyčtení dat
revert;
go
```

#### Pokus o vložení (vkládání není povoleno)

```sql
execute as user = 'cteaaa';
insert into osoby values ('Test','Neopravneny','2025-01-01');  -- Očekává se chyba
revert;
go
```

#### Vkládání pod uživatelem insAAA

```sql
execute as user = 'insaaa';
insert into osoby values ('Maly','Karel','1999-03-15');
revert;
go

select * from osoby;
go
```

#### Pokus o aktualizaci pod uživatelem insAAA (aktualizace není povoleno)

```sql
execute as user = 'insaaa';
update osoby
   set jmeno = 'Zmena'
 where prijmeni = 'Novak';  -- Očekává se chyba
revert;
go
```

#### Aktualizace pod uživatelem updAAA

```sql
execute as user = 'updaaa';
update osoby
   set jmeno = 'Zmeneno'
 where prijmeni = 'Novak';
revert;
go

select * from osoby;
go
```

---

## Shrnutí praktických úloh a odevzdání

### Praktické úlohy obsahují:

1. **Vytvoření databáze** – např. databáze pojmenovaná příjmením (v tomto případě `prijmeni`).
2. **Vytvoření tabulky `osoby`** – se sloupci `prijmeni`, `jmeno` a `datum_narozeni`.
3. **Naplňování tabulky** – vložení několika záznamů.
4. **Vytvoření uživatelů a přidělení práv:**
   - `cteAAA` – pouze pro čtení.
   - `insAAA` – pouze pro vkládání.
   - `updAAA` – pouze pro aktualizaci.
5. **Testování práv** – provedení operací pod jednotlivými uživateli a ověření, zda jsou dodržena omezení podle přidělených práv.
6. **Úloha se svědectvími (printscreeny a skripty)** – odevzdání skriptů a screenshotů dle zadaného vzoru.
7. **Logování operací pomocí triggerů** – vytvoření informační tabulky `log` a odpovídajících triggerů pro INSERT, DELETE a UPDATE u zadaných tabulek.

### Odevzdání

- **ER Schema** – včetně informační tabulky.
- **Skripty** – pro vytvoření triggerů, procedur, a operace vkládání a aktualizace.
- **Prtscr datového listu** – dokumentující operace provedené v databázi.
- Skripty a výsledné screenshoty jsou následně uloženy dle požadovaného umístění, např. na disk `O:\odevzdat\...`.