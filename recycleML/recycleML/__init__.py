import os
from os.path import join, dirname, realpath
#import magic

from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime

from recycleML import tester

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

@app.route("/handleUpload", methods=['GET', 'POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            x = str(datetime.now())
            x = x.replace(':', '')
            x = x.replace('.', '')
            x = x.replace(' ', '')
            x = x + '.jpg'
            path = dirname(realpath(__file__)) + os.path.join('/static/img/tmp/', x)
            photo.save(path)
            a = yield tester.get_classification(path) 
            p1 = a[0]
            n1 = a[1]
            p2 = a[2]
            n2 = a[3]
            p3 = a[4]
            n3 = a[5]
            p4 = a[6]
            n4 = a[7]
            p5 = a[8]
            n5 = a[9]
            p6 = a[10]
            n6 = a[11]
    return render_template('index.html', path=path, title='Upload',
    p1=p1, n1=n1, p2=p2, n2=n2, p3=p3, n3=n3, p4=p4, n4=n4, p5=p5, n5=n5, p6=p6, n6=n6)

# p = 0
# 
# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             print("f1")
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         print("c1")
#         if file.filename == '':
#             print("f2")
#             flash('No selected file')
#             return redirect(request.url)
#         print(file.filename)

#         print("c2")

#         if allowed_file(file.filename):
#             print("f3")
#             now = datetime.now()
#             filename = secure_filename(file.filename)
#             global p
#             p = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             print("yee")
#             return render_template('index.html', image=send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename), filename=p, title='Upload')
#     print("yeet")
#     print(request.method)
#     return render_template('index.html', filename=p, title='Upload')

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', title='Upload')

if __name__ == '__main__':
    app.run(debug=True)
