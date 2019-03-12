from http.server import HTTPServer,BaseHTTPRequestHandler
import os
import re
from urllib import parse


class RequestCallBack(BaseHTTPRequestHandler):
    def do_POST(self):
        print("收到POST")

    def do_GET(self):
        path = parse.urlparse(self.path).path
        query = parse.urlparse(self.path).query
        if path =="/favicon.ico":
            return
        filename ="weebroot"+path
        if filename == "weebroot/":
            filename = "weebroot/indexes.html"
        if not os.path.exists(filename):
            return
        self.send_response(200)
        self.send_header("Content-Type","text/html")
        self.end_headers()
        html = """
        <html>
             <head>
                  <meta charset="utf8">
             </head>
             <body>
                  <h1>返回的页面</h1>
             </body>
        </html>
        """
        # with open(filename,"r",charset="utf-8") as f:
        #     filestr = f.read()
        #     filestr = re.sub("{%.*?%}",query,filestr)
        #     self.wfile.write(filestr.encode("utf8"))
        self.wfile.write(html.encode("utf8"))
        root = "weebroot"
        with open(root+self.path,"r",encoding="utf8") as f:
            self.wfile.write(f.read().encode("utf8"))


saddr = ("192.168.15.6", 8080)
server = HTTPServer(saddr, RequestCallBack)
server.serve_forever()
