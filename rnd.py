from bottle import route, run, template

@route('/')
def index():
    return '<h1>pyweb</h1>'

@route('/health')
def index():
    return 'ok'

@route('/v1/<action>/<param>')
def user_api(action, param):
    return template('<b>{{action}} {{param}}</b>!', action=action, user=param)

run(host='0.0.0.0', port=8080)