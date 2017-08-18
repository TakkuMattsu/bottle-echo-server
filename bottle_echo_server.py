from bottle import route, run, template, request
from bottle import static_file
from datetime import datetime as dt

@route('/', method='GET')
@route('/', method='POST')
def index():
    tstr = '2012-12-29 13:49:37'
    tdatetime = dt.strptime(tstr, '%Y-%m-%d %H:%M:%S')
    print('{0} {1} -> {2}'.format(tdatetime, request.method, request.url))
    print('header -> {0}'.format(dict(request.headers)))
    print('body -> {0}'.format(request.body.read().decode('utf-8')))
    print()
    return template('index')

@route('/favicon.ico', method='GET')
def get_favicon():
    return static_file('favicon.ico', root='./static')

run(host='0.0.0.0', port=8080, reloader=True)
