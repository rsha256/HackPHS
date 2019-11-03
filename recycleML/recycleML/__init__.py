import os
#import magic

from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime

UPLOAD_FOLDER = 'static/img/tmp'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


app = Flask(__name__)


app.secret_key = "dev"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


# upload
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

p = 0

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        print(file.filename)
        if allowed_file(file.filename):
            now = datetime.now()
            filename = secure_filename(file.filename)
            global p
            p = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("yee")
            return render_template('index.html', image=send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename), filename=p, title='Upload')
    print("yeet")
    print(request.method)
    return render_template('index.html', filename=p, title='Upload')

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', title='Upload')

if __name__ == '__main__':
    app.run(debug=True)
