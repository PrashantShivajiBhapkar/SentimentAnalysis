#!/usr/bin/env python

import operator, os, sys
import cherrypy
from public.py import Politics

class Root(object):

    def __init__(self):
        self.politics = Politics.Politics()
        # print (self.politics)

    @cherrypy.expose
    def index(self):
        return 'Geddit'

def main():

    root = Root()

    # Some global configuration; note that this could be moved into a
    # configuration file
    cherrypy.config.update({
        'tools.encode.on': True, 'tools.encode.encoding': 'utf-8',
        'tools.decode.on': True,
        'tools.trailing_slash.on': True,
        'tools.staticdir.root': os.path.abspath(os.path.dirname(__file__)),
    })

    app = cherrypy.tree.mount(root, "/")

    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == '__main__':
    main()
