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
import http.cookiejar
import chardet

# 创建 MozillaCookieJar(有 load 实现)实例对象
cookiejar = http.cookiejar.MozillaCookieJar()
# 从文件中读取 cookie 内容到变量
cookiejar.load('./data/cookie.txt')
# 使用 HTTPCookieProcessor()来创建 cookie 处理器对象，参数为 CookieJar()对象
handler = request.HTTPCookieProcessor(cookiejar)
#通过 build_opener() 来构建 opener
opener = request.build_opener(handler)
response = opener.open("https://www.baidu.com")
# 4. 打印响应内容
html = response.read()
charset = chardet.detect(html)['encoding']
print(charset)
print(html.decode(charset))





