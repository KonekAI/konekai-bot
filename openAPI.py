'''

pip install chronological
pip install openai
pip install python-dotenv
pip install loguru

import os
import openai

response = openai.Completion.create(
    engine="davinci", prompt="This is a test", max_tokens=5)

# From terminal you can run this to test
# openai api completions.create - e davinci - p "This is a test" - M 5 - -stream

curl https://api.openai.com/v1/engines/davinci/completions -H "Content-Type: application/json" -H "Authorization: Bearer insertKeyHere" -d '{"prompt": "This is a test", "max_tokens": 5}'
'''
import os
import openai
import requests


def askOpenAI(question):
    url = 'https://api.openai.com/v1/answers'
    openAI = os.environ['OPEN_AI']
    headers = {'Authorization': f'Bearer {openAI}'}

    
    response = requests.post(url, headers=headers, json=question)
    return (response.json()["answers"])



def puppyTest():
    url = 'https://api.openai.com/v1/answers'
    openAI = os.environ['OPEN_AI']
    headers = {'Authorization': f'Bearer {openAI}'}
    payload = {
        "documents": ["Puppy A is happy.", "Puppy B is sad."],
        "question": "which puppy is happy?",
        "search_model": "ada",
        "model": "curie",
        "examples_context": "In 2017, U.S. life expectancy was 78.6 years.",
        "examples": [["What is human life expectancy in the United States?", "78 years."]],
        "max_tokens": 5,
        "stop": ["\n", "<|endoftext|>"]
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.json()["answers"])
    return (response.json()["answers"])


