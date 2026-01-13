klient - app, pomocí které se připojujeme k serveru
server - MySQL instrukce, kde jsou uložena data

**mysqld** (daemon) - program, který běží na pozadí a spravuje příchozí/odchozí požadavky
- je to více vláknový proces
- session 
	- je **doba** od úspěšného propojeni až do ukončeni spojeni
	- po celou tuto dobu ma připojení své **thread_id** (které je přiděleno mysqld)
**parser** (analyzátor) - program, který kontroluje SQL syntaxi jednotlivých příkazu v připojeních (jedno připojení může obsahovat vice příkazu) a generuje automaticky kazdemu  techto prikazu jedinečné **sql_id** (event_id)
- take kontroluje uživatelská oprávněni
**optimizer** - program, který přípravy a potom provede 'execution plan', prováděcí plan přístupu na konkrétní storage engine (**oblast na disku**, kde jsou uložena požadovaná data)
- pracuje **multisessionově**, tzn. pracuje s příkazy různých sessions
- query execution plan se sestavuje pro každý engine zvlášť
- důvodem je, ze práce s diskem je nejpomalejší
- kontroluje právo přístupu uživatele na daný disk (user access privileges)
**metadata cache** - paměti pro metadata (názvy tabulek, atributu, omezeni, procedur, ..., uživatelských prav.. = to, co nejsou konkrétní uživatelská data) + ??? objektech
**Query Cache** - obsahuje předchozí, již provedené příkazy, na kterých byla provedena kontrola pomoci **parseru**
- pokud je příchozí požadavek v té paměti, vezme si z ni a pouze se mu přidá nove unikátní sql_id, ale parser udělá analýzu znovu (zkrátí se čas zpracovaní)
=> query cache je příklad použití "předpřipravených dat"
= data ahead of time in anticipation of it's use
(**Key Cache**) - paměť, která obsahuje indexy (PKs nebo indexy vytvořené k tabulkám, které se zpracovávají)
- pokud je index malý (B-strom pro vyhledávaní), tak se načtou i jeho data
- pokud je index velký, ke v té paměti pouze b-strom a data jsou na disku v MyISAM ???
**MyISAM** (MySQL Indexed Sequential Access Method) - je to algoritmus přístupu k indexovaným datům od firmy IBM => rychli přístup k velmi velkému objemu dat