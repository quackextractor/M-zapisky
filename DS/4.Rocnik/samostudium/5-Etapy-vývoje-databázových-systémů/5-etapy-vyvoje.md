# Teoretický list: Etapy vývoje databázových systémů

### 1. Životní cyklus databáze (DBLC) 
Životní cyklus databáze (Database Life Cycle) popisuje celý proces od vzniku, přes používání až po konec databáze.
* Skládá se ze šesti základních fází: analýza, návrh, implementace, testování, provoz (nasazení) a údržba.
* Příčinou ukončení životního cyklu je stav, kdy se údržba systému stane finančně nebo technicky náročnější než vytvoření zcela nové databáze.
* K zániku staré databáze dochází typicky kvůli extrémnímu nárůstu objemu dat nebo potřebě integrovat zcela nové zdroje dat.
* Ukončení cyklu umožní nasadit nový systém, odstranit historické chyby, zrychlit provoz a přizpůsobit se novým požadavkům.
* Po ukončení cyklu následuje začátek vývoje nové databáze opět v první fázi analýzy.

### 2. Popis a význam jednotlivých etap vývoje

**1. Analýza**
* Jedná se o nejdůležitější fázi celého cyklu, protože rozhoduje o správném pochopení fungování organizace, jejích dat a požadavků.
* Špatná analýza nevyhnutelně vede ke špatnému návrhu a následně ke špatné databázi.
* Zahrnuje zjišťování požadavků HW a SW organizace, analýzu datových souborů a nastavení uživatelských účtů, rolí a práv prostřednictvím konzultací s firmou.
* Definuje potřebná data, jejich vzájemné vazby a datové toky, jako jsou vstupy, výstupy a transformace.
* Výsledkem této fáze je konceptuální model (například E-R diagram), který slouží jako logický most mezi uživatelem a tvůrcem databáze.

**2. Návrh (Design)**
* Fáze návrhu se rozděluje na tvorbu logického a relačního schématu.
* Logické schéma slouží k určení entit, vazeb, dekompozici vztahů M:N a zajištění normalizace (nebo případné denormalizace).
* Relační schéma již představuje konkrétní technické řešení, které neslouží pro klienta, ale pro vývojáře.
* V relačním schématu se definují konkrétní tabulky, sloupce, datové typy a technické řešení vazeb pomocí primárních (PK) a cizích (FK) klíčů.
* Nedílnou součástí je zajištění integrity databáze, zejména entitní, referenční a doménové.

**3. Implementace**
* Představuje fyzickou realizaci navržené databáze na vybraném serveru pomocí příkazů jazyka SQL, čímž se vyřeší strukturální požadavky (vytvoření tabulek).
* Zahrnuje také realizaci procedurální části, do které spadá programování objektů jako jsou pohledy (view), uložené procedury, funkce, triggery a indexy.

**4. Testování**
* Do vytvořené databáze se vloží testovací data (mock data) k ověření celkové funkčnosti.
* Ověřuje se dodržování integritních omezení, absence redundancí a správná funkce programovatelné procedurální části.
* Krok zahrnuje i testování uživatelských účtů, přístupových práv, rolí a procesů zálohování.
* Důležitou součástí je ověření výkonu databáze pod zátěží (Load testing).

**5. Nasazení do provozu (Deployment)**
* Tato fáze obnáší nahrání finální struktury databáze (provedení transakce) na produkční systém uživatele.
* Do systému se nahrají nebo importují "živá" ostrá uživatelská data.
* Následuje otestování všech funkcí v reálném ostrém provozu a konečné předání zákazníkovi.

**6. Údržba a optimalizace**
* Je nejdelší fází cyklu a řeší správu uživatelů, pravidelné zálohování a archivaci starých historických dat.
* Součástí údržby je monitorování výkonu, ladění dotazů, přidávání nových indexů a zmenšování objemu databáze.
* Během údržby se také reaguje na případné změny v business pravidlech organizace a provádí se opravy nalezených chyb.

