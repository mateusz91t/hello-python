from PyPDF2 import pdf
import click
import PyPDF2
from click.termui import prompt


@click.command()
@click.option('-i', help='pdf source input', prompt=True)
@click.option('-o', help='text source output', prompt=True)
def get_pdf_txt(i: str, o: str):
    with open(i, 'rb') as pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        output = [f'\n\n--- PAGE {j} ---\n' + read_pdf.getPage(j).extractText() for j in range(read_pdf.getNumPages())]
        pdf_file.close()
    with open(o, 'w+', encoding='utf-8') as txt_file:
        txt_file.writelines(output)
        txt_file.close()


get_pdf_txt()
