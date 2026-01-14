"""
Convert list of MD files to single PDF.
"""
import markdown
import pdfkit

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

list_of_files = ['book_src/table_of_content.md', 'book_src/intro.md', 'book_src/Part_1.md']
output_file = 'book/Computer Science For Kids.pdf'

def convert_md_to_pdf(list_of_files, output_file):
    # Combine all MD files
    md_content = ""
    for f in list_of_files:
        with open(f, encoding='utf-8') as file:
            md_content += file.read() + "\n\n"

    # Convert to HTML with nice styling
    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
body {{ font-family: "Segoe UI", Helvetica, Arial, sans-serif; font-size: 11pt; line-height: 1.6; color: #333; }}
h1 {{ font-size: 24pt; font-weight: 600; margin-top: 20px; }}
h2 {{ font-size: 18pt; font-weight: 600; margin-top: 25px; }}
h3 {{ font-size: 14pt; font-weight: 600; }}
ul, ol {{ margin-left: 15px; padding-left: 15px; }}
li {{ margin-bottom: 4px; }}
code {{ background: #f4f4f4; padding: 2px 5px; font-family: Consolas, monospace; }}
strong {{ font-weight: 600; }}
em {{ font-style: italic; }}
</style></head>
<body>{markdown.markdown(md_content, extensions=['fenced_code', 'tables'])}</body></html>"""

    options = {'margin-top': '15mm', 'margin-bottom': '15mm', 'margin-left': '15mm', 'margin-right': '15mm'}
    pdfkit.from_string(html, output_file, configuration=config, options=options)
    print(f">> Created: {output_file}")

convert_md_to_pdf(list_of_files, output_file)