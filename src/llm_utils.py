from urllib import response
import requests
import json
import re

def ollama_api(text):

    if not text or len(text.strip()) < 10:
        print("input is too short or empty")
        return

    try:
        prompt = f"""
            Extract the following fields from the insurance card text:

            - Policy Numbers
            - Insured Name
            - Coverage Period

            Return only valid JSON like this:
            {{
              "Policy Numbers": "...",
              "Insured Name": "...",
              "Coverage Period": "..."
            }}

            Text:
            {text}
            """

        payload = {
            "model" : "llama3",
            "prompt" : prompt,
            "stream" : False
        }

        response = requests.post(
            "http://localhost:11434/api/generate",
           json=payload,
           timeout = 60)

        if response.status_code == 200:
            result = response.json()
            clean = extract_json_from_response(result.get("response", ""))
            return clean
            

        else:
            print("Error: ", response.status_code, response.text)

    except Exception as e:
        print("A mistake had occured: exception" + e)



def extract_json_from_response(response_text):
    match = re.search(r"\{[\s\S]*\}", response_text)
    if match:
        try:
            return json.loads(match.group())
        except:
            return {"raw_response": response_text}
    return {"raw_response": response_text}