# 创建和启动服务器
from wsgiref.simple_server import make_server
def index(env, response):
	response("200 OK", [("Content-type", 	"text/html")])
	return [b"<h1>Hello Web!</h1>"]


httpd = make_server("", 8000, index)
print("web server starting……")
httpd.serve_forever()

