import cherrypy

class Politics(object):
	"""docstring for Politics"""

	def __init__(self):
		pass

	@cherrypy.expose
	def index(self):
		return 'This is index page of politics'

	@cherrypy.expose
	def trump(self):
		return 'This is index page of trump'