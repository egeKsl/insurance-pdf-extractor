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

---

## 🚀 How It Works

1. Place your PDF files into `data/input/`.
2. Run the main script:
   ```bash
   python src/main.py
---

## 🧩 Example Output
{
  "Policy Numbers": "TCP 401 —14-21/CGL—401-14-21",
  "Insured Name": "State of Georgia Government or State employees",
  "Coverage Period": "July 1, 2020 — June 30, 2021"
}
