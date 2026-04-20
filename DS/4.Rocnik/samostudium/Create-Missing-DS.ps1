# 1. Delete the mangled folders (folders starting with 6- through 25-)
6..25 | ForEach-Object { Get-ChildItem -Directory -Filter "$($_)-*" | Remove-Item -Recurse -Force }

# 2. Force PowerShell console to handle UTF-8 correctly
[console]::InputEncoding = [console]::OutputEncoding = New-Object System.Text.UTF8Encoding

# 3. Create the correct folders and files
$topics = @(
    @{"folder"="6-Úpravy-a-údržba-dat-v-databázi"; "file"="6-upravy-a-udrzba.md"},
    @{"folder"="7-Zálohování-a-archivace-dat"; "file"="7-zalohovani-a-archivace.md"},
    @{"folder"="8-Export-Import-dat-z-databáze"; "file"="8-export-import.md"},
    @{"folder"="9-Architektura-databázových-systémů"; "file"="9-architektura.md"},
    @{"folder"="10-Bezpečnost-databázového-systému"; "file"="10-bezpecnost.md"},
    @{"folder"="11-Jazyk-SQL-DDL-DML-příkazy"; "file"="11-sql-ddl-dml.md"},
    @{"folder"="12-Vnořené-dotazy"; "file"="12-vnorene-dotazy.md"},
    @{"folder"="13-Transakce-a-transakční-zpracování"; "file"="13-transakce.md"},
    @{"folder"="14-Indexy"; "file"="14-indexy.md"},
    @{"folder"="15-Datové-sklady"; "file"="15-datove-sklady.md"},
    @{"folder"="16-Vizualizace-dat"; "file"="16-vizualizace.md"},
    @{"folder"="17-Uložené-procedury-a-funkce"; "file"="17-procedury-a-funkce.md"},
    @{"folder"="18-Triggery"; "file"="18-triggery.md"},
    @{"folder"="19-Pokročilé-modelování"; "file"="19-pokrocile-modelovani.md"},
    @{"folder"="20-Business-Intelligence"; "file"="20-business-intelligence.md"},
    @{"folder"="21-Relační-modely-hierarchických-struktur"; "file"="21-hierarchicke-struktury.md"},
    @{"folder"="22-Správa-serveru-Microsoft-SQL-Server"; "file"="22-sprava-mssql.md"},
    @{"folder"="23-Správa-serveru-Oracle"; "file"="23-sprava-oracle.md"},
    @{"folder"="24-Správa-serveru-MySQL"; "file"="24-sprava-mysql.md"},
    @{"folder"="25-SQL-datové-typy-v-různých-databázových-prostředích"; "file"="25-sql-datove-typy.md"}
)

foreach ($topic in $topics) {
    if (-not (Test-Path -Path $topic.folder)) {
        New-Item -ItemType Directory -Path $topic.folder | Out-Null
    }
    
    $filePath = Join-Path -Path $topic.folder -ChildPath $topic.file
    if (-not (Test-Path -Path $filePath)) {
        New-Item -ItemType File -Path $filePath | Out-Null
    }
}

Write-Host "Cleanup and recreation complete."