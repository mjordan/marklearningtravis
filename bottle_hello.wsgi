import bottle
from bottle import route, template

@route('/hello')
def hello():
    return template('Hello')

application = bottle.default_app()
