"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/5/30'
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

filename = './data/renrencookie.txt'
# 创建MozillaCookieJar(有load实现)实例对象
cookiejar = http.cookiejar.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookiejar.load(filename,ignore_discard=True,ignore_expires=True)
# 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
handler = request.HTTPCookieProcessor(cookiejar)
#通过 build_opener() 来构建opener
opener = request.build_opener(handler)
# addheaders 接受一个列表，里面每个元素都是一个headers信息的元祖, opener将附带headers信息
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"),
                     ]

for item in cookiejar:
    print(item.name + "=" + item.value + ";")



response = opener.open("http://www.renren.com/966924492/")
# 4. 打印响应内容
html = response.read()
charset = chardet.detect(html)['encoding']
print(charset)
print(html.decode(charset))

