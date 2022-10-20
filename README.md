# ProjectPdf

---

## Use python to handle common task of pdf file, e.g. split a pdf file.

- Split a pdf file
- Add watermark to a pdf file
- Merge pdf files
- Extract pdf pages of an existing pdf file to a new pdf file
- Rotate a pdf file
- Add image file to a pdf file

---

Note: In add_image2pdf.py, I can't insert the watermark image on the bottom of a pdf file 
using only the PyMuPDF library. To solve this problem, I use both the PyPDF2 and PyMuPDF.
Steps:
1. Add the image to the blank pdf and output a watermark pdf. (using PyMuPDF)
2. Merge the watermark pdf to the input pdf. (using PyPDF2)

---

## Environment:
- Windows 10
- Python 3.10.4
- PyPDF2 2.10.8
- PyMuPDF 1.20.2
Note: The python scripts may not work for linus or macOS platforms.

---

## Commands to install the python package PyPDF2
```python
pip install PyPDF2==2.10.8

```
or install the latest version
```python
pip install PyPDF2
```

---

## Commands
### Check python version
```python
python -V
```

### Check pip version
```python
pip --version
```

### Check the version of the python packages
```cmd
pip show PyPDF2
```
```cmd
pip show PyMuPDF
```

### List all the installed python packages
```python
pip list
```