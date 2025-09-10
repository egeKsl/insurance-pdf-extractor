from urllib import response
import request 
import json

def test_ollama_api(text):

    print("""ollama llm testing""")
    if not text or len(text.strip()) < 10:
        print("input is too short or empty")
        return

    try:
        promt = "briefly summarize the following text: " + text + "'"

        payload = {
            "model" : "llama3",
            "promt" : promt,
            "stream" : False
        }

        response = requests.post(
            "http://localhost:11434/api/generate",
           json=payload,
           timeout = 60)

        if response.status_code == 200:

            result = response.json()
            print("response: ", result)
            print("Ollama testing has been complated")

        else:
            print("Error: ", response.status_code, response.text)

    except Exception as e:
        print("A mistake had occured while testing: exception" + e)


