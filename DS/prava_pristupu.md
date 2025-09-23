Po instalaci MSSQL se nalézá pouze uživatel SA s heslem, které jste mu určili během instalace. 
Pokud chceme užívat jiné Databáze, chceme přidělit nové uživatelé, hesla a přidělit jim přístupová práva.

Přihlášení probíhá na úrovní serveru, ale uživatele se vytváří na úrovni databáze.
- Přihlášení ---
- Oprávnění uvnitř Databáze se udělují uživatelům databáze

Přihlášení musí být namapováno na uživatelé databáze, aby se k ní mohl někdo připojit. Pokud není namapováno na žádného uživatele databáze, pořád se můžete připojit na instanci databáze, ale nemáte přístup k žádným objektům databázi.

```sql
-- DB = AAA
-- User: 'readingUser'
-- Password: 'read'

create login readingUser with password = 'read',
password_policy = OFF;
user readingUser for login readingUser,
alter login readingUser
	with default_database = AAA;
grant select on osoby to readingUser;
revoke select on osoby from readingUser;
```