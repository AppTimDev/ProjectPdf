"""
Usage:
Add watermark pdf to a pdf file

User-defined variables:
input_filename
watermark_filename
output_filename
"""
from PyPDF2 import PdfReader, PdfWriter
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
        input_fr = PdfReader(f_input)
        watermark_fr = PdfReader(f_watermark)
        watermark_page = watermark_fr.pages[0]

        fw = PdfWriter()
        for i in range(len(input_fr.pages)):
            page = input_fr.pages[i]
            page.merge_page(watermark_page)
            fw.add_page(page)

        with open(output_pdf, "wb") as f_output:
            fw.write(f_output)
            print(f'Write pdf file: {output_pdf}')    
                
except Exception as e:
    print('Error:',e)    
finally:
    print('End of program.')
    