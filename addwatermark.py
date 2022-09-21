"""
Environment:
-Python 3.10.4
-PyPDF2 (Version: 2.10.8)

Usage:
Add watermark to a pdf

User-defined variables:
input_filename
watermark_filename
output_filename
"""
from PyPDF2 import PdfFileReader, PdfFileWriter
from os import path

#User-defined variables
input_filename = r'pdfs\input.pdf'
watermark_filename = r'pdfs\watermark_copy.pdf'
output_filename = r'pdfs\output.pdf'
try:
    #current file directory
    cfd = path.dirname(__file__)
    input_pdf = path.join(cfd, input_filename)
    watermark_pdf = path.join(cfd, watermark_filename)
    output_pdf = path.join(cfd, output_filename)

    with open(input_pdf, "rb") as f_input, open(watermark_pdf, "rb") as f_watermark:
        input_fr = PdfFileReader(f_input)
        watermark_fr = PdfFileReader(f_watermark)
        watermark_page = watermark_fr.getPage(0)

        fw = PdfFileWriter()
        for i in range(input_fr.getNumPages()):
            page = input_fr.getPage(i)
            page.mergePage(watermark_page)
            fw.addPage(page)

        with open(output_pdf, "wb") as f_output:
            fw.write(f_output)
            print(f'Write pdf file: {output_pdf}')    
                
except Exception as e:
    print('Error:',e)    
finally:
    print('End of program.')
    