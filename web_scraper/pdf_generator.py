```python
from fpdf import FPDF
from web_scraper.config import MAX_SUMMARY_LENGTH

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Web Scraper Report', 0, 1, 'C')

    def chapter_title(self, link):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Link: %s' % link, 0, 1, 'L')
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
        pdf.chapter_body(summary[:MAX_SUMMARY_LENGTH])

    pdf.output('web_scraper_report.pdf', 'F')
```
This code creates a PDF class that extends the FPDF class. The header method sets the header of the PDF, the chapter_title method sets the title of each chapter (which is the link), and the chapter_body method sets the body of each chapter (which is the summary). The generate_pdf function takes a dictionary where the keys are the links and the values are the summaries, and generates a PDF where each link and its summary is a chapter. The PDF is saved as 'web_scraper_report.pdf'.