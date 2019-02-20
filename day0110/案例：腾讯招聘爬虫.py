"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2019/1/10'
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
from bs4 import BeautifulSoup


def tencent():
    # 1、页面请求
    url='https://hr.tencent.com/position.php?&start=10#a'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
    req = request.Request(url,headers=headers)
    response = request.urlopen(req)
    html = response.read()
    # 数据提取
    html = BeautifulSoup(html, 'lxml')
    # 通过css选择器提取数据
    result = html.select('table[class="tablelist"] > tr')
    result.pop()
    result.pop(0)
    print(len(result))
    for item in result:
        name = item.select('td > a')[0].get_text()
        datail_url = item.select('td > a')[0].attrs['href']
        cate = item.select('td')[1].get_text()
        nums = item.select('td')[2].get_text()
        city = item.select('td')[3].get_text()
        pub_date = item.select('td')[4].get_text()
        print(("职位名称：", name), datail_url, cate, nums, city, pub_date)


if __name__ == "__main__":
    tencent()
