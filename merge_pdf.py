"""
Usage:
Merge pdfs

User-defined variables:
filenames
output_filename
"""
from PyPDF2 import PdfReader, PdfWriter
from os import path


def merge(filenames, outputfile_path):
    print(f'Output file path: {outputfile_path}')
    pdf_output = PdfWriter()
    for filename in filenames:
        print(f'merge file: {filename}')
        pdf_input = PdfReader(filename)
        if pdf_input is None:
            return
        total_page_num = len(pdf_input.pages)
        for i in range(total_page_num):                
            pdf_output.add_page(pdf_input.pages[i])

    with open(outputfile_path, 'wb') as f_output:
        pdf_output.write(f_output)

        
def main():
    try:
        #User-defined variables        
        filenames = [r'pdfs\input.pdf', r'pdfs\input.pdf']
        output_filename = r'pdfs\output.pdf'

        cfd = path.dirname(__file__)
        input_file_names = []
        for filename in filenames:
            input_file_names.append(path.join(cfd, filename))
        merge(input_file_names, path.join(cfd, output_filename)) #merge files
        print('Merge pdf files complete!')               
    except Exception as e:
        print('Error:',e)    
    finally:
        print('End of program.')    


if __name__ == '__main__':
    main()
