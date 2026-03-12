# 10.3.2026: SQL-DDL, role, účty, oprávnění, práva

* Lze přidělit roli **serverovou** nebo nechat **public** (přístup na server)
* Lze přidat roli **databázovou** nebo nechat **public** (přístup do databáze)
* Pokud někdo má roli pouze **public**, lze mu nechat pouze velmi omezená práva a oprávnění
* Pomocí grant...
* **Oprávnění:** dám uživateli možnost provádět určitou činnost (DML, DDL)
* **Právo:** práce s určitým objektem (tabulkou, view, procedura, ...)


* Pokud je přidělena db role např. **db_datareader**, **db_datawriter** ... platí vždy pro všechny objekty
* **Přidělení oprávnění pomocí DCL**
* Př.: `GRANT select TO <user>;`
* `DENY view ANY DATABASE TO <user>;`


* Přidělujeme práva co nejmenší = lepší zabezpečení
* MySQL je pouze jeden stupeň pro přístup na server k databázi = **account = login = user**
* **Vytvoření "uživatelů"**
* `CREATE USER 'username'@'ip' IDENTIFIED BY 'password'`


* **Smazání**
* `DROP USER 'username'@'ip'`


* Vytvořením "uživatele" u MySQL zajistíme **přístup na server**
* Dál pak vybíráme buď:
* Administrátorské (serverové) role: stejné jako na MSSQL a je u nich vidět, jaká práva umožňují
* Nebo vybrat konkrétní db/všechny db a nastavit k nim určitá práva => neexistují databázové role