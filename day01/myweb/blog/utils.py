#
# @Time    : 2019/3/4 14:31
# @Author  : Mat
# @壮      ：Very Cool
# @File    : utils.py
# @Software: PyCharm
#  ......................我佛慈悲......................
#                        _oo0oo_
#                       o8888888o
#                       88" . "88
#                       (| -_- |)
#                       0\  =  /0
#                     ___/`---'\___
#                   .' \\|     |// '.
#                  / \\|||  :  |||// \
#                 / _||||| -卍-|||||- \
#                |   | \\\  -  /// |   |
#                | \_|  ''\---/''  |_/ |
#                \  .-\__  '-'  ___/-. /
#              ___'. .'  /--.--\  `. .'___
#           ."" '<  `.___\_<|>_/___.' >' "".
#          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#          \  \ `_.   \_ __\ /__ _/   .-` /  /
#      =====`-.____`.___ \_____/___.-`___.-'=====
#                        `=---='
#
# ..................佛祖开光 ,永无BUG...................
# ..................佛祖保佑，永不加班...................
import random, string
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, string
from PIL import Image,ImageDraw,ImageFont,ImageFilter


def getRandomChar(count=4):
    ran = string.ascii_lowercase + string.digits
    chr = ''
    for i in range(count):
        chr += random.choice(ran)
    return chr


def getRandomColor():
    return (random.randint(50, 150), random.randint(50, 150), random.randint(50, 150))


def creatr_code():
    img = Image.new('RGB', (120, 30), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Arvo-Regular.ttf', 25)
    code = getRandomChar()
    for t in range(4):
        draw.text((30*t+5, 0), code[t], getRandomColor(),font)
    for _ in range(random.randint(0, 50)):
        draw.point((random.randint(0, 120),
            random.randint(0, 30)), fill=getRandomColor())
    # 使图片验证码变模糊
    # img = img.filter(ImageFilter.BLUR)
    return img, code
