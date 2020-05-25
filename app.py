import os
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        data = request.form

        text = '''[spotify]
username = {}
password = {}
client_id = {}
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

        print("Service restart:", os.system('sudo systemctl restart mopidy.service'))

        return render_template('index.html', flash="Credentials set!")
    
@app.route('/alarm', methods=['POST'])
def alarm():
    cron_text = '{} {} * * * mpc clear && mpc add {} && mpc play'.format(
        request.form['minutes'],
        request.form['hours'],
        request.form['spotify_uri']
    )

    remove_cron_command = 'sudo crontab -r'
    cron_set_command = '(sudo crontab -l ; echo "{}") | sort - | uniq - | sudo crontab -'.format(cron_text)

    print("Removing old crontabs:", os.system(remove_cron_command))
    print("Setting crontab:", os.system(cron_set_command))
    
    return render_template('index.html', flash="Alarm set!")

