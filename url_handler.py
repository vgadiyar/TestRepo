import bottle

@bottle.route('/')
@bottle.route('/index');
def home_page():
	return "Hello, Baruch\n"

@bottle.route('/testpage')
def test_page():
	return "this is a test page"

bottle.debug(True)
bottle.run(host='localhost', port=8080)
