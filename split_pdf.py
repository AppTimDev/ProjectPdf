"""

Usage:
Split pdf

Example:
page_indexes = [1,3]

Then the pdf file will be splitted into 2 pdf files
file1: page 1-2
file2: page 3-end

User-defined variables:
input_filename
page_indexes
"""
from PyPDF2 import PdfReader, PdfWriter
from os import path

def split_by_pages_indexes(input_file_name, page_indexes):
    """
    :param input_file_name: filename
    :param page_indexes: 
    :return: None
    """
    cfd = path.dirname(__file__)
    input_file_full_name = path.join(cfd, input_file_name)
    with open(input_file_full_name, 'rb') as f_input:
        pdf_input = PdfReader(f_input)
        if pdf_input is None:
            return

        total_page_num = len(pdf_input.pages)
        print('total page:',total_page_num)

        split_indexes = []
        for i,pageNum in enumerate(page_indexes):
            try:
                split_indexes.append((pageNum,page_indexes[i+1]))
            except:
                split_indexes.append((pageNum,total_page_num+1))
        #print(split_indexes)       

        for split_index in split_indexes:
            pdf_output = PdfWriter()
            
            start = split_index[0] -1
            end = split_index[1]-1
            print('pdf pages:',str(start+1) + '-' + str(end))           
            split_pdf_name = "".join(input_file_name.split('.')[:-1]) + '_' + str(start+1) + '.pdf'

            for i in range(start, end):
                pdf_output.add_page(pdf_input.pages[i])

            output_file_full_name = path.join(cfd, split_pdf_name)
            with open(output_file_full_name, 'wb') as f_output:
                pdf_output.write(f_output)




def main():
    try:
        #User-defined variables
        input_file_name = r'pdfs\input.pdf'
        page_indexes = [1,3]

        
        split_by_pages_indexes(input_file_name, page_indexes) #split pdf files
        print('Split pdf files complete!')               
    except Exception as e:
        print('Error:',e)    
    finally:
        print('End of program.')    


if __name__ == '__main__':
    main()
