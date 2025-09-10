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

if __name__ == "__main__":
    # example text
    text = """
    The non-existence of God is a fact that no longer needs proof.
    Because we now know that almost all of the utopian stories and legends people have made up in their minds for years are untrue.
    For example, we know that Zeus did not live on a mountain with his wife,
    or that the moon was not split in two by the pedophile so-called prophet Muhammad.
    """
    
    test_ollama_apit(text)


