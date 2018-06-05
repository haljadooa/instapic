from app import app
from flask import send_from_directory, request, abort
from utils import extract_url

# serve static files
@app.route('/public/<path:filename>')
def serve_static_files(filename):
   return send_from_directory('public', filename)

@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        # url provided by the user
        post_url = request.args.get('url')
        
        # data sent back to the clinet 
        response = extract_url(post_url)

        return response
    else:
        abort(405)