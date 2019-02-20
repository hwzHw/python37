from urllib import request
from urllib import parse
from lxml import etree


def tiebaSpider(url, startPage, endPage, name):

    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}
    barname = name
    num = 1 #图片文件的索引
    # 页面的循环
    for page in range(startPage, endPage + 1):
        pn = (page - 1) * 50
        fullurl = url + "&pn=" + str(pn)
        # 请求指定的页面
        print('请求页面，页码是：', page)
        req = request.Request(fullurl, headers=headers)
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        # 数据提取
        selector = etree.HTML(html)
        ls = selector.xpath('//li[contains(@class,"j_thread_list clearfix")]')
        print('ls len:', len(ls))
        base_url = 'https://tieba.baidu.com'
        for link in ls:
            url = base_url + link.xpath('.//div[contains(@class,"threadlist_title pull_left j_th_tit")]/a/@href')[0]
            print('url:', url)
            req = request.Request(url,headers=headers)
            response = request.urlopen(req)
            html = response.read()
            selector = etree.HTML(html)
            image_links = selector.xpath('//img[@class="BDE_Image"]/@src')
            # 依次下载帖子中图片
            for image_link in image_links:
                # 下载图片
                image = request.urlopen(image_link).read()
                # 打开文件，保存图片
                image_file = './images/'+barname+"_"+ str(num) + ".png"
                print('下载文件：',image_file)
                with open(image_file,'wb') as file:
                    file.write(image)
                    num+=1

    print('down end.')


if __name__ == '__main__':
    tiebaname = input('请输入贴吧名称：')
    startPage = int(input('请输入起始页码：'))
    endPage = int(input('请输入终止的页码：'))

    url = 'https://tieba.baidu.com/f?'
    kw = {'kw':tiebaname}
    kw = parse.urlencode(kw)
    print(kw)
    url = url + kw
    print(url)
    tiebaSpider(url,startPage,endPage,tiebaname)