### 3. Dokumentace: Obsah a forma
Správně vedená dokumentace je klíčová pro pochopení struktury a dlouhodobou údržbu systému. Rozděluje se na tři hlavní části:
* **Technická dokumentace (Data Dictionary):** Popisuje přesnou strukturu tabulek, definice relací a použité datové typy pro každý element.
* **Uživatelská dokumentace:** Obsahuje návody a manuály určené pro koncovou obsluhu aplikací, které jsou nad databází postavené.
* **Dokumentace změn (Versioning):** Slouží k vedení záznamů o všech úpravách databázového schématu v průběhu času.

********************************************************************************

# Cvičení k maturitní otázce

Otestujte své znalosti vypracováním odpovědí na následující otázky.

**Otázka 1: Analýza a její důležitost**
Vysvětlete, proč je fáze analýzy považována za absolutně nejdůležitější krok v celém životním cyklu databáze. Jaké konkrétní kroky se v této fázi provádějí a co je jejím hlavním výstupem?

**Otázka 2: Fáze návrhu**
Popište rozdíl mezi logickým schématem a relačním schématem, které vznikají ve fázi návrhu. Co řeší jedno a co druhé?

**Otázka 3: Konec životního cyklu**
Za jaké situace dochází k ukončení životního cyklu databáze a jaké výhody přináší nasazení zcela nového systému?

**Otázka 4: Testování systému**
Před nasazením do provozu probíhá důkladné testování. Jmenujte alespoň pět konkrétních oblastí nebo prvků databáze, které se během fáze testování musí ověřit.

**Otázka 5: Databázová dokumentace**
Pokud byste měli novému vývojáři předat hotovou databázi, do jakého typu dokumentace se bude muset podívat, aby pochopil datové typy a strukturu tabulek? Jaké další dva typy dokumentace by měly u profesionálního projektu vzniknout?

********************************************************************************

# Řešení cvičení

**Řešení 1: Analýza a její důležitost** Analýza je nejdůležitější, protože rozhoduje o správném pochopení dat, potřeb a problémů organizace. Jakákoliv chyba nebo nedorozumění v této fázi vede ke špatnému návrhu a ve výsledku ke špatně fungující databázi. V této fázi se zjišťují HW a SW požadavky, definují se datové toky (vstupy a výstupy), určují se práva a role uživatelů. Hlavním výstupem je logický konceptuální model (např. E-R diagram), který slouží jako srozumitelný most mezi zadavatelem a tvůrcem systému.

**Řešení 2: Fáze návrhu** Logické schéma je abstraktnější a zaměřuje se na určení entit, jejich vzájemných vazeb, zajištění normalizace a dekompozici složitých vztahů M:N. Neřeší konkrétní technologii. Relační schéma je naproti tomu přesné technické řešení pro vývojáře. Definuje finální tabulky, sloupce, specifické datové typy a technickou realizaci vazeb pomocí primárních (PK) a cizích (FK) klíčů pro zajištění integrity.

**Řešení 3: Konec životního cyklu** Životní cyklus databáze končí v momentě, kdy se její údržba stane finančně nebo technicky náročnější a dražší než vytvoření zcela nové databáze. K tomu typicky dochází při obrovském nárůstu objemu dat nebo při změně primárních zdrojů dat. Ukončení staré databáze a nasazení nové přináší výhodu v podobě odstranění historických chyb, zrychlení provozu a snadnější adaptaci na nové firemní požadavky.

**Řešení 4: Testování systému**
Během testování, do kterého se vkládají cvičná data (mock data), se musí ověřit:
1. Dodržování integritních omezení.
2. Absence datových redundancí.
3. Funkčnost procedurální části (triggery, uložené procedury, pohledy).
4. Uživatelské účty, přístupová práva a definované role.
5. Procesy pravidelného zálohování.
6. Výkon databáze pod zátěží (Load testing).

**Řešení 5: Databázová dokumentace** Nový vývojář se bude muset podívat do Technické dokumentace (označované také jako Data Dictionary), která detailně popisuje strukturu všech tabulek, definice relací a použité datové typy. Dále by měla u projektu vzniknout Uživatelská dokumentace (manuály pro koncové uživatele pracující s aplikací)  a Dokumentace změn (Versioning) evidující historii veškerých úprav v databázovém schématu.