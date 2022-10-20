'''
Environment:
-Python 3.10.4
-PyPDF2 2.10.8
-PyMuPDF 1.20.2

Usage:
Add a watermark image file to a pdf file

'''
from PyPDF2 import PdfFileReader, PdfFileWriter
from os import path
import fitz

#User-defined variables
rect_img = fitz.Rect(100,0,300,200) #determine the image position on the pdf
filename_input  = r'pdfs\input.pdf'
filename_blank  = r'pdfs\blank.pdf'
filename_image  = r'pdfs\copy.png'
filename_watermark = r'pdfs\temp_watermark.pdf'

filename_output = r'pdfs\output.pdf'

try:
    #current file directory
    cfd = path.dirname(__file__)
    path_input = path.join(cfd, filename_input)
    path_blank = path.join(cfd, filename_blank)
    path_image = path.join(cfd, filename_image)
    path_watermark = path.join(cfd, filename_watermark)
    path_output = path.join(cfd, filename_output)

    #1. Add the image to the blank pdf and output a watermark pdf.
    with fitz.open(path_blank) as doc:
        for page in doc:
            page.insert_image(rect=rect_img, filename=path_image)
        doc.save(path_watermark)
        print(f'Temp watermark pdf file is created: {path_watermark}')
    
    #2. Merge the watermark pdf to the input pdf. 
    with open(path_input, "rb") as f_input, open(path_watermark, "rb") as f_watermark:
        fr_input = PdfFileReader(f_input)
        #fr_watermark = PdfFileReader(f_watermark)
        #page_watermark = fr_watermark.getPage(0)

        fw = PdfFileWriter()
        for i in range(fr_input.getNumPages()):
            page = fr_input.getPage(i)

            #important: keep watermark pdf on the bottom
            fr_watermark = PdfFileReader(f_watermark)
            page_watermark = fr_watermark.getPage(0)            
            page_watermark.merge_page(page)
            fw.addPage(page_watermark)
            # page.merge_page(page_watermark)
            # fw.add_page(page)

        with open(path_output, "wb") as f_output:
            fw.write(f_output)
            print(f'Final output pdf file is created: {path_output}')
                
except Exception as e:
    print('Error:',e)
finally:
    print('End of program.')