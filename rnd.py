from bottle import route, run, template

@route('/')
def index():
    return '<h1>pyweb</h1>'

@route('/<action>/<user>')
def user_api(action, user):
    return template('<b>{{action}} {{user}}</b>!', action=action, user=user)

run(host='0.0.0.0', port=8080)