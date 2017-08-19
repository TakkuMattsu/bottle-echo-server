from bottle import route, run, request, static_file
from datetime import datetime as dt

@route('/', method='GET')
@route('/', method='POST')
def index():
    tstr = '2012-12-29 13:49:37'
    tdatetime = dt.strptime(tstr, '%Y-%m-%d %H:%M:%S')
    result1 = '{0} {1} -> {2}'.format(tdatetime, request.method, request.url)
    result2 = 'header -> {0}'.format(dict(request.headers))
    result3 = 'body -> {0}'.format(request.body.read().decode('utf-8'))
    print(result1)
    print(result2)
    print(result3)
    print()
    return '{0}<br><br>{1}<br><br>{2}<br>'.format(result1, result2, result3)

@route('/favicon.ico', method='GET')
def get_favicon():
    return static_file('favicon.ico', root='./static')

run(host='0.0.0.0', port=8080, reloader=True)
