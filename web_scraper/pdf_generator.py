```python
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Web Scraper Report', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def generate_pdf(data):
    pdf = PDF()
    pdf.add_page()

    for link, summary in data.items():
        pdf.chapter_title(link)
        pdf.chapter_body(summary)

    pdf.output('web_scraper_report.pdf', 'F')
```