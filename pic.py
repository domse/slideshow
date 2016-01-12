from bottle import route, run, template, static_file
from glob import glob

@route('/')
def index():
	res = ''
	list = glob("./data/picture/*.JPG")
	for obj in list:
		res += obj[15:] + ' '
	return res
	
@route('/image/<filename:re:.*\.jpg>')
def image(filename):
	return static_file(filename, root='./data/picture/', mimetype='image/jpg')

run(host='localhost', port=8080)