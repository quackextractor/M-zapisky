klient - app, pomocí které se připojujeme k serveru
server - MySQL instrukce, kde jsou uložena data

**mysqld** (daemon) - program, který běží na pozadí a spravuje příchozí/odchozí požadavky
- je to vícevláknový proces
- session 
	- je **doba** od úspěšného propojeni až do ukončeni spojeni
	- po celou tuto dobu ma připojení své **thread_id** (které je přiděleno mysqld)
**parser** (analyzátor) - program, který kontroluje SQL syntaxi jednotlivých příkazu v připojeních (jedno připojení může obsahovat vice příkazu) a generuje automaticky kazdemu  techto prikazu jedinečné **sql_id** (event_id)
- take kontroluje uživatelská oprávněni
**optimizer** - program, který přípravy a potom provede 'execution plan', prováděcí plan přístupu na konkrétní storage engine (**oblast na disku**, kde jsou uložena požadovaná data)
- pracuje **multisessionove**, tzn. pracuje s příkazy různých sessions
- query execution plan se sestavuje pro každý engine zvlášť
- důvodem je, ze práce s diskem je nejpomalejší