# Researching Bottle

from bottle import route, default_app, run, request
import json


@route('/')
def index():
    return '<h1>PYWEB</h1>'


@route('/ping')
def health():
    return 'ok'


@route('/status')
def status():
    result = {
        'bottle': 'UP'
    }
    return result


@route('/webhook', method=['POST'])
def webhook():
    data = json.loads(request.data)
    print(data)
    return 'ok'


application = default_app()

if __name__ == '__main__':
    run(server='gunicorn', host='0.0.0.0', port=8080, workers=4)
