import requests
from bs4 import BeautifulSoup
from flask import abort, jsonify
from htmlmin.minify import html_minify

# extract url from insta post
def extract_url(post_url):
    response = requests.get(post_url)

    if response.status_code == 200:

        body = response.text
        soup = BeautifulSoup(body, 'html.parser')

        # grab the content's type first
        meta_type = soup.find_all('meta', {'property': 'og:type'})
        content_type = meta_type[0]['content']

        # check if the post is a photo, video, or profile pic
        # we preform specifc actions based on the content type
        if (content_type == 'instapp:photo') or (content_type == 'profile'):
            meta_photo = soup.find_all('meta', {'property': 'og:image'})
            image_url = meta_photo[0]['content']

            return jsonify({"data": {"type": "image", "url": image_url}})
        elif content_type == 'video':
            
            meta_video = soup.find_all('meta', {'property': 'og:video'})
            video_url = meta_video[0]['content']

            return jsonify({"data": {"type": "video", "url": video_url}})

# compress html
def compress(data):
    return html_minify(data)

