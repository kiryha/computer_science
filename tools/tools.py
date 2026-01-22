"""
Convert list of MD files to single PDF.
"""
import markdown
import pdfkit

# CONFIGURATION
OUTPUT_FILE = 'book/Computer Science Made Simple.pdf'
WKHTMLTOPDF_PATH = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

LIST_OF_FILES = [
    'book_src/title.md',
    'book_src/intro.md',
    'book_src/table_of_content.md',
    'book_src/Part_1_PR.md',
]

PDF_OPTIONS = {
    'page-width': '210mm',
    'page-height': '275mm',
    'margin-top': '15mm',
    'margin-bottom': '15mm',
    'margin-left': '15mm',
    'margin-right': '15mm',
    'dpi': '300',
}

#  STYLES 
CSS = """
body { font-family: "Segoe UI", Helvetica, Arial, sans-serif; font-size: 11pt; line-height: 1.6; color: #333; }
h1 { font-size: 24pt; font-weight: 600; margin-top: 20px; }
h2 { font-size: 18pt; font-weight: 600; margin-top: 25px; }
h3 { font-size: 14pt; font-weight: 600; }
ul, ol { margin-left: 30px; padding-left: 20px; }
li { margin-bottom: 6px; }
code { background: #f4f4f4; padding: 2px 5px; font-family: Consolas, monospace; }
strong { font-weight: 600; }
em { font-style: italic; }

/* Page breaks between files */
.page-break { page-break-after: always; }

/* Title page centering */
.title-page { display: table; width: 100%; height: 800px; text-align: center; }
.title-page-inner { display: table-cell; vertical-align: middle; }
.title-page h1 { font-size: 36pt; border: none; }
"""

#  CONVERTER 
def convert_md_to_pdf(files, output):
    config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
    
    html_parts = []
    for i, f in enumerate(files):
        with open(f, encoding='utf-8') as file:
            content = markdown.markdown(file.read(), extensions=['fenced_code', 'tables'])
            if i == 0:  # Title page
                content = f'<div class="title-page"><div class="title-page-inner">{content}</div></div>'
            html_parts.append(content)
    
    body = '<div class="page-break"></div>'.join(html_parts)
    html = f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'
    
    pdfkit.from_string(html, output, configuration=config, options=PDF_OPTIONS)
    print(f">> Created: {output}")


if __name__ == '__main__':
    convert_md_to_pdf(LIST_OF_FILES, OUTPUT_FILE)
