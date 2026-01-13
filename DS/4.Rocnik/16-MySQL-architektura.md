# 16. MySQL Architektura

## Vnitřní struktura MySQL

* Systém je velmi flexibilní a nabízí různé druhy úložišť (storage engines).
* Obsahuje velké množství pluginů, což znamená, že chování a správa dat záleží na použitém úložišti.

## MySQL fyzická architektura

* Představuje vlastní realizaci systému, tedy souborový systém.
* Architekturu dělíme na dvě hlediska:
    1.  **Fyzické hledisko**: složky souborů.
    2.  **Logické hledisko**: blokové schéma zpracování připojení.

### Adresářová struktura

1.  **MySQL base directory**
    * a) **Program files** - knihovny, dokumenty, soubory pro UNIX atd.
    * b) **Executables** - spustitelné soubory jako `mysql`, `mysqld`, `mysqladmin`, `mysqldump`.

2.  **MySQL data directory**
    * a) **Systémová data** - server log file, status file, .ib log files, system tablespace.
    * b) **Data subdirectories** (pro každou databázi) - obsahují indexy + data, struktury objektů (.frm soubory) a katalogy.

![[architektura-mysql.png]]

> **Důležitá poznámka:** Buffer je větší, ale pomalejší oproti cache.

---

## Komponenty a procesy

* **klient** - aplikace, pomocí které se připojujeme k serveru.
* **server** - MySQL instrukce, kde jsou uložena data.

* **mysqld** (daemon) - program, který běží na pozadí a spravuje příchozí/odchozí požadavky.
    * Je to vícevláknový proces.
    * **Session**:
        * Je **doba** od úspěšného propojení až do ukončení spojení.
        * Po celou tuto dobu má připojení své **thread_id** (které je přiděleno mysqld).

* **parser** (analyzátor) - program, který kontroluje SQL syntaxi jednotlivých příkazů v připojeních (jedno připojení může obsahovat více příkazů) a generuje automaticky každému z těchto příkazů jedinečné **sql_id** (event_id).
    * Také kontroluje uživatelská oprávnění.

* **optimizer** - program, který připraví a potom provede 'execution plan', prováděcí plán přístupu na konkrétní storage engine (**oblast na disku**, kde jsou uložena požadovaná data).
    * Pracuje **multisessionově**, tzn. pracuje s příkazy různých sessions.
    * Query execution plan se sestavuje pro každý engine zvlášť.
    * Důvodem je, že práce s diskem je nejpomalejší.
    * Kontroluje právo přístupu uživatele na daný disk (user access privileges).

* **metadata cache** - paměť pro metadata (názvy tabulek, atributů, omezení, procedur, ..., uživatelských práv... = to, co nejsou konkrétní uživatelská data) + statistiky o objektech.

* **Query Cache** - obsahuje předchozí, již provedené příkazy, na kterých byla provedena kontrola pomocí **parseru**.
    * Pokud je příchozí požadavek v té paměti, vezme si z ní a pouze se mu přidá nové unikátní sql_id, ale parser udělá analýzu znovu (zkrátí se čas zpracování).
    * => Query cache je příklad použití "předpřipravených dat".
    * = Data ahead of time in anticipation of it's use.

* **Key Cache** - paměť, která obsahuje indexy (PKs nebo indexy vytvořené k tabulkám, které se zpracovávají).
    * Pokud je index malý (B-strom pro vyhledávání), tak se načtou i jeho data.
    * Pokud je index velký, je v té paměti pouze B-strom a data jsou na disku v MyISAM storage engine.

* **MyISAM** (MySQL Indexed Sequential Access Method) - je to algoritmus přístupu k indexovaným datům od firmy IBM => rychlý přístup k velmi velkému objemu dat.