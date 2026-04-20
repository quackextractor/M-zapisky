# Teoretický list: Integrita dat relační databáze

### 1. Význam integrity dat 
Integrita databáze znamená zajištění jednoznačnosti, konzistence, spolehlivosti a přesnosti dat po celou dobu jejich životnosti. Zajišťuje, že se databáze nachází vždy v platném a správném stavu a nedochází k ukládání nesmyslných nebo poškozených údajů. Toho se dosahuje pomocí aplikování takzvaných integritních omezení.

### 2. Typy integritních omezení

**Entitní integrita**
* Slouží k jednoznačné identifikaci každého konkrétního záznamu v tabulce.
* Tuto integritu realizuje primární klíč (PRIMARY KEY), který zaručuje, že hodnota je pro každý řádek zcela unikátní a nesmí nikdy obsahovat prázdnou hodnotu (NOT NULL).

**Referenční integrita**
* Zajišťuje správné a logické vazby mezi tabulkami a chrání databázi před vznikem takzvaných "sirotčích" záznamů.
* Pravidlo stanovuje, že každý cizí klíč (FOREIGN KEY) v jedné tabulce musí buď odkazovat na reálně existující primární klíč v jiné tabulce, nebo musí nabývat hodnoty NULL, pokud to návrh povoluje.
* Výchozí chování databáze zakazuje smazat záznam z tabulky na straně vztahu "1", pokud na něj stále existuje odkaz z tabulky na straně "N".
* Pro řešení aktualizací a mazání propojených dat se využívají dodatečná pravidla jako ON DELETE CASCADE (automatické smazání potomků), ON DELETE SET NULL (vymazání cizího klíče), NO ACTION nebo SET DEFAULT.

**Doménová integrita**
* Omezuje a definuje množinu všech přípustných hodnot pro konkrétní neklíčové sloupce.
* Realizuje se primárně volbou správného datového typu (např. INT, VARCHAR, DATE) a nastavením rozsahu.
* Mezi další omezující pravidla patří NOT NULL (zákaz prázdné hodnoty) a UNIQUE (zajištění unikátnosti hodnot ve sloupci).
* Součástí doménové integrity je omezení CHECK, které ověřuje splnění logického výrazu před vložením dat (např. kontrola `plat > 0` nebo `vek >= 18`).
* Využívá se také pravidlo DEFAULT, které do sloupce automaticky dosadí výchozí hodnotu, pokud uživatel při vkládání řádku žádnou nespecifikuje.

**Uživatelská (procedurální) integrita**
* Zatímco předchozí omezení jsou deklarativní a definují se přímo ve struktuře tabulky (při použití DDL), procedurální integrita se využívá pro specifická a složitá obchodní pravidla.
* Řeší se pomocí naprogramovaného kódu, nejčastěji pomocí uložených procedur nebo triggerů.
* Trigger dokáže automaticky reagovat na změny dat (operace DML) a udržet konzistenci, například automatickým logováním historie, ručně definovaným kaskádovým mazáním nebo úplným zablokováním nechtěné operace.

### 3. Způsoby nastavení v SQL a příklady
Integritní omezení se zapisují v jazyce SQL převážně pomocí DDL příkazů CREATE TABLE nebo ALTER TABLE.

**Příklad komplexní tabulky s integritními omezeními:**

```sql
CREATE TABLE Zamestnanci (
    -- Entitní integrita
    id_zamestnance INT PRIMARY KEY,

    -- Doménová integrita (NOT NULL, UNIQUE, CHECK, DEFAULT)
    jmeno VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    plat DECIMAL(10, 2) CHECK (plat >= 15000),
    datum_nastupu DATE DEFAULT CURRENT_DATE,

    -- Referenční integrita
    id_oddeleni INT,
    CONSTRAINT fk_oddeleni FOREIGN KEY (id_oddeleni)
        REFERENCES Oddeleni(id_oddeleni)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
```

********************************************************************************

# Cvičení k maturitní otázce

Vypracujte odpovědi na následující otázky.

