from bottle import route, run, template, static_file
from glob import glob
import json

@route('/')
def index():
	picset = set()
	picturelist = glob("./data/picture/*.jpg")
	for picture in picturelist:
		picset.add('/image/' + picture[15:])
	return json.dumps(list(picset))

@route('/image/<filename:re:.*\.jpg>')
def image(filename):
	return static_file(filename, root='./data/picture/', mimetype='image/jpg')

run(host='localhost', port=8080)
