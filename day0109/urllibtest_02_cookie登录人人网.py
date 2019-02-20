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
from urllib import parse
import chardet

# _o ：去掉
Request_URL="http://www.renren.com/966924492"
head = {}
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400'
head['Cookie']='anonymid=jhsxb2breoia7; _r01_=1; _de=32B20555AD3784A6BF2D3D01B72FE013; ln_uact=17752558702; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=bbeaa27f-d9ca-4b24-84bb-7c1a63164ca5%7C077a3e2b1c00096d5c13732ceee74ce5%7C1546657316365%7C1%7C1546657318223; depovince=HEN; JSESSIONID=abc-nqCo2n4BCeG2jCXGw; ick_login=fa69aec0-393a-4767-ab31-4f3dde23e2cf; jebecookies=52e4a003-daea-4a7c-83ec-24e11ccd84ce|||||; p=c576416c36979076d9635e049916a4ad2; first_login_flag=1; t=88450b49fb14139f7d0430e4f8a399992; societyguester=88450b49fb14139f7d0430e4f8a399992; id=966924492; xnsid=ce889ac7; ver=7.0; loginfrom=null; jebe_key=bbeaa27f-d9ca-4b24-84bb-7c1a63164ca5%7C077a3e2b1c00096d5c13732ceee74ce5%7C1546657316365%7C1%7C1547018142072; wp_fold=0'

#定义request对象
req = request.Request(Request_URL,headers=head)
#用post方法进行请求，指定data参数
response = request.urlopen(req)
html = response.read()
charset = chardet.detect(html)['encoding']
html = html.decode(charset)
print(html)

