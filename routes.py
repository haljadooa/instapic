from app import app
from flask import send_from_directory, request, abort
from utils import extract_url, extract_json

# serve static files
@app.route('/public/<path:filename>')
def serve_static_files(filename):
   return send_from_directory('public', filename)

@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        # url provided by the user
        post_url = request.args.get('url')

        is_album = int(request.args.get('album'))

        if is_album == 1:
            response = extract_json(post_url)

            return response
        else:    
            response = extract_url(post_url)

            return response   
    else:
        abort(405)