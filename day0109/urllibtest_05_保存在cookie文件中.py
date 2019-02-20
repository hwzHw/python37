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
import http.cookiejar
from urllib import request

#保存 cookie 的本地磁盘文件名
filename = './data/cookie.txt'
#1. 声明一个 MozillaCookieJar(有 save 实现)对象实例来保存 cookie，之后写入文件
cookiejar = http.cookiejar.MozillaCookieJar(filename)
#2. 使用 HTTPCookieProcessor()来创建 cookie 处理器对象，参数为 CookieJar()对象
handler = request.HTTPCookieProcessor(cookiejar)
#3. 通过 build_opener() 来构建 opener
opener = request.build_opener(handler)
#4. 创建一个请求，原理同 urllib2 的 urlopen
response = opener.open("https://www.baidu.com")
#5. 保存 cookie 到本地文件
cookiejar.save()


