import llm_utils
import ocr_utils
import json,os

if __name__ == "__main__":
    #OCR
    path = 'C:\\Users\\corle\\Downloads\\2025_09_10_13_17_Office_Lens[1].pdf'
    text = ocr_utils.scanned_pdf(path)

    print("Extracted Text: ", text)

    #LLM
    result = llm_utils.ollama_api(text)

    os.makedirs("data/output", exist_ok=True)

    with open("data/output/result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("Done. Saved to data/output/result.json")


