from email.mime import image
import os
import io
import PyPDF2
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def scanned_pdf(path):
    print("*"*20 + "scanned pdf testing" + "*"*20)

    if not os.path.exists(path):
        print("The file does not exist")
        return None

    try:

        with open(path,'rb') as file
            the_pdf = PyPDF2.PdfReader(file)

            if len(the_pdf.pages) < 1:
                print("The PDF file is empty")
                return None

            first_page = the_pdf.pages[0]

            if '/resources' in first_page and '/XObject' in first_page['/resources']:
                the_object = first_page['/resources']['/XObject'].get_object()

                for obj in the_object:
                    if the_object[obj]['/Subtype'] == '/Image':
                        data = the_object[obj].get_data()
                        image = Image.open(io.BytesIO(data))

                        #OCR process
                        text = pytesseract.image_to_string(image,lang='eng')
                        print("Extracted text from scanned PDF: ", text)
                        print("*"*20 + "scanning has been complated!" + "*"*20)

            print("There is no image can be extracted from the PDF")

    except Exception as e:
        print("A mistake had occured while testing: exception" + str(e))
        return None


if __name__ == "__main__":
    # example text
    path = 'C:\\Users\\corle\\Downloads\\2025_09_10 13_17 Office Lens.pdf'
    
    scanned_pdf(path)