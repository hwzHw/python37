from wsgiref.simple_server import make_server


def findall():
    return ["<h1>Findall</h1>".encode("gbk")]


def findgood():
    return ["<h1>FindGood</h1>".encode("gbk")]


def findbad():
    return ["<h1>FindBad</h1>".encode("gbk")]


urls = (
    ("/findall/", findall),
    ("/findgood/", findgood),
    ("/findbad/", findbad)

)


def RunServer(env,response):
    url = env["PATH_INFO"]
    func = None

    for item in urls:
        if item[0] == url:
            func = item[1]
            break
    if func:
        res = func()
    else:
        res = [b"<h1>404</h1>"]
    headers = [("Content-type", "text/html")]
    response("200 OK", headers)
    print(res)
    return res


if __name__ == "__main__":
    httpd = make_server("", 9000, RunServer)
    print("Start")
    httpd.serve_forever()
