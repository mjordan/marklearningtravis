"""
Simple Bottle script that returns 'Hello' to the HTTP client.
Configured to run as a WSGI application under Apache, using
the accompanying wsgi.conf.
"""
import bottle
from bottle import route, template

@route('/hello')
def hello():
    return template('Hello')

application = bottle.default_app()
