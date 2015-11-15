#!/usr/bin/env python

import cherrypy
import json
from controllers.automatic_tag import automatic_tag as auto_tag

if __name__ == '__main__':
    cherrypy.tree.mount(
        auto_tag(), '/api/auto_tag',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    cherrypy.engine.start()
    cherrypy.engine.block()
