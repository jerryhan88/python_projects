import pyjsonrpc

c = pyjsonrpc.HttpClient("http://localhost:8080")

print c.add(1, 2)
print c.echo("echo test")
print c.hello()
