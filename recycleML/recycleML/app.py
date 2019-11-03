import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', title='app')

if __name__ == '__main__':
    app.run(debug=True)
