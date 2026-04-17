## Teoretický list: Modelování relační databáze
#### 2) Modelování relační databáze - základní pojmy a terminologie, konceptuální vs relační model, identifikace vztahů, konvence ER diagramu v prostředí Oracle DataModeler

### 1. Základní pojmy a terminologie
* **Entita:** Objekt reálného světa, o kterém chceme uchovávat data (např. Zákazník, Kniha, Zaměstnanec). V relačním modelu se z ní stává **tabulka**.
* **Atribut:** Vlastnost dané entity (např. Jméno, Cena, Datum_narozeni). V relačním modelu se z něj stává **sloupec**.
* **Záznam (N-tice):** Konkrétní instance entity s vyplněnými hodnotami atributů. V databázi tvoří jeden **řádek** tabulky.
* **Primární klíč (Primary Key - PK):** Atribut (nebo skupina atributů), který jednoznačně identifikuje každý záznam v tabulce. Nesmí obsahovat prázdné hodnoty (NULL) a musí být unikátní (např. Rodne_cislo, ID_zakaznika).
* **Cizí klíč (Foreign Key - FK):** Atribut v jedné tabulce, který odkazuje na primární klíč v jiné tabulce. Slouží k vytvoření a vynucení propojení (vztahu) mezi daty.
* **Doména:** Množina všech povolených hodnot pro daný atribut (např. datový typ VARCHAR pro text, INT pro celá čísla).

### 2. Konceptuální vs. Relační model
Návrh databáze probíhá ve fázích. Nejprve se tvoří konceptuální model, poté relační (logický) a nakonec fyzický.

**Konceptuální model:**
* **Účel:** Slouží k zachycení byznys požadavků a logiky. Je srozumitelný i pro netechnické lidi (zákazníky, manažery).
* **Prvky:** Entity, atributy, vztahy (relace).
* **Vlastnosti:** Je nezávislý na konkrétním databázovém systému (nezajímá nás, zda to bude Oracle, MySQL nebo PostgreSQL). Povoluje existenci vztahů M:N (mnoho ku mnoha). Neřeší přesné datové typy.

**Relační (Logický) model:**
* **Účel:** Převádí konceptuální model do struktury relační databáze podle matematických pravidel relační algebry.
* **Prvky:** Tabulky, sloupce, primární klíče, cizí klíče.
* **Vlastnosti:** Vztahy M:N z konceptuálního modelu musí být rozbity pomocí takzvané vazební (asociační) tabulky na dva vztahy 1:N. Definuje se zde normální forma databáze (normalizace).

### 3. Identifikace vztahů a kardinalita
Vztah definuje, jak spolu entity souvisí. Kardinalita určuje číselné vyjádření tohoto vztahu (kolik instancí jedné entity může být přiřazeno k instancím druhé entity).

* **1:1 (Jedna ku jedné):** Jeden záznam v entitě A odpovídá maximálně jednomu záznamu v entitě B a naopak. (Příklad: Občan a Občanský_průkaz).
* **1:N (Jedna ku mnoha):** Jeden záznam v entitě A může odpovídat více záznamům v entitě B, ale záznam v entitě B odpovídá pouze jednomu záznamu v entitě A. Jedná se o nejběžnější typ vztahu. (Příklad: Zákazník a Objednávka - zákazník může mít více objednávek, ale objednávka patří jen jednomu zákazníkovi).
* **M:N (Mnoho ku mnoha):** Více záznamů v entitě A může odpovídat více záznamům v entitě B. (Příklad: Student a Předmět - student studuje více předmětů a předmět je studován více studenty).
* **Opcionalita (Povinnost vztahu):** Určuje, zda vztah musí existovat.
    * **Mandatory (Povinný):** Zaměstnanec MUSÍ patřit do nějakého Oddělení.
    * **Optional (Volitelný):** Zaměstnanec MŮŽE řídit auto (ale nemusí).

### 4. Konvence ER diagramu v prostředí Oracle Data Modeler
Oracle SQL Developer Data Modeler (SDDM) používá pro konceptuální model standardně **Barkerovu notaci**.

