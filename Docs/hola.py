from bottle import route, run, templates

@route('/hola/juan')
def hola(juan):
	return templates('<b>Hola {{juan}}</b!', name=juan)
"""
	@route('/')
	def index():
		return templates('<b>Hola mundo<b/>!')
"""
	run(host='localhost', port=9000)