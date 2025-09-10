from urllib import response
import requests
import json

def test_ollama_api(text):

    print("""ollama llm testing""")
    if not text or len(text.strip()) < 10:
        print("input is too short or empty")
        return

    try:
        prompt = "briefly summarize the following text: " + text + "'"

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
            print("response: ", result)
            print("Ollama testing has been complated")

        else:
            print("Error: ", response.status_code, response.text)

    except Exception as e:
        print("A mistake had occured while testing: exception" + e)

if __name__ == "__main__":
    # example text
    text = """
    Artificial intelligence and machine learning are rapidly evolving fields that 
    are transforming various industries. Large language models like those provided 
    by Ollama enable developers to create innovative applications in natural 
    language processing, computer vision, and robotics.
    """
    
    test_ollama_api(text)


