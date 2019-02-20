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
<p class="title story" name="dromouse"><b>The Dormouse's story</b></p><p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#创建 Beautiful Soup 对象
soup = BeautifulSoup(html,'lxml')
print(type(soup))
print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.a)
print(soup.p)
print(type(soup.p))
print('==========================')
#soup 对象本身比较特殊，它的 name 即为 [document]
print(soup.name)
print(soup.head.name)
#把p标签的所有属性打印输出了出来，得到的类型是一个字典。
print(soup.p.attrs)
#根据名称获取对应的属性值，类型为列表
print(soup.p['class'])
print(soup.p.get('class'))  # 等效的
print(soup.p['name'])
# 可以对这些属性和内容等等进行修改
soup.p['class'] = "newClass"
soup.p['class2'] = "newClass2"
print(soup.p)
# 删除属性
del soup.p['class']
print(soup.p)
print('==========================')
#创建 Beautiful Soup 对象
soup = BeautifulSoup(html,'lxml')
#获取标签内部的文字
print('获取标签内部的文字:')
print(soup.p.string)
print(type(soup.p.string))
print('==========================')
#创建 Beautiful Soup 对象
soup = BeautifulSoup(html,'lxml')
print('演示Beautiful Soup 对象:')
print(type(soup))
print(soup.name)
print(soup.attrs)

p = soup.p
print(p)
print(type(p))
print('==========================')
#创建 Beautiful Soup 对象
soup = BeautifulSoup(html,'lxml')
print('演示comment 对象:')
print(soup.a)
print(soup.a.string)
print(type(soup.a.string))

print('==========================')
ls = soup.select('p')
for it in ls:
    print(it.string)