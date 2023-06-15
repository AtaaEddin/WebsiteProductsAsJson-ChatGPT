import openai
import json
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup

from GPTfunctions.JsonFormater import jsonformater_function
from GPTfunctions.Scraper import scraper_function

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def scrape_text(url):
    """Scrape text from a webpage"""
    # Most basic check if the URL is valid:
    if not url.startswith('http'):
        return "Error: Invalid URL"
    
    try:
        headers = {
            'User-Agent': 'My User Agent 1.0',
            'From': 'youremail@domain.example'  # This is another valid field
        }
        # print("url: ", url)
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        return "Error: " + str(e)

    # Check if the response contains an HTTP error
    if response.status_code >= 400:
        return "Error: HTTP " + str(response.status_code) + " error"

    soup = BeautifulSoup(response.text, "html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    
    if len(text) > 4090:
        text = text[:4090]
    return text

def query(input, query_GPTfunctions, output_parameter_name):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content": input}],
        functions=query_GPTfunctions,
        function_call="auto",
    )
    #print(completion)
    reply_content = completion.choices[0].message

    funcs = reply_content.to_dict()['function_call']['arguments']
    funcs = json.loads(funcs)
    #print(funcs[output_parameter_name])
    return funcs[output_parameter_name]

def get_products(user_input):
    website_url = query(user_input, [scraper_function], "website_url")
    html_content = scrape_text(website_url)
    products = query(html_content, [jsonformater_function], "products")
    return products


