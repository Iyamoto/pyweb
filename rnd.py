# Researching Bottle

from gevent import monkey
monkey.patch_all()
from bottle import route, run, template


@route('/')
def index():
    return '<h1>pyweb</h1>'


@route('/ping')
def health():
    return 'ok'


@route('/status')
def status():
    result = {
        'bottle': 'UP'
    }
    return result


@route('/v1/<action>/<param>')
def apiv1(action, param):
    return template('<b>{{action}} {{param}}</b>!', action=action, user=param)

# run(server='gunicorn', host='0.0.0.0', port=8080, workers=4)
run(host='0.0.0.0', port=8080, server='gevent')
