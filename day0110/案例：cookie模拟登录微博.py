# 获取一个有登录信息的Cookie模拟登陆
import requests
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    # 重点：这个Cookie是保存了密码无需重复登录的用户的Cookie，这个Cookie里记录了用户名，密码(通常经过RAS加密)
    "Cookie": "SINAGLOBAL=3302089224669.22.1472035369223; un=3414018462@qq.com; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5i18Aw7NyeAg6CaaNECPyx5JpX5KMhUgL.Foqceh50Sh27eK52dJLoIEXLxK-LBK-L1hMLxK-LBo5L12qLxK.L1h-LBoMLxK-LB.-LB--LxK-L12BL1-2t; UOR=www.yiihuu.com,widget.weibo.com,tech.ifeng.com; SCF=AvEvZ-N1Nn2fjE8sghEjOeRpXyJf2tw7T2O4uTOBuLqdwp2NTu-RwgJlc3DZATipWSG0BlFhr_HfLvXiU-xQ6qI.; SUB=_2A25xMv3xDeRhGeBI61IS9C_MyjyIHXVSRmg5rDV8PUNbmtAKLXXMkW9NRqLCt0eHzIjyobXLkbdJGMeS5TacNvUP; SUHB=0mxU0epBmcmRH1; ALF=1578615072; SSOLoginState=1547079073; Ugrow-G0=169004153682ef91866609488943c77f; YF-V5-G0=a2489c19ecf98bbe86a7bf6f0edcb071; YF-Page-G0=0dccd34751f5184c59dfe559c12ac40a; wb_view_log_6600341010=1920*10801; _s_tentry=-; Apache=7550862659276.177.1547079126724; ULV=1547079126748:152:3:2:7550862659276.177.1547079126724:1546872819981",
}
response = requests.get('https://weibo.com/u/6600341010/home?wvr=5&lf=reg',headers=headers)
print(response.text)