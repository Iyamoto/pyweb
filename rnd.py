# Researching Bottle

from bottle import route, default_app


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


application = default_app()
