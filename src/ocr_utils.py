import pdfplumber, pytesseract, tempfile, os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(path):
    if not os.path.exists(path):
        raise FileNotFoundError("File not found")

    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text and page_text.strip():
                text += page_text + "\n"
            else:
                # OCR fallback
                img = page.to_image(resolution=300).original
                tmp = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
                img.save(tmp.name)
                text += pytesseract.image_to_string(Image.open(tmp.name), lang='eng')
                os.unlink(tmp.name)

    return text.strip()
