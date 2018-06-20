import requests, re, json
from bs4 import BeautifulSoup
from flask import abort, jsonify
from htmlmin.minify import html_minify


def extract(post_url, isAlbum):
    # make a get request to the provided URL
    response = requests.get(post_url)

    # check if the request was successful
    if response.status_code == 200:

        # grab the content of the HTML DOC
        # and pass it to BeautifulSoup
        body = response.text
        soup = BeautifulSoup(body, 'html.parser')

        # look for the meta that contains the content type
        # and assign the value to the "content_type" variable
        meta_type = soup.find_all('meta', {'property': 'og:type'})
        content_type = meta_type[0]['content']

        # find all of the script tags
        scrTag = soup.find_all('script', {'type': 'text/javascript'})

        # where the data pulled from Instagram is stored
        datapoints = []

        # regex to erase everything outside of {}
        pattern = re.compile(r"[{].*[}]")

        # pick the 3rd script tag and process it
        for data in pattern.findall(str(scrTag[3])):
            # after the data is processed 
            # its assigned to the "datapoints" array
            datapoints.append(json.loads(data))

        # run this if the post is not an album
        if not isAlbum:
            # additional checking for reliability
            if (content_type == 'instapp:photo') or (content_type == 'profile') or (content_type == 'video'):
                if content_type == 'video': 
                    video_url = datapoints[0]['entry_data']['PostPage'][0]['graphql']['shortcode_media']['video_url']

                    return jsonify({"type": "video", "url": video_url})
                else: 
                    image_url = datapoints[0]['entry_data']['PostPage'][0]['graphql']['shortcode_media']['display_url']

                    return jsonify({"type": "image", "url": image_url})

        # run this if its an album
        else:
            # this contains a link to every album
            urls = []

            # the album
            album = datapoints[0]['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']

            # error handling
            try:
                # enumerate through every link in the album
                # and assign it to the "urls" list
                for i, item in enumerate(album):
                    url = {
                        "url": item['node']['display_url']
                    }
                    
                    urls.append(url)
            except:
                return abort(500)

            # once the enumerations is done, the array is returned.
            return jsonify({"type": "album", "urls": urls})


# compress html
def compress(data):
    return html_minify(data)