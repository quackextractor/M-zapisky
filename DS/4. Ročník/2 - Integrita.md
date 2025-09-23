# Integrita db, integritní omezení

**integrita databáze** = jednoznačnost, konzistence, spolehlivost db

Zajištujeme pomocí **integritních omezení**

1. **Entitní integritní omezení** = PK. PK je NOT NULL, jednoznačně popisuje každý záznam v dané entitě
2. **Referenční integritní omezení** = každá entita na straně N musí mít atribut, který obsahuje některou z hodnot PK na straně 1 ??? je NULL, nemusí být unikátní. 
   Pokud nastavena referenční integrita tak defaultní **nelze smazat** **záznam ze strany 1** pokud odkazuje na **záznam na straně N** (lze to povolit např. **ON CASCADE**)
3. **Doménové integritní omezení**  = omezení některých atributů:
- datový typ
- rozsah
- NOT NULL
- UNIQUE
- CHECK