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
- kontroluje pravo pristupu uzivatele na dany disk (user access privileges)
**metadata cache** - paměti pro metadata (nazvy tabulek, atributu, omezeni, procedur, ..., uzivatelskych prav.. = to, co nejsou konkretni uzivatelska data) + ??? objektech
**QueryCache** - obsahuje predchozi, jiz provedene prikazy, na kterych byla provedena kontrola pomoci **parseru**
- pokud je prichozi pozadavek v te pameti, vezme si z ni a pouze se mu prida nove unikatni sql_id, ale parser udela analyzu znovu (zkrati se cas zpracovani)
=> query cache je priklad pouziti "predpripravenych dat"
= data ahead of time in anticipation of it's use
(**KeyCache**) - pamet, ktera obsahuje indexy (PKs nebo indexy vytvorene k tabulkam, ktere se zpracovavaji)
- pokud je index maly (B-strom pro vyhledavani), tak se nactou i jeho data
- pokud je index velky, ke v te pameti pouze a fdata jsou na disku v MyISAM ???F
**MyISAM** (MySQL Indexed Sequential Access Method) - je to algoritmus pristupu k indexovanym datun od firmy IBM => rychli pristup k velmi velkemu objemu dat