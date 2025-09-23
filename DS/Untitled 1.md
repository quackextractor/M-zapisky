| Vlastnost        | Shlukovaný index (Clustered)                  | Neshlukovaný index (Non-Clustered)                            |
| ---------------- | --------------------------------------------- | ------------------------------------------------------------- |
| Uložení dat      | Data jsou fyzicky seřazena podle klíče indexu | Uchovává samostatnou strukturu s ukazateli na řádky v tabulce |
| Počet indexů     | Pouze 1 na tabulku                            | Více na tabulku                                               |
| Rychlost         | Rychlejší při rozsahových dotazech a třídění  | Vhodnější pro rychlé vyhledání konkrétních atribut            |
| Dopad na tabulku | Mění fyzické uspořádání záznamů v tabulce     | Nemění fyzické uspořádání, přidává pouze další strukturu      |
| Paměť            | Vyžaduje méně paměti (menší nadstavba)        | Vyžaduje více paměti pro strukturu                            |
