# ProjectPdf
## Objectives
- use python scripts to handle some tasks and work with PDF documents
- use pipenv to manage a virtualenv for this project

---

## Use python to handle common task of pdf file, e.g. split a pdf file.

- Split a pdf file
- Merge pdf files
- Extract pdf pages of an existing pdf file to a new pdf file
- Add watermark pdf to a pdf file
- Add image file to a pdf file
- Rotate a pdf file

Note: In add_image2pdf.py, I can't insert the watermark image on the bottom of a pdf file 
using only the PyMuPDF library. To solve this problem, I use both the PyPDF2 and PyMuPDF.
Steps:
1. Add the image to the blank pdf and output a watermark pdf. (using PyMuPDF)
2. Merge the watermark pdf to the input pdf. (using PyPDF2)

---

## Environment:
- Windows 10
- Python 3.11.3
- PyMuPDF==1.22.5
- PyPDF2==3.0.1

Note: The python scripts may not work for linus or macOS platforms.

---

## Setup
0. Pipenv Setup

https://github.com/AppTimDev/PythonVenv

1. Create a virtual environment and install the packages
```sh
pipenv install
```
or

Install the package only
```sh
pipenv install PyPDF2 PyMuPDF
```

---

## How to Run the program 

1. Split a pdf file
- Input: 'pdfs/input.pdf'
- Output: 'pdfs/input_[pageNum].pdf'
```sh
pipenv run python split_pdf.py
```

2. Merge pdf files
- Input: 'pdfs/input.pdf' (change variable filenames in merge_pdf.py)
- Output: 'pdfs/output.pdf'
```sh
pipenv run python merge_pdf.py
```

3. Extract pdf pages of an existing pdf file to a new pdf file
- Input: 'pdfs/input.pdf'
- Output: 'pdfs/output_extract.pdf'
```sh
pipenv run python extract_pdf.py
```

4. Add watermark pdf to a pdf file
- Input: 'pdfs\input.pdf' and 'pdfs\watermark_copy.pdf'
- Output: 'pdfs\output.pdf'
```sh
pipenv run python addwatermark.py
```

5. Add image file to a pdf file 
- Input: 'pdfs\input.pdf' and 'pdfs\copy.png' and 'pdfs\blank.pdf' (given)
- Output: 'pdfs\output.pdf'
```sh
pipenv run python add_image2pdf.py
```

6. Rotate a pdf file
- Input: 'pdfs\input.pdf'
- Output: 'pdfs\output.pdf'
```sh
pipenv run python rotate_pdf.py
```

---

## Commands
### Check python version
```sh
pipenv run python -V
```

### Check pip version
```sh
pipenv run pip -V
```

### Check the version of the python packages
```sh
pipenv run pip show PyPDF2 PyMuPDF
```

### List all the installed python packages
```sh
pipenv run pip list
```

### Export to requirements.txt
```sh
pipenv run pip freeze > requirements.txt
```