**1. Definice a účel integrity**
Vysvětlete, co znamená pojem integrita databáze. Jaké tři hlavní vlastnosti databázových záznamů tento pojem zastřešuje a pomocí jakých prostředků se těchto vlastností dosahuje?

**2. Entitní vs. referenční integrita**
Detailně popište rozdíl mezi entitní a referenční integritou. K jakému typu klíče se obě tyto integrity vážou a co přesně v databázi zajišťují? Co se stane v databázi, dojde-li k porušení referenční integrity, a jak se tento jev odborně nazývá?

**3. Návrh SQL struktury**
Napište SQL příkaz (DDL) pro vytvoření tabulky `Vozidla`. Tabulka musí splňovat následující integritní omezení:
* Sloupec `spz` bude sloužit jako textový primární klíč o délce 8 znaků.
* Sloupec `vin_kod` musí být unikátní a nesmí být nikdy prázdný.
* Sloupec `rok_vyroby` musí přijímat pouze hodnoty větší nebo rovné roku 2000.
* Sloupec `id_majitel` bude cizím klíčem odkazujícím na tabulku `Majitele (id_majitel)`. Pokud je majitel z databáze vymazán, automaticky se musí vymazat i všechna jeho vozidla.

**4. Deklarativní vs. procedurální integrita**
Vysvětlete rozdíl mezi deklarativním a procedurálním způsobem zajištění integrity. Jaký databázový objekt byste použili, pokud byste potřebovali zajistit integritu, kterou nelze pokrýt omezením CHECK (například výpočet z jiných tabulek před smazáním záznamu)?

********************************************************************************

# Řešení cvičení

**1. Definice a účel integrity** Integrita databáze označuje stav, kdy jsou uložená data po celou dobu své životnosti přesná, spolehlivá, konzistentní a jednoznačná. Zajišťuje, aby data dávala smysl a neodporovala stanoveným pravidlům. Tohoto cíle se dosahuje definováním integritních omezení (constraints) na úrovni tabulek nebo vytvořením procedurálních pravidel na úrovni databázového serveru.

**2. Entitní vs. referenční integrita** Entitní integrita se váže na primární klíč (PRIMARY KEY) a zajišťuje, že každý záznam v tabulce bude mít jedinečný identifikátor, který navíc nesmí nabývat hodnoty NULL. Referenční integrita se naproti tomu váže na cizí klíč (FOREIGN KEY) a definuje pravidla logických vazeb mezi různými tabulkami. Vynucuje pravidlo, že cizí klíč smí obsahovat pouze existující hodnoty primárních klíčů z odkazované tabulky (nebo NULL). Při porušení referenční integrity by v systému začaly vznikat takzvané "sirotčí" záznamy - data, která odkazují na nadřazený objekt, jenž byl smazán nebo vůbec neexistuje.

**3. Návrh SQL struktury**
```sql
CREATE TABLE Vozidla (
    spz VARCHAR(8) PRIMARY KEY,
    vin_kod VARCHAR(50) UNIQUE NOT NULL,
    rok_vyroby INT CHECK (rok_vyroby >= 2000),
    id_majitel INT,
    CONSTRAINT fk_majitel_vozu FOREIGN KEY (id_majitel)
        REFERENCES Majitele(id_majitel)
        ON DELETE CASCADE
);
```

**4. Deklarativní vs. procedurální integrita** Deklarativní integrita se nastavuje přímo při návrhu struktury tabulky pomocí SQL DDL příkazů. Využívá statická omezení jako UNIQUE, CHECK, PRIMARY KEY nebo FOREIGN KEY. Procedurální integrita naproti tomu využívá dynamický programový kód pro vynucení složitých firemních procesů a pravidel. V případě, že standardní CHECK nestačí (protože obvykle nemůže komunikovat s jinými tabulkami), použije se speciální objekt zvaný trigger (spoušť). Trigger dokáže zachytit událost (např. operaci DELETE) a před jejím potvrzením automaticky vyhodnotit jakkoliv složitý dotaz napříč databází k ověření, zda je smazání platné.