from flask import Flask
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)

from views import *
from routes import *

# unless in development, use gunicorn instead...

#if __name__ == '__main__':
#    app.debug = True
#    app.run('127.0.0.1', 8080)