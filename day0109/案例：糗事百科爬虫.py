"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2019/1/9'
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
from lxml import  etree
import chardet
from urllib import error


page=1
url='https://www.qiushibaike.com/8hr/page/1/'
headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}

try:
    req = request.Request(url,headers=headers)
    response = request.urlopen(req)
    resHtml = response.read()
    #resHtml = resHtml.decode()
    html = etree.HTML(resHtml)
    ls = html.xpath('//li[contains(@id,"qiushi_tag")]')
    print(len(ls))
    for item in ls:
        imgurl = item.xpath('./a/img/@src')
        if len(imgurl)>0:
            imgurl = imgurl[0]
        else:
            imgurl = '未知'
        print('imgurl:',imgurl)
        title = item.xpath('.//a[@class="recmd-content"]')[0]
        detailUrl = title.xpath('@href')[0]
        print('detail url:',detailUrl)
        title = title.text
        print('title:',title)
        author = item.xpath('.//span[@class="recmd-name"]/text()')[0]
        print('author:',author)
        portrait = item.xpath('.//a[@class="recmd-user"]/img/@src')[0]
        print('portrait:',portrait)
        tmp = item.xpath('.//div[@class="recmd-num"]/span')
        votenum = tmp[0].text
        print("votenum:",votenum)
        comments=0
        if len(tmp)>=5:
            comments = tmp[3].text
        print('comments:',comments)

except error.URLError as e:
    print(e)

