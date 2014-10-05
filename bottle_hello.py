from bottle import route, run, template

@route('/hello')
def index():
    return template('Hello')

