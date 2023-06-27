"""
Usage:
Extract selected pages from a pdf file and the pages will be combined to produce a new pdf file.

User-defined variables:
input_filename
output_filename
page_indexes
"""
from PyPDF2 import PdfReader, PdfWriter
from os import path


def extract_pdf_pages(page_indexes, input_filename, output_filename):
    page_indexes = [i-1 for i in page_indexes]
    #current file directory
    cfd = path.dirname(__file__)
    input_file_full_name = path.join(cfd, input_filename)
    output_file_full_name = path.join(cfd, output_filename)

    with open(input_file_full_name, 'rb') as f_input:
        pdf_input = PdfReader(f_input)
        page_count = len(pdf_input.pages)
        #print('num of page:', page_count)
        pdf_output = PdfWriter()
        for i in page_indexes:
            page = pdf_input.pages[i]
            pdf_output.add_page(page)
        
        with open(output_file_full_name, 'wb') as f_output:
            pdf_output.write(f_output)


def main():
    try:
        #User-defined variables        
        input_filename = 'pdfs/input.pdf'
        output_filename = 'pdfs/output_extract.pdf'
        page_indexes = [1,3]

        extract_pdf_pages(page_indexes, input_filename, output_filename)
        print('Extract pdf complete!')
    except Exception as e:
        print('Error:',e)    
    finally:
        print('End of program.')


if __name__ == '__main__':
    main()