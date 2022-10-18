"""
Environment:
-Python 3.10.4
-PyPDF2 (Version: 2.10.8)

Usage:
Rotate a pdf file

User-defined variables:
input_filename
output_filename
rotate_degree
"""

from PyPDF2 import PdfFileReader, PdfFileWriter
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
        input_fr = PdfFileReader(f_input)

        fw = PdfFileWriter()
        for i in range(input_fr.getNumPages()):
            page = input_fr.getPage(i)
            page.rotate_clockwise(rotate_degree)
            fw.addPage(page)

        with open(output_pdf, "wb") as f_output:
            fw.write(f_output)
            print(f'Write pdf file: {output_pdf}')    
                
except Exception as e:
    print('Error:',e)    
finally:
    print('End of program.')


