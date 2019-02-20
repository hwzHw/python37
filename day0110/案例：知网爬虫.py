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
'''
需求：
知网爬虫：
爬取作者，链接，标题，期刊等
存储到mysql数据库中
'''

import requests
import pymysql
from lxml import etree

def get_html(url,para_data):
    headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
    content = requests.get(url,params=para_data)
    return content


if __name__ == "__main__":
    keyword ="人工智能" #要查找的关键字
    base_url = 'https://www.cn-ki.net'
    max_page = 2   #最大爬取的页数
    page = 1
    data = {
        'keyword':keyword,
        'db':'SCDB'
    }

    #链接数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='dbcnki1809', charset='utf8')
    cursor = conn.cursor()

    content = get_html(base_url+'/search',data)

    while page<=max_page:
       print('page:',page)
       tree = etree.HTML(content.text)
       ls = tree.xpath('//div[@class="mdui-col-xs-12 mdui-col-md-9 mdui-typo"]')
       print(len(ls))
       for item in ls:
           detail_url = item.xpath('./h3/a/@href')[0]
           detail_url = base_url + detail_url
           print('detail_url:',detail_url)
           con = get_html(detail_url,None).text
           h = etree.HTML(con)
           print('test:',con)
           print('test:', h.xpath('//span[@class="headline"]/text()')[0])
           print('test:', h.xpath('//v-container[@class="body-1 grey--text text--darken-2"]/v-layout/v-flex[2]/text()')[0].strip())

           title = item.xpath('./h3/a//text()')
           title = ''.join(title)
           print('title:',title)

           author = item.xpath('./div[1]/span[1]/text()')[0]
           print('author:',author)

           periodal= item.xpath('./div[1]/span[3]/text()')[0]
           print('periodal:',periodal)

           pub_date = item.xpath('./div[1]/span[4]/text()')[0]
           print('pub_date:',pub_date)

           type = item.xpath('./div[1]/span[5]/text()')[0]
           print('type:',type)

           summary = item.xpath('./div[@class="mdui-col-xs-12 mdui-typo"]/p//text()')
           if len(summary)>0:
               summary = ''.join(summary)
               summary = summary.strip()
           else:
               summary = '空'
           print('summary:',summary)
           print('='*60)

           strsql='Insert into tb_cnki VALUES (0,%s,%s,%s,%s,%s,%s,%s)'
           parmams = [detail_url,title,author,periodal,pub_date,type,summary]
           cursor.execute(strsql,parmams)
           conn.commit()

       page+=1
       if page <= max_page:
           nextbtn=tree.xpath('//div[@class="mdui-col-xs-9 TitleLeftCell mdui-valign"]/a[last()]')
           if len(nextbtn)>0:
               if nextbtn[0].text == '下一页':
                   page_url = nextbtn[0].attrib['href']
                   page_url = base_url +'/'+ page_url
                   print(page_url)
                   content = get_html(page_url,'')

    #关闭数据库
    cursor.close()
    conn.close()




