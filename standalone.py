# Researching Bottle

# from gevent import monkey
# monkey.patch_all()
from bottle import route, run, template


@route('/v1/<action>/<param>')
def apiv1(action, param):
    return template('<b>{{action}} {{param}}</b>!', action=action, param=param)


@route('/object/<id:int>')
def callback(id):
    assert isinstance(id, int)

if __name__ == '__main__':
    run(server='gunicorn', host='0.0.0.0', port=8080, workers=4)
    # run(host='0.0.0.0', port=8080, server='gevent')
