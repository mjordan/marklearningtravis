from bottle import route, template

@route('/hello')
def index():
    return template('Hello')

