from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch

def text_to_pdf(input_text_file, temp_pdf_file):
    with open(input_text_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    c = canvas.Canvas(temp_pdf_file, pagesize=A4)
    width, height = A4
    y = height - inch

    for index, line in enumerate(lines):
        line = line.strip()
        if y < inch:
            c.showPage()
            y = height - inch

        if index == 0:
            # First line as bold heading
            c.setFont("Helvetica-Bold", 16)
        else:
            c.setFont("Helvetica", 12)

        c.drawString(1 * inch, y, line)
        y -= 18 if index == 0 else 14

    c.save()


def add_pdf_password(input_pdf, output_pdf, password):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)
    with open(output_pdf, "wb") as f:
        writer.write(f)

def convert_text_to_protected_pdf(input_text_file, output_pdf_file, password):
    temp_pdf_file = "temp_unprotected.pdf"

    print("Converting text to PDF...")
    text_to_pdf(input_text_file, temp_pdf_file)

    print("Applying password protection...")
    add_pdf_password(temp_pdf_file, output_pdf_file, password)

    os.remove(temp_pdf_file)
    print(f"Done! Output: {output_pdf_file}")
convert_text_to_protected_pdf("security.txt", "security.pdf", "123456")    

# -------- Example usage --------
# if __name__ == "__main__":
#     input_text_file = "security.txt"            # Your .txt file
#     output_pdf_file = "security.pdf" # Output PDF name
#     password = "12345"                       # Set your desired password

   # convert_text_to_protected_pdf(input_text_file, output_pdf_file, password)
