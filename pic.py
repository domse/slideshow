from bottle import route, run, template, static_file, view
from glob import glob
import json

@route('/')
@view('slideshow_template')
def index():
	picset = set()
	picturelist = glob("./data/picture/*.jpg")
	for picture in picturelist:
		picset.add('/image/' + picture[15:])
	return dict(picturelist=picset)



@route('/list/')
def list():
	picset = set()
	picturelist = glob("./data/picture/*.jpg")
	for picture in picturelist:
		picset.add('/image/' + picture[15:])
	return json.dumps(list(picset))

@route('/image/<filename:re:.*\.jpg>')
def image(filename):
	return static_file(filename, root='./data/picture/', mimetype='image/jpg')

@route('/js/responsiveslides.min.js')
def slide():
	return static_file('responsiveslides.min.js', root='./data/js/', mimetype='text/javascript')

run(host='localhost', port=8080)
