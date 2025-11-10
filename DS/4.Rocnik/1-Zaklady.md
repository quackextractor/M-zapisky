# 1. Základy

**Relační databáze** - popis, terminologie, modelování rel. db.
	rel. db. architektura klient-server

![[Image1DS.png]]

**klient** - program např. v C#, Java, web. stránka, management studio, příkazový řádek

**databáze** - úložiště obsahující data a metadata
	data - **uživatelské hodnoty**
	metadata - strukturovaná data např. atributy, omezení atd.

**managment studio** 
- "zapouzdřuje" databázi, tzn. tvoří **rozhraní** pro přístup k úložišti, k datům přistupujeme pouze pomocí SQL
- zabezpečuje databázi ... hlídá práva a oprávnění přístupu k datům
-  řeší multitaskingový přístup
- transakční zpracování a úrovni izolace

### Terminologie
**Entita** - soubor objektů stejného typu
**Atribut** - vlastnost entity
**Instance, záznam** - konkrétní jeden objekt

**Relace** - vztahy mezi entitami se popisují pomoci:
1. **Kardinality** - četnost ve vztahu = kolik záznamů odpovídá jednomu záznamu v dané tabulce (a naopak) -> typy: 1:1, 1:N, M:N
2. **Parcialita** - povinnost ve vztahu může/musí
3. **Stupeň vazby** 
	a) stupeň 1 ... jedna entita ve vazbě (self-reference)
	b) stupeň 2 ...dvě entity, klasický vztah dvou entit (i vztah M:N)
	c) stupeň 3 a více ... 3 a více entit ve vztahu
	
![[Image2DS.png]]

**Primární klíč**, **Cizí klíč**: technicky realizují vazby v databázi


