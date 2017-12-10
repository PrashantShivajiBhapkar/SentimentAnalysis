import cherrypy

class Politics(object):
	"""docstring for Politics"""

	def __init__(self):
<<<<<<< HEAD
		print ('this is about politics')
=======
>>>>>>> ae997cf7366ced46f8f8ca0d040237fa98deb6f6
		pass

	@cherrypy.expose
	def index(self):
		return 'This is index page of politics'

	@cherrypy.expose
	def trump(self):
		return 'This is index page of trump'
