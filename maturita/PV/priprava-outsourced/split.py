import os
import re
from pypdf import PdfReader, PdfWriter

def split_pdf_by_mapping(pdf_path, mapping_path, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read the mapping file
    with open(mapping_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Reconstruct broken lines if a topic name spans multiple lines
    normalized_lines = []
    current_line = ""
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        # If the line does not contain '=', append it to the buffer
        if "=" not in line:
            current_line += line + " "
        else:
            current_line += line
            normalized_lines.append(current_line)
            current_line = ""

    # Open the source PDF
    try:
        reader = PdfReader(pdf_path)
        total_pages = len(reader.pages)
    except FileNotFoundError:
        print(f"Error: The file '{pdf_path}' was not found.")
        return

    # Regex to extract the topic name and page numbers
    pattern = re.compile(r'^(.*?)\s*=\s*pages?\s*(\d+)(?:-(\d+))?', re.IGNORECASE)

    # Use enumerate to assign numbers 1 through 25 to the output files
    for index, line in enumerate(normalized_lines, start=1):
        match = pattern.search(line)
        if not match:
            print(f"Could not parse line: {line}")
            continue

        topic_name = match.group(1).strip()
        
        # Remove characters that are invalid in file names
        safe_name = re.sub(r'[\\/*?:"<>|]', "", topic_name)

        start_page = int(match.group(2))
        end_page = int(match.group(3)) if match.group(3) else start_page

        # PDF pages are 0-indexed in pypdf
        start_idx = start_page - 1
        end_idx = end_page - 1

        if start_idx < 0 or end_idx >= total_pages:
            print(f"Skipping '{safe_name}': pages {start_page} to {end_page} are out of bounds.")
            continue

        writer = PdfWriter()
        for i in range(start_idx, end_idx + 1):
            writer.add_page(reader.pages[i])

        # Format page information for the filename
        if start_page == end_page:
            page_info = f"page {start_page}"
        else:
            page_info = f"pages {start_page}-{end_page}"

        # Create the new filename with zero-padded numbers (01, 02, etc.) and page info
        filename = f"{index:02d} - {safe_name} ({page_info}).pdf"
        output_path = os.path.join(output_dir, filename)
        
        with open(output_path, 'wb') as out_file:
            writer.write(out_file)

        print(f"Saved: {output_path}")

if __name__ == "__main__":
    # Define your file paths here
    PDF_FILE = "PV.pdf"
    MAPPING_FILE = "topic_mapping.txt"
    OUTPUT_DIRECTORY = "out"

    split_pdf_by_mapping(PDF_FILE, MAPPING_FILE, OUTPUT_DIRECTORY)