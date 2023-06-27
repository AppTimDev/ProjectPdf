"""
Usage:
Rotate a pdf file

User-defined variables:
input_filename
output_filename
rotate_degree
"""

from PyPDF2 import PdfReader, PdfWriter
from os import path

#User-defined variables
input_filename = r'pdfs\input.pdf'
output_filename = r'pdfs\output.pdf'
rotate_degree = 90 #clockwise

try:
    #current file directory
    cfd = path.dirname(__file__)
    input_pdf = path.join(cfd, input_filename)
    output_pdf = path.join(cfd, output_filename)

    with open(input_pdf, "rb") as f_input:
        input_fr = PdfReader(f_input)

        fw = PdfWriter()
        for i in range(len(input_fr.pages)):
            page = input_fr.pages[i]
            page.rotate(rotate_degree)
            fw.add_page(page)

        with open(output_pdf, "wb") as f_output:
            fw.write(f_output)
            print(f'Write pdf file: {output_pdf}')    
                
except Exception as e:
    print('Error:',e)    
finally:
    print('End of program.')


