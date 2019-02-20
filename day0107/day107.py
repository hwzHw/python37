from urllib import request
import urllib.request
import urllib.parse
import os
url = 'https://www.baidu.com/'
#输入吧名，输入起始页码，输入结束页码，
# 然后在当前文件夹中创建一个以吧名为名字的文件夹，
# 里面是每一页的html内容，文件名是吧名_page.html
ba_name = input('请输入要爬取的吧名:')
start_page = int(input('请输入要爬取的起始页码：'))
end_page = int(input('请输入要爬取得结束页码：'))
#创建文件夹
if not os.path.isdir(ba_name):
    os.mkdir(ba_name)
#依次爬取每一页数据
for page in range(start_page, end_page+1):
    #page就是当前页
    #拼接url的过程
    data = {
        'kw': ba_name,
        'pn': (page - 1) * 50
    }

    data = urllib.parse.urlencode(data)
    #生成指定的url
    url_t = url + data
    print(url_t)
    herders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }
    request = urllib.request.Request(url=url_t, headers=herders)
    print('%s页开始进行下载' % page)
    response = urllib.request.urlopen(request)
    #生成文件名
    filename = ba_name+'_'+str(page)+'.html'
    #拼接文件路径
    filepath = ba_name+'/'+filename
    #写内容
    with open(filepath, 'wb') as fp:
        fp.write(response.read())
