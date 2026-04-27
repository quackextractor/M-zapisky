import os
import re

def unify_markdown_headings():
    for filename in os.listdir('.'):
        if filename.endswith('.md'):
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            new_lines = []
            has_title = False
            
            for line in lines:
                # 1. Přeskočí případný duplicitní tučný nadpis (např. u Oscara Wildea)
                if '**Šablona studijního průvodce' in line:
                    continue
                
                # 2. Sjednotí hlavní nadpis na H1
                if re.match(r'^[\s#\*]*Šablona studijního průvodce', line):
                    line = '# Šablona studijního průvodce k maturitě\n'
                    has_title = True
                
                # 3. Sjednotí číslované sekce na H2 a odstraní VŠECHNY přebytečné hvězdičky
                elif re.match(r'^[\s#\*]*\d+\.\s+', line):
                    # Změna z \*? na \** zajistí smazání všech hvězdiček na konci
                    line = re.sub(r'^[\s#\*]*(\d+\.)\s*\*?(.*?)\**\s*$', r'## \1 \2\n', line)
                
                # 4. Sjednotí podsekce (např. ČÁST A) na H3
                elif re.match(r'^[\s#\*]*ČÁST', line):
                    line = re.sub(r'^[\s#\*]*', '### ', line)
                
                new_lines.append(line)
            
            # 5. Pokud dokumentu chyběl hlavní nadpis, vloží ho na první řádek
            if not has_title:
                new_lines.insert(0, "# Šablona studijního průvodce k maturitě\n\n")
                
            # Zapíše změny zpět do souboru
            with open(filename, 'w', encoding='utf-8') as file:
                file.writelines(new_lines)
            
            print(f"Zpracován soubor: {filename}")

if __name__ == '__main__':
    unify_markdown_headings()