"""
Convert list of MD files to single PDF. Adjust CSS below for styling.
"""


import markdown
from xhtml2pdf import pisa

list_of_files = ['book_src/table_of_content.md', 'book_src/intro.md', 'book_src/Part_1.md']
output_file = 'book/Computer Science For Kids.pdf'

# Combine all MD files
md_content = ""
for f in list_of_files:
    with open(f, encoding='utf-8') as file:
        md_content += file.read() + "\n\n"

# Convert to HTML with styling
html = f"""
<html><head><style>
    body {{ font-family: Georgia; font-size: 12pt; line-height: 1.6; margin: 40px; }}
    h1 {{ font-size: 24pt; }}
    h2 {{ font-size: 18pt; }}
    code {{ background: #f4f4f4; padding: 2px 5px; }}
</style></head>
<body>{markdown.markdown(md_content, extensions=['fenced_code', 'tables'])}</body></html>
"""

with open(output_file, "wb") as pdf:
    pisa.CreatePDF(html, dest=pdf)
    print(f"Created: {output_file}")
