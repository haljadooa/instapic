from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# prevent jsonify from sorting data alphabetically
app.config['JSON_SORT_KEYS'] = False

from views import *
from routes import *

# unless in development, use gunicorn instead...
#if __name__ == '__main__':
#    app.debug = True
#    app.run('127.0.0.1', 9000)