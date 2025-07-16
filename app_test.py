import cherrypy
from webtest import TestApp
from app import HomePage 

def make_app():
    cherrypy.tree.mount(HomePage(), '/', {
        '/static': {
            'tools.staticdir.dir': './public',
            'tools.staticdir.on': True,
        }
    })
    return TestApp(cherrypy.tree)

def test_index():
    app = make_app()
    response = app.get('/')
    assert response.status_code == 200

def test_showcase():
    app = make_app()
    response = app.get('/showcase')
    assert response.status_code == 200

def test_projects():
    app = make_app()
    response = app.get('/projects')
    assert response.status_code == 200