from settings import ROOT_DIR
from views import index

def setup_routes(app):
    app.router.add_get('/', index, name='index')
    app.router.add_get('/index', index)

def setup_static_routes(app):
    app.router.add_static('/static/',
                        path = ROOT_DIR / 'static',
                        name = 'static')