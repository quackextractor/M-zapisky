## **2. krok OLAP** (Online Analytics Processing)

- Proces efektivního získávání dat z databáze.
- Používají se databáze **Data Warehouse**, **Star DB** -> všechny tyto pojmy odpovídají struktuře DB.

**Tato DB se skládá:**

- **a) z FACT tabulek:** "obsahuje klíče, které odkazují na DIM table + údaje, které lze měřit, použít atd."
- **b) z DIM tabulek:** "opakuje údaje kdo, co, kde, kdy (číselníky)"

Přechod mezi **OLTP** (plně normalizované DB) a **OLAP** (FACT + DIM tabulky) se provádí **ELT/ETL** procesy.

---

### **Př. Star DB (Útulek - Adopce zvířat)**

Jednoduché schéma, jedna faktová tabulka uprostřed, dimenze okolo (denormalizované).

``` mermaid
erDiagram
    FACT_ADOPCE {
        int ID_adopce PK
        int SK_zvire FK
        int SK_chovatel FK
        int SK_utulek FK
        int SK_novy_majitel FK
        decimal poplatek_za_adopci
        decimal naklady
        date datum_prichodu
        date datum_odchodu
        decimal zisk "vypočítané"
        int delka_pobytu "vypočítané"
    }

    DIM_ZVIRE {
        int SK_zvire PK
        string NK_cip_id
        string druh
        string rasa
    }

    DIM_CHOVATEL {
        int SK_chovatel PK
        string jmeno
    }

    DIM_UTULEK {
        int SK_utulek PK
        string nazev
    }

    DIM_NOVY_MAJITEL {
        int SK_novy_majitel PK
        string jmeno
    }

    FACT_ADOPCE }|..|| DIM_ZVIRE : "obsahuje"
    FACT_ADOPCE }|..|| DIM_CHOVATEL : "obsahuje"
    FACT_ADOPCE }|..|| DIM_UTULEK : "obsahuje"
    FACT_ADOPCE }|..|| DIM_NOVY_MAJITEL : "obsahuje"
```

**DIM T:** zvíře, chovatel, útulek, nový majitel

**FACT data:**

- poplatek za adopci
- náklady
- dat. příchodu
- dat. odchodu

**Nové atributy (vypočítané):**

- poplatek za adopci + náklady -> **zisk**
- dat. příchodu + dat. odchodu -> **délka pobytu**

---

### **Problem + Řešení**

Kdyby chyběly údaje povinné, tak data z útulku musíme poslat zpátky s chybovou hláškou. Nemůžeme si vymýšlet povinné údaje, které nám nepřišly.

---

### **!! Přímý přechod z normalizované DB do DIM tab**

Je pomocí **VIEWS**.

- **a)** View pro spojení: druh, zvíře, rasa.
- **b)** `INSERT INTO` dim_zvire tabulky.
- **c)** + Vytvoření nových unikátních **SKs** a uložení **PKs** + **NKs** k záznamu.

**OLAP používá vlastní unikátní klíče:**

- **Surrogate Keys (SKs):** Místo původních PKs.
- **Natural Keys (NKs):** Přiřazené unikátní číslo (např. rodné číslo, čip ID...).

---

### **Typy schémat v OLAP**

#### **1. Star Schema (Hvězda)**

- Viz příklad výše.
- Nejjednodušší a nejrychlejší pro dotazování.
- Dimenze jsou **denormalizované** (obsahují redundantní data, např. rasa je přímo v tabulce zvíře).

#### **2. Snowflake Schema (Vločka)**

- Varianta Star schématu, kde jsou DIM tabulky **normalizované**.
- Dimenze se větví do dalších pod tabulek (odstraňuje redundanci).
- **Př.:** `DIM_ZVIRE` neobsahuje název rasy, ale pouze `ID_RASA`, které odkazuje na novou tabulku `DIM_RASA`.
- **Nevýhoda:** Složitější dotazy (více JOINů), pomalejší výkon než Star.

Code snippet

``` mermaid
erDiagram
    FACT_ADOPCE }|..|| DIM_ZVIRE : "Foreign Key"
    DIM_ZVIRE }|..|| DIM_RASA : "Foreign Key (Normalizace)"
    DIM_RASA }|..|| DIM_DRUH : "Foreign Key (Normalizace)"

    FACT_ADOPCE {
        int ID_adopce
        int SK_zvire
        decimal zisk
    }

    DIM_ZVIRE {
        int SK_zvire
        int ID_rasa FK
        string jmeno
    }

    DIM_RASA {
        int ID_rasa
        int ID_druh FK
        string nazev_rasy
    }
    
    DIM_DRUH {
        int ID_druh
        string nazev_druhu
    }
```

#### **3. Galaxy Schema (Galaxie / Fact Constellation)**

- Obsahuje **více FACT tabulek**.
- Různé FACT tabulky sdílejí stejné DIM tabulky (**Conformed Dimensions**).
- Umožňuje sledovat více procesů najednou (např. adopce a veterinární zákroky).

Code snippet

``` mermaid
erDiagram
    FACT_ADOPCE {
        int ID_adopce
        int SK_zvire FK
        decimal poplatek
    }

    FACT_VETERINA {
        int ID_zakrok
        int SK_zvire FK
        int SK_veterinar FK
        decimal cena_lecby
    }

    DIM_ZVIRE {
        int SK_zvire
        string jmeno
    }

    DIM_VETERINAR {
        int SK_veterinar
        string specializace
    }

    FACT_ADOPCE }|..|| DIM_ZVIRE : "sdílí dimenzi"
    FACT_VETERINA }|..|| DIM_ZVIRE : "sdílí dimenzi"
    FACT_VETERINA }|..|| DIM_VETERINAR : "specifická dimenze"
```