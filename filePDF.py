import PyPDF2
import os

os.chdir('C:\\Users\\Asus\\Desktop\\NER')

pdfFile = open('rule-based-NER.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)

print(reader.numPages)

page = reader.getPage(0)

print(page.extractText())

# pdf reading with the help of pyPDF
for pageNum in range(reader.numPages):
    reader1 = reader.getPage(pageNum).extractText()
    print(reader1)
