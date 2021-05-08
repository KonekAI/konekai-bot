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

import requests

url = 'https://api.openai.com/v1/answers'
headers = {
    'Authorization': 'Bearer insertKeyHere'}


def puppyTest():
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
    return (response.json()["answers"])


# print(puppyTest())


def toHackTest(question: str):
    payload = {
        "documents": ["TOHacks is a student-run organization affiliated with the University of Toronto.",
                      "TOHacks hosted a virtual hackathon for participants to compete in on May 8th and May 9th in 2021.",
                      "Shwetha Sivakumar and Andy Tran are the Co-Chairs and Co-Founders of TOHacks.",
                      "Spandhana Gade is the Vice President of HR Strategy at TOHacks and Joy Lin is the Vice President of Operations at TOHacks.",
                      "Four people are allowed per team for the hackathon, and participants of all levels of experience are welcome.",
                      "The official website for TOHacks is https://www.tohacks.ca/.",
                      "Questions about TOHacks can be emailed to info@tohacks.ca."
                      "TOHacks is on Facebook at https://www.facebook.com/hackathontohacks/ and on LinkedIn at https://www.linkedin.com/company/tohacks/."],
        "question": question,
        "search_model": "ada",
        "model": "curie",
        "examples_context": "In 2017, U.S. life expectancy was 78.6 years. Atul Gawande has written about the decline of end of life health care in America.",
        "examples": [["What is human life expectancy in the United States?", "78 years."], ["Who wrote books about health care in America?", "Atul Gawande."]],
        "max_tokens": 50,
        "stop": ["\n", "<|endoftext|>"]
    }

    response = requests.post(url, headers=headers, json=payload)
    return (response.json()["answers"])


# print(toHackTest("What is TOHacks?"))
# print(toHackTest("Who is the founder of TOHacks?"))
# print(toHackTest("Who is allowed to participate in TOHacks?"))
# print(toHackTest("When is TOHacks Hackathon happening?"))
# print(toHackTest("Where can I learn more about TOHacks?"))
