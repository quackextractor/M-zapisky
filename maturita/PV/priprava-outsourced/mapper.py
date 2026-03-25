import fitz  # PyMuPDF
import re
import unicodedata

# Updated list based on actual PDF text
TARGET_TOPICS = [
    "Adresování a správa paměti",
    "Algoritmizace - Grafy, Prohlédávání", 
    "Algoritmizace - Rekurze, Brute Force",
    "Anonymní metody (Lambda)",
    "Architectural design patterns",
    "Asymptotické paměťové a časové",
    "Datové typy, Generika",
    "Dědičnost, method overriding",
    "Integrita dat, Kontrola vstupu", 
    "Komunikace s databázovým systémem",
    "Komunikace v síti",
    "Metodiky a životní cyklus",
    "Návrhové vzory",
    "Principy objektového programování",
    "Programovací jazyky",
    "Soubory a serializace",
    "Strojové učení - Příprava dat",
    "Strojové učení s využitím regrese", 
    "Strojové učení s využitím umělých",
    "Testování, Unit testování",
    "Typy datových struktur",
    "Vlákna, Paralelní",
    "Vlastnosti datových struktur",
    "Výjimky a aserce",
    "Zpracování a parsování"
]

def normalize(text):
    """Removes spaces, numbers, punctuation, and ALL accents/diacritics."""
    # Strip accents
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    # Remove non-words and numbers, lowercase
    return re.sub(r'[\W\d_]+', '', text).lower()

def map_pdf_chronologically(pdf_path, topics, output_filename="topic_mapping.txt"):
    doc = fitz.open(pdf_path)
    
    full_text = ""
    page_map = []
    
    # Step 1: Build the massive continuous string and the page map
    for page_num in range(len(doc)):
        text = doc.load_page(page_num).get_text()
        norm_text = normalize(text)
        
        full_text += norm_text
        page_map.extend([page_num + 1] * len(norm_text))

    # Step 2: Find where each topic starts
    found_topics = []
    missing_topics = []
    
    for original_topic in topics:
        norm_topic = normalize(original_topic)
        char_index = full_text.find(norm_topic)
        
        if char_index != -1:
            start_page = page_map[char_index]
            found_topics.append({
                "topic": original_topic,
                "start_page": start_page,
                "index": char_index
            })
        else:
            missing_topics.append(original_topic)

    # Step 3: Sort topics by where they appear
    found_topics = sorted(found_topics, key=lambda x: x["index"])
    
    # Step 4: Calculate the page ranges and format the output
    output_lines = []
    output_lines.append("### Clean Topic Mapping ###\n")
    
    for i in range(len(found_topics)):
        current = found_topics[i]
        
        if i < len(found_topics) - 1:
            next_topic = found_topics[i+1]
            end_page = next_topic["start_page"] - 1
        else:
            end_page = len(doc)
            
        if current["start_page"] >= end_page:
            output_lines.append(f"{current['topic']} = page {current['start_page']}")
        else:
            output_lines.append(f"{current['topic']} = pages {current['start_page']}-{end_page}")

    if missing_topics:
        output_lines.append("\n### Topics Not Found (Check for severe typos in PDF) ###")
        for t in missing_topics:
            output_lines.append(f"- {t}")

    final_output = "\n".join(output_lines)
    
    # Print to the console
    print(final_output)
    
    # Save to the text file
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(final_output)
        
    print(f"\nOutput successfully saved to '{output_filename}'")

if __name__ == "__main__":
    pdf_file = "PV.pdf"
    
    try:
        map_pdf_chronologically(pdf_file, TARGET_TOPICS)
    except Exception as e:
        print(f"An error occurred: {e}")