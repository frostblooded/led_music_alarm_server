from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def parse_request():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        print(request.form['test'])
        return "Thanks for submitting"
