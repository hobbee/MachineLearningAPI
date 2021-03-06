#!/usr/bin/env python

import cherrypy
import json
from controllers.automatic_tag import automatic_tag as auto_tag
from controllers.association import association as association

import glob
import os.path
import codecs
import re

'''
def find_all():
    for file in glob.glob('./models/resources/articles/*'):
        id = re.compile("[0-9]+").search(file).group(0)
        allLines = open(file, 'r', encoding='utf-8').read()
        yield (id, allLines)

'''
import sys
sys.path.append("./models/")
import model as Model
from model import model
from article import article

if __name__ == '__main__':
    Model.Base.metadata.create_all(Model.Engine)
    cherrypy.config.update({'server.socket_host': '0.0.0.0'
                       })
    cherrypy.tree.mount(
        auto_tag(), '/api/auto_tag',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    cherrypy.tree.mount(
        association(), '/api/association',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    cherrypy.engine.start()
    cherrypy.engine.block()

'''
    for item in find_all():
        article = articles(item[1])
        article.save()
'''
