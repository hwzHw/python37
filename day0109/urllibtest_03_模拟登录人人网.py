"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/17'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from urllib import request
from urllib import parse
import chardet
import http.cookiejar


# 1. 构建一个 CookieJar 对象实例来保存 cookie
cookie = http.cookiejar.CookieJar()
# 2. 使用 HTTPCookieProcessor()来创建 cookie 处理器对象，参数为 CookieJar()对象
cookie_handler = request.HTTPCookieProcessor(cookie)
# 3. 通过 build_opener() 来构建 opener
opener = request.build_opener(cookie_handler)
# 4. addheaders 接受一个列表，里面每个元素都是一个 headers 信息的元祖, opener 将附带headers 信息
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]
# 5. 需要登录的账户和密码
data = {"email":"17752558702", "password":"qikuedu9527"}
# 6. 通过 urlencode()转码
postdata = parse.urlencode(data).encode(encoding='UTF8')
print(postdata)
# 7. 构建 Request 请求对象，包含需要发送的用户名和密码
req = request.Request("http://www.renren.com/PLogin.do", data = postdata)
# 8. 通过 opener 发送这个请求，并获取登录后的 Cookie 值，
opener.open(req)
# 9. opener 包含用户登录后的 Cookie 值，可以直接访问那些登录后才可以访问的页面
response = opener.open("http://www.renren.com/966924492/")
# 10. 打印响应内容
print(response.read().decode())

