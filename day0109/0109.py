# 什么是 cookie？什么是session？
# 1. 什么是Cookie
# Cookie是HTTP协议的规范之一，它是服务器和客户端之间传输的小数据。
# 首先由服务器通过响应头把Cookie传输给客户端，客户端会将Cookie保存起来。
# 当客户端再次请求同一服务器时，客户端会在请求头中添加该服务器保存的Cookie，发送给服务器。
#  Cookie就是服务器保存在客户端的数据！
#  Cookie就是一个键值对！！！
# 2. Cookie规范
# Cookie通过请求头和响应头在服务器与客户端之间传输；
# Cookie大小限制在4KB之内；
# 一台服务器在一个客户端最多保存20个Cookie；
# 一个浏览器最多可以保存300个Cookie；
# 1.什么是session
#
# 在WEB开发中，服务器可以为每个用户浏览器创建一个会话对象（session对象），
# 注意：一个浏览器独占一个session对象(默认情况下)。因此，
# 在需要保存用户数据时，服务器程序可以把用户数据写到用户浏览器独占的session中，
# 当用户使用浏览器访问其它程序时，其它程序可以从用户的session中取出该用户的数据，为用户服务。
# session与浏览器
#  session对象是保存在服务器端的，而sessionId是通过Cookie保存在客户端的。
#  因为Cookie不能在多个浏览器中共享，所以session也不能在多个浏览器中共享。
# 也就是说，使用IE登录后，再使用FireFox访问服务器还是没有登录的状态。


# 常见状态代码、状态描述、说明：
# 200 OK?????//客户端请求成功
# 400 Bad Request? //客户端请求有语法错误，不能被服务器所理解
# 401 Unauthorized //请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用
# 403 Forbidden? //服务器收到请求，但是拒绝提供服务
# 404 Not Found? //请求资源不存在，eg：输入了错误的URL
# 500 Internal Server Error //服务器发生不可预期的错误
# 503 Server Unavailable? //服务器当前不能处理客户端的请求，一段时间后可能恢复正常

# 2、get 方法和 post 方法的区别？
# 提交参数的位置不同：
# GET 提交的数据会放在 URL 之后，以?分割 URL 和传输数据，参数之间以&相连，如
# POST 方法是把提交的数据放在 HTTP 包的 Body 中。
# 提交参数的大小不同（理论上，存在争议）：
# GET 提交的数据大小有限制（因为浏览器对 URL 的长度有限制），这点要根据实际情况而论，目前浏览器种类比较多，不同的浏览器大小限制不同。
# POST 方法提交的数据理论上没有限制，但是不建议太大。
# 安全问题上：
# GET 方式提交数据，会带来安全问题，因为参数是裸露在地址栏上，所以较不安全。
# POST 方式参数在 body 中，所以安全性较高（注意：只是较高，不是很安全，在 http协议下，不管哪种提交方式，都是明码提交，只要有抓包工具，都能抓取数据的！！！）
# 是否浏览器可以收藏
# GET 请求因为参数在地址栏上，因此可以收藏（因为参数也会保存啊）。
# POST 请求不行，不能被浏览器收藏，因为参数无法被浏览器保存。


from urllib import request
from urllib import parse
import chardet
import http.cookiejar
# 1、用cookie模拟登录人人网
# Request_URL="http://www.renren.com/966924492"
# head = {}
# head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400'
# head['Cookie']='anonymid=jhsxb2breoia7; _r01_=1; _de=32B20555AD3784A6BF2D3D01B72FE013; ln_uact=17752558702; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=bbeaa27f-d9ca-4b24-84bb-7c1a63164ca5%7C077a3e2b1c00096d5c13732ceee74ce5%7C1546657316365%7C1%7C1546657318223; depovince=HEN; JSESSIONID=abc-nqCo2n4BCeG2jCXGw; ick_login=fa69aec0-393a-4767-ab31-4f3dde23e2cf; jebecookies=52e4a003-daea-4a7c-83ec-24e11ccd84ce|||||; p=c576416c36979076d9635e049916a4ad2; first_login_flag=1; t=88450b49fb14139f7d0430e4f8a399992; societyguester=88450b49fb14139f7d0430e4f8a399992; id=966924492; xnsid=ce889ac7; ver=7.0; loginfrom=null; jebe_key=bbeaa27f-d9ca-4b24-84bb-7c1a63164ca5%7C077a3e2b1c00096d5c13732ceee74ce5%7C1546657316365%7C1%7C1547018142072; wp_fold=0'
#
# #定义request对象
# req = request.Request(Request_URL,headers=head)
# #用post方法进行请求，指定data参数
# response = request.urlopen(req)
# html = response.read()
# charset = chardet.detect(html)['encoding']
# html = html.decode(charset)
# print(html)



# 2、利用cookie和post模拟登录人人网个人主页

# 1. 构建一个 CookieJar 对象实例来保存 cookie
# cookie = http.cookiejar.CookieJar()
# # 2. 使用 HTTPCookieProcessor()来创建 cookie 处理器对象，参数为 CookieJar()对象
# cookie_handler = request.HTTPCookieProcessor(cookie)
# # 3. 通过 build_opener() 来构建 opener
# opener = request.build_opener(cookie_handler)
# # 4. addheaders 接受一个列表，里面每个元素都是一个 headers 信息的元祖, opener 将附带headers 信息
# opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
#                                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]
# # 5. 需要登录的账户和密码
# data = {"email":"17752558702", "password":"qikuedu9527"}
# # 6. 通过 urlencode()转码
# postdata = parse.urlencode(data).encode(encoding='UTF8')
# print(postdata)
# # 7. 构建 Request 请求对象，包含需要发送的用户名和密码
# req = request.Request("http://www.renren.com/PLogin.do", data = postdata)
# # 8. 通过 opener 发送这个请求，并获取登录后的 Cookie 值，
# opener.open(req)
# # 9. opener 包含用户登录后的 Cookie 值，可以直接访问那些登录后才可以访问的页面
# response = opener.open("http://www.renren.com/966924492/")
# # 10. 打印响应内容
# print(response.read().decode())

# 3、用cookie模拟登录微博
Request_URL="https://weibo.com/u/5885869521/home?wvr=5"
head = {}
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400'
head['Cookie']='SINAGLOBAL=8761444336935.016.1543835803707; login_sid_t=ace5776bfc8edd7618ede23be776881b; cross_origin_proto=SSL; ALF=1578563556; SSOLoginState=1547027557; _s_tentry=passport.weibo.com; SUB=_2A25xMbQ1DeRhGeNG41cZ9ifJyT2IHXVSRqL9rDV8PUNbmtAKLXT8kW9NSx9sYYFpbPhTGZyJ7FxVDKLglulMt4hZ; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFjcaJC2vs-9h6d84-_13jh5JpX5KzhUgL.Fo-R1h-RSo.feo22dJLoI0qLxKBLBonL12BLxKnLBKMLBKeLxKBLBonLB.2LxKBLB.BL1K-LxKnL1h5L12eLxK-LB.qL1K.t; SUHB=0gHiJVuJvXOuK9; wvr=6; Apache=3037666285527.294.1547027495933; ULV=1547027495950:3:1:1:3037666285527.294.1547027495933:1544613520966; UOR=baishi.baidu.com,widget.weibo.com,graph.qq.com'

#定义request对象
req = request.Request(Request_URL,headers=head)
#用post方法进行请求，指定data参数
response = request.urlopen(req)
html = response.read()
charset = chardet.detect(html)['encoding']
html = html.decode(charset)
print(html)