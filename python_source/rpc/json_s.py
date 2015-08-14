import pyjsonrpc

class RequestHandler(pyjsonrpc.HttpRequestHandler):

    @pyjsonrpc.rpcmethod
    def add(self, a, b):
        print 'R:add'
        return a + b
    
    @pyjsonrpc.rpcmethod
    def echo(self, msg):
        print 'R:echo'
        print 'test'
        return msg
    
    @pyjsonrpc.rpcmethod
    def hello(self):
        print 'R:hello'
        return 'hello'
  

# Threading HTTP-Server
http_server = pyjsonrpc.ThreadingHttpServer(
    server_address=('localhost', 8080),
    RequestHandlerClass=RequestHandler
)

print "Starting HTTP server ..."
print "URL: http://localhost:8080"

http_server.serve_forever()
