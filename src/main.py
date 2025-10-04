import llm_utils
import ocr_utils
import json,os

def get_all_pdfs(input_dir):
    pdf_files = []
    for file in os.listdir(input_dir):
        if file.lower().endswith('.pdf'):
            pdf_files.append(os.path.join(input_dir, file))
    return pdf_files

def process_all_pdfs(input_dir = "data/input",output_dir="data/output"):

    #be sure that the input and output directories exist
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    pdf_files = get_all_pdfs(input_dir)
    if not pdf_files:
        print("No PDF files found in", input_dir)
        return

    print(f"Found! {len(pdf_files)} PDF files. Starting extraction...\n")

    for pdf_path in pdf_files:
        try:
            #naming the output file
            file_name = os.path.basename(pdf_path)
            output_path = os.path.join(
                output_dir, os.path.splitext(file_name)[0] + ".json"
            )

            print(f"Processing.....: {file_name}")

            #OCR
            text = ocr_utils.scanned_pdf(pdf_path)
            if not text:
                print(f"No text extracted from {file_name}, skipping...\n")
                continue

            #LLM
            result = llm_utils.ollama_api(text)
            if not result:
                print(f"LLM returned no result for {file_name}, skipping...\n")
                continue

            #save the result
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

            print(f"Done. Saved to {output_path}\n")

        except Exception as e:
            print(f"Error while processing {pdf_path}: {e}\n")


if __name__ == "__main__":
    process_all_pdfs()



