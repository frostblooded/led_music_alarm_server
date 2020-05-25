from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def parse_request():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        data = request.form

        text = '''[spotify]
username = {}
password = {}
cliend_id = {}
client_secret = {}
private_session = true

[mpd]
enabled = true
        '''.format(data['username'],
                   data['password'],
                   data['client_id'],
                   data['client_secret'])

        text_file = open("/etc/mopidy/mopidy.conf", "w")
        text_file.write(text)
        text_file.close()
        return "Thank you!"
