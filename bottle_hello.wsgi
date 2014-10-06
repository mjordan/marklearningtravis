import sys
from bottle import route, template

sys.path.append("lib")

@route('/hello')
def hello():
    return template('Hello')

application = bottle.default_app()
