from wsgiref.simple_server import make_server


# The WSGI application handler function
def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)

    # The response body returned by the application
    return [b'Hello, world! This is a WSGI application.']


# Create a WSGI server based on our application
with make_server('', 8000, simple_app) as httpd:
    print('Starting the WSGI server...')
    # Start the server and process requests
    httpd.serve_forever()
