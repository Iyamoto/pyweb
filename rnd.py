# Researching Bottle

import json
import os
from bottle import route, default_app, run, request, error


def updatelocalstate(statepath='state.json', data=None):
    if data is None:
        return 0

    if os.path.isfile(statepath):
        with open(statepath, 'r') as infile:
            state = json.load(infile)
    else:
        state = dict()

    z = state.copy()
    z.update(data)

    # Save updated state locally
    with open(statepath, 'w') as outfile:
        json.dump(z, outfile)

    return len(z)


@route('/')
def index():
    # TODO must show available links with descriptions
    return '<h1>PYWEB</h1>'


@route('/ping')
def health():
    return 'ok'


@route('/status')
def status():
    # TODO run some tests here
    result = {
        'bottle': 'UP'
    }
    return result


@route('/webhook', method='POST')
def webhook():
    # Check the sender

    # Get message
    data = request.json

    # Do something
    updatelocalstate(statepath=os.path.join('data', 'state.json'), data=data)

    return data


@route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            <input value="Login" type="submit" />
        </form>
    '''


@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')

    # Check login
    # TODO implement webhook based login
    return 'ok'

@error(404)
def error404():
    return 'Nothing here, sorry'


application = default_app()

if __name__ == '__main__':
    run(server='gunicorn', host='0.0.0.0', port=8080, workers=4)
