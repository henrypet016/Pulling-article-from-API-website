import requests
from html_templates import ARTICLE_HTML_TEMPLATE

API_URLS = [
    'https://api.elifesciences.org/articles/84711',
    'https://api.elifesciences.org/articles/85056',
    'https://api.elifesciences.org/articles/85056'
]

def fetch_api_response(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    return None

def generate_html_text_for_article(article_title: str) -> str:
    return ARTICLE_HTML_TEMPLATE.format(article_title=article_title)

def write_html_text_in_html_file(index, article_title):
    with open(f'article{index}.html', 'w') as file:
        file.write(generate_html_text_for_article(article_title))


for index, api_url in enumerate(API_URLS, start=1):
    api_response = fetch_api_response(api_url)
    if api_response:
        write_html_text_in_html_file(index, api_response['title'])
    else:
        print(f'Request to the API failed for {api_url}')