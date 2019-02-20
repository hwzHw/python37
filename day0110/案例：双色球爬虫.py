import requests
from lxml import etree

url = 'http://zst.aicai.com/ssq/openInfo/'
head={}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
start_page = 1
end_page = 2

for page in range(start_page,end_page+1):
    print('current page:',page)
    form_data = {
        "maxsize": 100,
        "sortTag": "down",
        "currentPage": page,
        "pageSize": 30,
        "gameIndex": 101,
        "pageInfo": "openInfo",
    }

    response = requests.post(url,data=form_data,headers=head)
    html = response.text
    #print(html)
    # 数据的提取
    html = etree.HTML(html)
    #print(html.tostring())
    ls = html.xpath('//tr')
    ls.pop(0)
    ls.pop(0)
    print(len(ls))

    for item in ls:
        num = item.xpath('./td')[0].text
        print('期号：',num)

        pub_date = item.xpath('./td')[1].text
        print('日期：',pub_date)

        red_ball = item.xpath('./td')[2].text +" "+item.xpath('./td')[3].text +" "+item.xpath('./td')[4].text +" "+item.xpath('./td')[5].text +" "+item.xpath('./td')[6].text +" "+item.xpath('./td')[7].text
        print('红色球：', red_ball)

        blue_ball = item.xpath('./td')[8].text
        print('蓝色球：', blue_ball)

        sum = item.xpath('./td')[9].text
        print('总投注额数：', sum)

        first_nums = item.xpath('./td')[10].text
        print('一等奖注数：', first_nums)
        first_prize = item.xpath('./td')[11].text
        print('一等奖奖金：', first_prize)
        second_nums = item.xpath('./td')[12].text
        print('二等奖注数：', second_nums)
        second_prize = item.xpath('./td')[13].text
        print('二等奖奖金：', second_prize)
        pool_prize = item.xpath('./td')[14].text
        print('奖池滚存（元）：', pool_prize)

        with open('./data/shuanseqiu.txt','a',encoding='utf-8') as file:
            file.write(num+','+pub_date+','+red_ball+','+blue_ball+','+sum+','+first_nums+','+first_prize+','+second_nums+','+second_prize+','+pool_prize+'\n')




