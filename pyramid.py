from wsgiref.simple_server import make_server
from jinja2 import Environment, FileSystemLoader
from pyramid.config import Configurator
from pyramid.response import Response


includes = [
                'app.js',
                'react.js',
                'leaflet.js',
                'D3.js',
                'moment.js',
                'math.js',
                'main.css',
                'bootstrap.css',
                'normalize.css',
            ]
environment = Environment(loader = FileSystemLoader('templates'))	   
css = []
js = []
def adding():
     for i in includes:
          if(i.split('.')[1] == 'css'):
              css.append(i)
      else:
              js.append(i)	    
      response = self.app(environ, start_response).decode() 
      return (response).encode()  	    
def Index(request):
     return Response(enviroment.get_template('/index.html').render({'styles':css,'scripts':js}))
def AboutMe(request):
    return Response(enviroment.get_template('/about/aboutme.html').render({'styles':css,'scripts':js}))
    
def app():
    conf = Configurator()
    conf.add_route('Index', '/index.html')
    conf.add_view(Index, route_name='Index')
    conf.add_route('AboutMe', '/about/aboutme.html')
    conf.add_view(AboutMe, route_name='AboutMe')
    return conf.make_wsgi_app()

if __name__ == '__main__':
    adding()
    ap=app()
    server = make_server('localhost', 8000, ap)
