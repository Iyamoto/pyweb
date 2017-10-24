from bottle import route, run, template


@route('/')
def index():
    return '<h1>pyweb</h1>'


@route('/ping')
def health():
    return 'ok'


@route('/v1/<action>/<param>')
def apiv1(action, param):
    return template('<b>{{action}} {{param}}</b>!', action=action, user=param)

run(server='gunicorn', host='0.0.0.0', port=8080)
