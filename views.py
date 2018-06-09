from app import app
from flask import render_template
from utils import compress

@app.route('/')
def index():
    compressed = compress(render_template('index.html'))
    return compressed