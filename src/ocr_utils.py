import os
import io
import PyPDF2
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def scanned_pdf(path):

    if not os.path.exists(path):
        print("The file does not exist")
        return None

    try:

        with open(path,'rb') as file:
            the_pdf = PyPDF2.PdfReader(file)

            if len(the_pdf.pages) < 1:
                print("The PDF file is empty")
                return None

            first_page = the_pdf.pages[0]

            if '/Resources' in first_page and '/XObject' in first_page['/Resources']:
                the_object = first_page['/Resources']['/XObject'].get_object() 

                for obj in the_object:
                    if the_object[obj]['/Subtype'] == '/Image':
                        data = the_object[obj].get_data()
                        image = Image.open(io.BytesIO(data))

                        #OCR process
                        text = pytesseract.image_to_string(image,lang='eng')
                        print("Extracted text from scanned PDF: ", text)
                        print("*"*20 + "scanning has been complated!" + "*"*20)
                        return text.strip()

            print("There is no image can be extracted from the PDF")

    except Exception as e:
        print("A mistake had occured while testing: exception" + str(e))
        return None

