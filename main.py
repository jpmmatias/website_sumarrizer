from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
import os
import ollama
from Website import Website


load_dotenv()

HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"



OLLAMA_HOST = os.getenv("OLLAMA_HOST")



def summarize_website(url, max_words = 0):
    website_content= Website(url)
    system_message = "You are a helpful assistant that can receive content from a website and summarize it in the best way possible" if max_words == 0 else f"You are a helpful assistant that can receive content from a website and summarize it, use only {max_words} number of words" 
    messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": f"Summarize for me please: {website_content.__str__()}"}
    ]
    response = ollama.chat(model=MODEL, messages=messages)
    return response['message']['content'] 

print("Welcome to website summarizer, what website do you want to summarize?")
url = str(input("Enter the website: "))
print("Do you have a maximum number of words? If no maximum, type 0")
max_num_words = int(input("Max num of words: "))
print(summarize_website(url=url, max_words=max_num_words))

    

