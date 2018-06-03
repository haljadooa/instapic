from app import app
from flask import send_from_directory, request, abort
from utils import extract_url

@app.route('/public/<path:filename>')
def serve_static_files(filename):
   return send_from_directory('public', filename)

@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        post_url = request.args.get('url') 
        image_url = extract_url(post_url)

        return image_url
    else:
        abort(405)