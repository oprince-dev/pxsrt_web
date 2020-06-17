from flask import Flask, render_template
from PIL import Image
import pxsrt
# import os


app = Flask(__name__)

@app.route('/')
def home():
    img = 'static/tokyo.jpg'
    return render_template('main.html', img=img)

if __name__ == '__main__':
    app.run(debug=True)
