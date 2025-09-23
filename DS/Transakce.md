## Implementace
Realizují se 2 způsoby:
- pomocí transakčního protokolu
- multigenerační

Transakční protokol je soubor dat, ve kterém má server uložené transakce a jejich průběh.
- s jehož pomocí lze vrátit vše do konzistentního stavu po pádu OS a nebo selhání HW
- k zajištění konzistenci dat se používají zámky (LOCKS) na úrovni  tabulky/záznamu -> musíme zajistit, že někdo jiný zároveň do databáze nepíše
- zamykání znamená, že se jiným transakcím znemožní práce s daty, které právě používá právě probíhající transakce, což vede k řazením transakcí do fronty a zpomalením paralelního zpracování
V paralelním spracování se řeší:
- způsoby zamikání
- vstupní izolovanosti

Filozofie zamikání se dále dělí na:
- optimistický způsob
- pesimistický způsob

U optimistické filozofie se předpokládá že ve většině případů nebude docházet ke konfliktům při přístupu k konkurenčním datům.

**Deadlock** - Transakce čekají na vzájem na zdroje, které jsou blokovány. Závislost do kruhu 
- řeší se to pomocí Timeout

Pesimistický způsob:
- zamiká data i ke čtení, záleží na vstupní situaci


