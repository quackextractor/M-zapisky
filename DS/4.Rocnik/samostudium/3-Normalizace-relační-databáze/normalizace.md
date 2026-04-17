# Teoretický list: Normalizace relační databáze

## 1. Význam normalizace a datové anomálie Normalizace je proces úpravy struktury databáze (tabulek), aby nedocházelo k redundanci (nadbytečnosti) dat a aby byla zajištěna konzistence z hlediska jednoznačnosti při vyhledávání. Cílem tohoto procesu je snížit duplikaci dat, usnadnit celkovou údržbu systému a zabránit vzniku anomálií při úpravách, vkládání a mazání záznamů.

Chybně navržená nebo nenormalizovaná databáze trpí následujícími problémy:
 * **Redundance (Update anomálie):** Nadbytečné opakování stejných dat, které vede k problémům při aktualizaci. Změna jednoho údaje může vyžadovat úpravy na mnoha místech, což zvyšuje riziko chyb.
* **Anomálie vkládání (Insert Anomaly):** Nemožnost vložit do databáze nová data, protože chybí jiná, logicky nesouvisející data.
* **Anomálie mazání (Delete Anomaly):** Nechtěná ztráta důležitých dat při smazání jiného záznamu. Proces, kterým se rozděluje jedna široká tabulka do více menších tabulek s cílem splnit normální formy, se nazývá dekompozice. K řešení vazeb a odstraňování anomálií se určuje takzvaná funkční závislost, což je vztah, kdy hodnota jednoho atributu jednoznačně určuje hodnotu druhého atributu.

## 2. Normální formy (1. NF až 3. NF) Pro zajištění správně normalizované relační databáze se v praxi používají nejčastěji normální formy 1. NF až 3. NF.

* **1. normální forma (1. NF):** Aby byla splněna 1. NF, musí být stanoven primární klíč (je splněna takzvaná 0. NF) a zároveň musí být všechny prvky atomární. To znamená, že každé políčko tabulky obsahuje pouze jednu nerozložitelnou hodnotu a každý záznam je zcela jedinečný. Příkladem takové úpravy je rozdělení obecného sloupce "Adresa" na samostatné atomické atributy "Město", "Ulice" a "Číslo popisné".
* **2. normální forma (2. NF):** Pro splnění musí být tabulka v 1. NF a zároveň každý neklíčový atribut musí být plně závislý na celém primárním klíči. Toto pravidlo se zaměřuje na tabulky obsahující složený primární klíč (klíč skládající se ze dvou a více atributů) a odděluje částečně závislé atributy do vlastních tabulek. Pokud je primární klíč tabulky jednoduchý, je 2. NF automaticky splněna.
* **3. normální forma (3. NF):** Tabulka musí být ve 2. NF a zároveň neklíčové atributy nesmí být tranzitivně závislé na sobě navzájem. Všechny neklíčové atributy tak závisí výhradně a pouze na primárním klíči. Praktickým příkladem zavedení 3. NF je eliminace tranzitivní závislosti, kdy adresa zákazníka závisí na zákazníkovi a zákazník závisí na konkrétní objednávce.
* **Boyce-Coddova normální forma (BCNF):** Jedná se o přísnější verzi 3. NF. Její zavedení řeší problémy spojené se specifickými případy více překrývajících se kandidátních klíčů.

## 3. Normalizace vs. Denormalizace
Zatímco normalizace směřuje k odstranění duplicit, existují i situace, kdy se postupy záměrně obracejí.

* **Normalizace:** Zajišťuje databázi bez redundancí, garantuje lepší datovou integritu a nabízí jednodušší celkovou správu dat. Nevýhodou může být pomalé čtení dat a složitější tvorba statistik, protože dotazy vyžadují náročné spojování tabulek. Normalizace je základním pilířem pro systémy OLTP (Online Transaction Processing) pro běžný provoz.
* **Denormalizace:** Jedná se o záměrné porušení pravidel normalizace za účelem radikálního zrychlení čtení dat a zjednodušení složitých dotazů. Databáze může vědomě obsahovat duplikovaná data nebo předem spočítané hodnoty pomocí agregačních funkcí (například cena celkem), čímž se zrychlí výpisy a eliminují se složité spoje (JOIN). Nevýhodou denormalizace je zvýšené riziko nekonzistentních dat, tvorba redundancí a větší nároky na úložný prostor disku. Je typická pro analytické datové sklady (systémy OLAP).

---

# Cvičení k maturitní otázce: Normalizace databáze

