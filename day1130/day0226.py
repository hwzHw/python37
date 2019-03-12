#
# @Time    : 2019/2/26 20:33
# @Author  : Mat
# @壮      ：Very Cool
# @File    : day0226.py
# @Software: PyCharm
#  ......................我佛慈悲......................
#                        _oo0oo_
#                       o8888888o
#                       88" . "88
#                       (| -_- |)
#                       0\  =  /0
#                     ___/`---'\___
#                   .' \\|     |// '.
#                  / \\|||  :  |||// \
#                 / _||||| -卍-|||||- \
#                |   | \\\  -  /// |   |
#                | \_|  ''\---/''  |_/ |
#                \  .-\__  '-'  ___/-. /
#              ___'. .'  /--.--\  `. .'___
#           ."" '<  `.___\_<|>_/___.' >' "".
#          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#          \  \ `_.   \_ __\ /__ _/   .-` /  /
#      =====`-.____`.___ \_____/___.-`___.-'=====
#                        `=---='
#
# ..................佛祖开光 ,永无BUG...................
# ..................佛祖保佑，永不加班...................
from wsgiref.simple_server import make_server


def login():
    return ['<h1>Hello</h1>'.encode('utf-8')]


def register():
    return ['<h1>World</h1>'.encode('utf-8')]


def list_user():
    return ['<h1>Hello World</h1>'.encode('utf-8')]


def app(env, response):
    response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    path = env['PATH_INFO'][1:]
    if path == 'login':
        return login()
    elif path == 'register':
        return register()
    elif path == 'list_user':
        return list_user()
    else:
        return ['<h1 style="text-align: center; color: yellow;">迪迦奥特曼</h1>'.encode('utf-8')]


httpd = make_server('', 8080, app)
print('server running......')
httpd.serve_forever()