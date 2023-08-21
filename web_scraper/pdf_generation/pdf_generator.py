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
        line_height = 10
        margin = 10

        for item in self.data:
            link, summary = item
            pdf.cell(200, line_height, txt = "Link: " + link, ln = True)
            pdf.multi_cell(0, line_height, txt = "Summary: " + summary)
            pdf.ln(line_height) # Add a line break

        pdf.output(self.filename)
```