**Otázka 1: Analýza anomálií a redundance**
Vysvětlete, proč se v praxi provádí normalizace databáze a jaké tři konkrétní datové anomálie tento proces odstraňuje. Popište každou anomálii na základě definic.

**Otázka 2: Aplikace normálních forem (1. NF)**
Představte si návrh tabulky `Zaměstnanci`, která obsahuje sloupce: `ID`, `Jméno_a_příjmení` a `Telefonní_čísla`. Vysvětlete, proč tato tabulka nesplňuje 1. normální formu a popište konkrétní postup, jak ji do 1. NF správně převést.

**Otázka 3: Pochopení 2. a 3. normální formy**
Jaký je hlavní rozdíl mezi 2. a 3. normální formou z hlediska závislosti atributů na klíčích? Uveďte, v jakém specifickém případě databázového návrhu je 2. normální forma splněna automaticky.

**Otázka 4: Denormalizace v praxi**
Vysvětlete, z jakého důvodu bychom se rozhodli databázi úmyslně denormalizovat. Jaké konkrétní výhody a nevýhody tento postup přináší a do jakých typů systémů (OLTP nebo OLAP) je denormalizace vhodná?

---

# Řešení cvičení

**Řešení 1: Analýza anomálií a redundance** Normalizace se provádí za účelem minimalizace nadbytečného opakování dat (redundance) a zajištění konzistence databáze. Tento proces odstraňuje následující datové anomálie:
 * **Anomálie vkládání (Insert Anomaly):** Vzniká v situaci, kdy databázový systém nedovolí vložit nový záznam, protože k němu chybí jiná, avšak logicky nesouvisející data.
* **Anomálie mazání (Delete Anomaly):** Označuje ztrátu důležitých a nesouvisejících dat, ke které dojde nechtěně při smazání jiného primárního záznamu.
* **Redundance (Update Anomaly):** Je nadbytečné opakování dat, které ztěžuje úpravy. Změna jednoho údaje (například adresy oddělení) si následně žádá změnu na mnoha místech současně, jinak systém ztratí konzistenci.

**Řešení 2: Aplikace normálních forem (1. NF)** Zmíněná tabulka nesplňuje 1. normální formu (1. NF), protože hodnoty ve sloupcích nejsou atomické neboli nerozložitelné. Sloupec `Jméno_a_příjmení` obsahuje logicky více údajů v jedné buňce a sloupec `Telefonní_čísla` naznačuje přítomnost více záznamů o číslech pro jednoho zaměstnance.
Řešení spočívá v úpravě a dekompozici:
* Atribut `Jméno_a_příjmení` se musí rozdělit na dva samostatné atributy `Jméno` a `Příjmení`.
* Pro telefonní čísla je vhodné vytvořit novou nezávislou tabulku (např. `Telefony`), která se propojí se zaměstnancem pomocí cizího klíče a zachová tak jedinečnost a atomicitu jednotlivých záznamů bez omezování jejich počtu.

**Řešení 3: Pochopení 2. a 3. normální formy**
Hlavní rozdíl spočívá v typu závislosti neklíčových atributů. Ve 2. normální formě se vyžaduje, aby byl každý neklíčový atribut plně závislý na celém primárním klíči, čímž se řeší a odstraňují částečné závislosti v případech, kdy je primární klíč složený z více sloupců. Ve 3. normální formě se naopak řeší vztahy mezi samotnými neklíčovými atributy, které nesmí být tranzitivně závislé na sobě navzájem, ale musí záviset pouze na samotném primárním klíči. Z toho vyplývá, že 2. normální forma je splněna zcela automaticky tehdy, pokud má tabulka jednoduchý (nesložený) primární klíč.

**Řešení 4: Denormalizace v praxi** Databázi úmyslně denormalizujeme s cílem maximalizovat rychlost čtení dat a zjednodušit složité výpisy. Vkládáním redundantních dat se vyhneme nutnosti spojovat při vyhledávání velké množství tabulek.
* **Výhody:** Velmi rychlé čtení rozsáhlých dat a okamžitý přístup k předem spočítaným agregovaným hodnotám.
* **Nevýhody:** Zvýšené nároky na úložný prostor z důvodu redundance, obtížnější správa a s tím spojené riziko tvorby nekonzistentních dat při úpravách.
* **Využití:** Denormalizace dat je zcela typická a žádoucí pro analytické datové sklady v rámci systémů OLAP, zatímco striktní normalizace je vyhrazena pro běžné provozní systémy OLTP.