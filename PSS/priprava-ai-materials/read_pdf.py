import argparse
from pypdf import PdfReader

def extract_text(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract text from PDF')
    parser.add_argument('path', help='Path to PDF file')
    args = parser.parse_args()
    print(extract_text(args.path))
