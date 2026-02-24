24.2.2026 – Zálohování a archivace 

Archivace 

* Proces uložení dat v co nejjednodušším formátu, nejčastěji csv (sql, json) 
* Kódování nejčastěji UTF-8 nebo Windows-1250 
* Uložení dat na dlouhou dobu (10 a více let) většinou na jiný zabezpečený server 
* Předpokladem je málo častý přístup 
* Důvodem je ukládání historických dat (možný zpětný audit, trendy...) 

Zálohování 

* Záloha je uložení dat v plném formátu na aktivně používaný server (z důvodu rychlosti obnovy) 
* Ukládání dat na krátkou dobu podle důležitosti (cennosti) dat (1 min – 1 rok) 
* Zálohuje se s určitou pravidelnou frekvencí 
* Zálohu lze také použít k archivaci, ale je to nevýhodné (velký rozsah + formát nemusí existovat – archivní soubory jako záloha nelze použít – chybí systémové soubory) 
* Pravidelné zálohy nám umožňují obnovit data po chybách úložného media (chyba disku), chybách uživatele (smazaná tabulka) nebo výpadku systému 
* Kromě záchrany dat slouží zálohy také k administrativním důvodům 
	* Audit (účetní) 
	* Úspora místa 
	* Přenos mezi různými servery 
* Zálohovat lze celou databázi, část databáze, změny v databázi nebo jednotlivé soubory a transakční log 