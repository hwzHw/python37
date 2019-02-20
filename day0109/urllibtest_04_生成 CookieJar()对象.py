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

# 构建一个 CookieJar 对象实例来保存 cookie
cookiejar = http.cookiejar.CookieJar()
# 使用 HTTPCookieProcessor()来创建 cookie 处理器对象，参数为 CookieJar()对象
handler=request.HTTPCookieProcessor(cookiejar)
# 通过 build_opener() 来构建 opener
opener = request.build_opener(handler)
# 4. 以 get 方法访问页面，访问之后会自动保存 cookie 到 cookiejar 中
opener.open("https://www.baidu.com")
## 可以按标准格式将保存的 Cookie 打印出来
cookieStr = ""
for item in cookiejar:
    cookieStr = cookieStr + item.name + "=" + item.value + ";"
## 舍去最后一位的分号
print(cookieStr[:-1])



