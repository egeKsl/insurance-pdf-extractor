# Insurance PDF Field Extractor (OCR + LLM)

This project extracts structured information from insurance PDF documents — whether scanned or digital — using a combination of OCR and large language models.

---

## 🧠 Overview

The system automatically identifies the type of PDF (scanned or text-based) and extracts three key fields:

- **Policy Number**
- **Insured Name**
- **Coverage Period**

It integrates:
- 🧩 **Tesseract OCR** for scanned/image-based PDFs  
- 💬 **LLaMA 3 (via Ollama)** for natural language field extraction  
- ⚙️ **Python** for orchestration and automation

---

## ⚙️ Features
- Automatic detection of scanned vs. digital PDFs  
- End-to-end processing pipeline (OCR → LLM → JSON output)  
- Error handling for empty or hybrid documents  
- Simple directory-based workflow (`data/input` → `data/output`)  

---

## 📂 Project Structure
insurance-pdf-extractor/
│
├── data/
│   ├── input/             # Input PDFs (scanned or text-based)
│   └── output/            # Extracted JSON results
│
├── src/
│   ├── ocr_utils.py       # Handles OCR and text extraction
│   ├── llm_utils.py       # Communicates with Ollama (LLaMA 3) for field extraction
│   ├── main.py            # Main pipeline (runs OCR + LLM and saves output)
│
├── tests/                 # (Optional) test scripts for debugging or validation
│
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Ignore unnecessary files for Git
└── .gitattributes         # Git text/binary file rules
