# Researching Bottle

from bottle import route, default_app, run, request, error


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
