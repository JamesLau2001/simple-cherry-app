import cherrypy
import os
from jinja2 import Environment, FileSystemLoader
class HomePage(object):
    def __init__(self):
        self.env = Environment(
            loader=FileSystemLoader(os.path.join(os.getcwd(), 'templates'))
        )
    @cherrypy.expose
    def index(self):
        template = self.env.get_template('index.html')
        return template.render(link_url="/showcase", link_url1="/projects")
    @cherrypy.expose
    def showcase(self):
        template = self.env.get_template('showCaseSneakPeek.html')
        return template.render(link_url="/")
    @cherrypy.expose
    def projects(self):
        template = self.env.get_template('projects.html')
        return template.render(link_url="/")
    
if __name__ == '__main__':
    conf = {
        '/static': {
            'tools.staticdir.dir': './public',
            'tools.staticdir.on': True,
        }
    }
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(HomePage(), '/', conf)