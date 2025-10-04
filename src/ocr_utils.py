import os
import io
import re
import PyPDF2
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def is_meaningful_text(text):
    """Check if extracted text is actually readable and not garbage."""
    if not text or len(text.strip()) < 10:
        return False
    # remove whitespace and check ratio of letters to total characters
    letters = len(re.findall(r"[A-Za-z]", text))
    ratio = letters / max(len(text), 1)
    # require at least some words and 50% alphabetic ratio
    return len(text.split()) > 3 and ratio > 0.5


def scanned_pdf(path):

    if not os.path.exists(path):
        print("The file does not exist")
        return None

    try:
        with open(path, 'rb') as file:
            the_pdf = PyPDF2.PdfReader(file)

            if len(the_pdf.pages) < 1:
                print("The PDF file is empty")
                return None

            all_text = ""

            for i, page in enumerate(the_pdf.pages):
                # test if the page contains text
                text = page.extract_text()

                if text and is_meaningful_text(text):  
                    print(f"[Page {i+1}] Text-based PDF detected")
                    all_text += text + "\n"
                else:
                    # the second paper may be image-based
                    print(f"[Page {i+1}] Image-based PDF detected.Running OCR...")

                    if '/Resources' in page and '/XObject' in page['/Resources']:
                        the_object = page['/Resources']['/XObject'].get_object()

                        for obj in the_object:
                            if the_object[obj]['/Subtype'] == '/Image':
                                data = the_object[obj].get_data()
                                image = Image.open(io.BytesIO(data))
                                ocr_text = pytesseract.image_to_string(image, lang='eng')
                                all_text += ocr_text + "\n"

            if not all_text.strip():
                print("No text could be extracted from this PDF.")
                return None

            print("Text extraction complete!")
            return all_text.strip()
    except Exception as e:
        print("A mistake had occured while testing: exception" + str(e))
        return None