**Základní znaky Barkerovy notace v SDDM:**
* **Entita:** Zobrazuje se jako zaoblený obdélník.
* **Atributy a jejich typy:**
    * `#` (Křížek): Unikátní identifikátor (UID - budoucí primární klíč).
    * `*` (Hvězdička): Povinný atribut (Mandatory - v DB to bude NOT NULL).
    * `o` (Kolečko): Volitelný atribut (Optional - v DB to může být NULL).
* **Vztahy (Čáry a konce):**
    * **Plná čára:** Povinný vztah pro danou stranu (entita "musí" mít vztah).
    * **Přerušovaná čára:** Volitelný vztah pro danou stranu (entita "může" mít vztah).
    * **Rozvětvená čára (tzv. Crow's foot / Kohoutí stopa):** Označuje stranu "N" (mnoho).
    * **Rovná čára bez rozvětvení:** Označuje stranu "1" (jedna).

********************************************************************************

## Praktické cvičení: Návrh E-shopu

**Zadání (Byznys případ):**
Firma požaduje vytvoření databáze pro malý e-shop.
1. Systém musí evidovat zákazníky. U každého zákazníka potřebujeme znát jeho unikátní číslo (ID), jméno, email a volitelně i telefonní číslo.
2. Zákazníci mohou vytvářet objednávky. Zákazník může mít více objednávek. Objednávka vždy patří právě jednomu zákazníkovi. Každá objednávka má své číslo (ID) a datum vytvoření.
3. Objednávka obsahuje konkrétní produkty. Jedna objednávka může obsahovat více různých produktů a jeden produkt se může nacházet ve více různých objednávkách.
4. U produktu evidujeme jeho kód (ID), název a aktuální cenu.

### Úkol 1: Konceptuální modelování
Na základě zadání identifikujte:
* Všechny entity a jejich atributy.
* Určete u atributů, zda se jedná o UID (#), povinný (*) nebo volitelný (o) atribut.
* Popište vztahy mezi entitami a jejich kardinalitu.

### Úkol 2: Relační modelování
Převeďte váš konceptuální návrh z Úkolu 1 do relačního modelu. Zaměřte se na vyřešení problému s M:N vazbou. Vypište výsledné tabulky, jejich primární klíče (PK) a cizí klíče (FK).

---

## Řešení praktického cvičení

### Řešení Úkolu 1 (Konceptuální model):
**Entity a Atributy v Barkerově notaci:**
* **Zákazník:**
    * `#` ID_zakaznika
    * `*` Jmeno
    * `*` Email
    * `o` Telefon
* **Objednávka:**
    * `#` ID_objednavky
    * `*` Datum_vytvoreni
* **Produkt:**
    * `#` Kód_produktu
    * `*` Nazev
    * `*` Cena

**Vztahy:**
* **Zákazník a Objednávka:** Vztah 1:N. Zákazník může mít více objednávek (přerušovaná čára u zákazníka, rozvětvená u objednávky). Objednávka musí patřit jednomu zákazníkovi (plná čára u objednávky, nerozvětvená u zákazníka).
* **Objednávka a Produkt:** Vztah M:N. Objednávka obsahuje více produktů. Produkt může být ve více objednávkách.

### Řešení Úkolu 2 (Relační model):
Pro relační model musíme rozbít M:N vazbu mezi Objednávkou a Produktem přidáním asociační (vazební) tabulky. Tím vzniknou tři entity (tabulky):

1.  **Tabulka ZAKAZNIK**
    * `ID_zakaznika` (PK)
    * `Jmeno`
    * `Email`
    * `Telefon` (může být NULL)

2.  **Tabulka PRODUKT**
    * `Kod_produktu` (PK)
    * `Nazev`
    * `Cena`

3.  **Tabulka OBJEDNAVKA**
    * `ID_objednavky` (PK)
    * `Datum_vytvoreni`
    * `ID_zakaznika` (FK odkazující do tabulky ZAKAZNIK)

4.  **Tabulka POLOZKA_OBJEDNAVKY** (Vazební tabulka pro vyřešení M:N vztahu)
    * `ID_objednavky` (PK a zároveň FK odkazující do tabulky OBJEDNAVKA)
    * `Kod_produktu` (PK a zároveň FK odkazující do tabulky PRODUKT)
    * *(Složený primární klíč se skládá z ID objednávky a Kódu produktu, což zajišťuje, že v jedné objednávce nebude jeden produkt zapsán na více řádcích. Případně sem lze přidat sloupec jako 'Množství').*