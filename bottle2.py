from bottle import app, route, run, static_file, template, url

@route('/')
def main():
  return static_file('index.html', root='.')

@route('/static/<filename>', name='static')
def static(filename):
  return static_file(filename, root='static')

#hostip='192.168.0.129'
#apparently 0.0.0.0 accepts connection from any host. Using the actual IP address also works but seems less portable.
hostip='0.0.0.0'
run(host=hostip, port=9999)
