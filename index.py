#!/usr/bin/env python

import operator, os, sys
import cherrypy
from public.py import Politics
from genshi.template import TemplateLoader

loader = TemplateLoader(
    os.path.join(os.path.dirname(__file__), 'public/html'),
    auto_reload=True
)

class Root(object):

    def __init__(self):
        self.politics = Politics.Politics()

    @cherrypy.expose
    def index(self):
        tmpl = loader.load('index.html')
        return tmpl.generate(title='Geddit').render('html', doctype='html')

def main():

    root = Root()

    # Some global configuration; note that this could be moved into a
    # configuration file
    cherrypy.config.update(
        {
            'tools.encode.on': True, 'tools.encode.encoding': 'utf-8',
            'tools.decode.on': True,
            'tools.trailing_slash.on': True,
            'tools.staticdir.root': os.path.abspath(os.path.dirname(__file__)),
        }
    )

    config = {
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }

    app = cherrypy.tree.mount(root, "/", config)

    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == '__main__':
    main()