import requests
from AI import url,bearer

def askGPT3(query):

    # Setting up headers and data
    headers = {
        "Authorization": f"Bearer {bearer}",
        "Content-Type": "application/json",
    }
    data = {
        "messages": [
            {
                "role": "system",
                "content": f"Write a response to the user queries and follow their given tag instructions",
            },
            {
                "role": "user",
                "content": f"{query}",
            },
        ]
    }

    # Making the API request
    response = requests.post(url, headers=headers, json=data)
    if response.json()["success"]:
        # print("\n\nFrom chatgpt:\n")
        # print(response.json()["result"]["response"])
        return response.json()["result"]["response"]
    else:
        print("response failed from gpt")
        return None
    
# askGPT3("if i give you a text can you find pattern of instruction and reply on it and preapre it for llama 2 training")