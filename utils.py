import requests
from bs4 import BeautifulSoup
from flask import abort
from htmlmin.minify import html_minify

# extract url from insta post
def extract_url(post_url):
    response = requests.get(post_url)

    if response.status_code == 200:
        body = response.text

        soup = BeautifulSoup(body, 'html.parser')

        meta = soup.find_all('meta', {'property': 'og:image'})

        url = meta[0]['content']

        return url
        
# compress html
def compress(data):
    return html_minify(data)

