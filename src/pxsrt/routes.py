from flask import render_template, url_for, request, redirect
from pxsrt import app


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/image', methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
        if request.form['action'] == 'preview':
            f = request.files["userImageFile"]
            print(f)
            # return redirect(request.url)
    return render_template('index.html')


@app.route('/dispaly')
def display():

    return
