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