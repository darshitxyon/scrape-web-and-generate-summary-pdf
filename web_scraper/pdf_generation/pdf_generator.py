```python
from fpdf import FPDF

class PDFGenerator:
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename

    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", size = 15)

        for i, item in enumerate(self.data):
            link, summary = item
            pdf.cell(200, 10, txt = f"Link: {link}", ln = i+1, align = 'C')
            pdf.cell(200, 10, txt = f"Summary: {summary}", ln = i+2, align = 'C')

        pdf.output(self.filename)
```