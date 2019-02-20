"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/13'
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

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2" aa='123'>Lacie</a> and
<a href="http://example.com/tillie" class="sister2" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#创建 Beautiful Soup 对象
soup = BeautifulSoup(html,'lxml')
# 传字符串
print('查找字符串：')
print(soup.find_all('b'))
print(soup.find_all('a'))
print('==========================')
#传正则表达式
print('传正则表达式：')
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
print('==========================')
print('列表：')
print(soup.find_all(["a", "b"]))
print('==========================')
#keyword 参数
print('keyword 参数：')
print(soup.find_all(id='link2'))
print(soup.find_all(class_='sister'))
print(soup.find_all(href='http://example.com/lacie'))
print(soup.find_all(aa='123'))
print('==========================')
#text 参数
print('text 参数：')
print(soup.find_all(text="Elsie"))
print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))
print(soup.find_all(text=re.compile("Dormouse")))




