from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from config import PORT, HOST

def log(request):
    if request.method == 'POST' and 'message' in request.POST:
        message = request.POST.get('message')
        print '\033[92m>>\033[0m' + message
    response = Response(status=200)
    response.headerlist.append(('Access-Control-Allow-Origin', '*'))
    return response

def main():
    config = Configurator()
    config.add_route('log', '/log')
    config.add_view(log, route_name='log')
    app = config.make_wsgi_app()
    return app

if __name__ == '__main__':
    app = main()
    server = make_server(HOST, PORT, app)
    server.serve_forever()