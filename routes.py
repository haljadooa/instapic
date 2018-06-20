from app import app
from flask import send_from_directory, request, abort, render_template
from utils import extract

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
            response = extract(post_url, isAlbum=True)

            return response
        else:    
            response = extract(post_url, isAlbum=False)

            return response
    else:
        abort(405)