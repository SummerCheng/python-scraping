from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
from urllib.request import urlopen

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

# pdfFile = urlopen("http://www.bartleby.com/ebook/adobe/3134.pdf ")
pdfFile=open("C:\\Users\Lesley\Desktop\临床肿瘤学概论.pdf","rb")
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()
