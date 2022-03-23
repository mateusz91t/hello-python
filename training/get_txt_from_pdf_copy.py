from PyPDF2 import pdf
import click
import PyPDF4
from click.termui import prompt


@click.command()
@click.option('-i', help='pdf source input', prompt=True)
@click.option('-o', help='text source output', prompt=True)
def get_pdf_txt(i: str, o: str):
    with open(i, 'rb') as pdf_file:
        read_pdf = PyPDF4.PdfFileReader(pdf_file)
        output = [f'\n\n--- PAGE {j} ---\n' + read_pdf.getPage(j).extractText() for j in range(read_pdf.getNumPages())]
        pdf_file.close()
    with open(o, 'w+', encoding='utf-8') as txt_file:
        txt_file.writelines(output)
        txt_file.close()


# get_pdf_txt()
fpdf = 'D:\share_dir\publications\good\Active Learning Using Pre-clustering.pdf'
# read_pdf = PyPDF4.PdfFileReader(open(fpdf, 'rb'))
# read_pdf.pages[2].extractText()

from pdf2image import convert_from_path
from pytesseract import image_to_string

images = convert_from_path(fpdf)
for i,image in enumerate(images,start=1):
    image.save(f"./images/page_{i}.jpg","JPEG")

image_to_string("./images/page_1.jpg")

