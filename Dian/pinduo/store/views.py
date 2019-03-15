from django.shortcuts import render
from django.shortcuts import redirect, reverse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required


from . import models
from goods.models import GoodsType,Goods


def add(request):
    """
    添加商店，然后存储到数据库中
    :param request:
    :return:
    """
    # GET
    if request.method == "GET":
        #返回到开店界面
        return render(request,"store/add.html")
    # POST
    else:
        # 获取商家信息
        name = request.POST["name"]
        intro = request.POST["intro"]
        # 封面有
        try:
            cover = request.FILES["cover"]
            store = models.Store(name=name, intro=intro, cover=cover, user=request.user)
        except:
            store = models.Store(name=name,intro=intro,user=request.user)
        # 保存
        store.save()
        #
        # print(store.id)
        #返回详情页面
        return redirect(reverse("store:detail",kwargs={"s_id":store.id}))
        # return redirect(reverse("store:list"))


# 只允许GET请求
@require_GET
#登录
@login_required
# 商品列表
def list(request):
    """
    展示商家清单，并将数据返回到界面上
    :param request:
    :return:
    """
    #
    stores = models.Store.objects.filter(user=request.user, status__in=[0, 1])
    #
    return render(request,'store/shang_jia.html',{"stores":stores})


@login_required
#
def update(request,s_id):
    """
    修改商家信息，并将更新好的数据重新存储到数据库中
    :param request:
    :param s_id:
    :return:
    """
    # GET
    if request.method == "GET":
        store = models.Store.objects.get(pk=s_id)
        return render(request,"store/update.html",{'store':store})
    # POST
    else:
        name = request.POST["name"]
        intro = request.POST["intro"]
        store = models.Store.objects.get(pk=s_id)
        store.name = name
        store.intro = intro
        # try
        try:
            cover = request.FILES["cover"]
            store.cover = cover

        except:
            pass
        store.save()
        return redirect(reverse("store:detail",kwargs={"s_id":store.id}))


@require_GET
@login_required
def detail(request,s_id):
    """
    展示商家详情
    :param request:
    :param s_id:
    :return:
    """
    store = models.Store.objects.get(pk=s_id)
    type1 = GoodsType.objects.filter(parent__isnull=True)
    goods = Goods.objects.filter(store=store)
    #
    return render(request,"store/detail.html",{"store":store,"type1":type1,"goods":goods})


#GET请求进入
@require_GET
#允许登录
@login_required
# 修改商店
def change(req,s_id,status):
    """
    修改商店状态
    :param req:
    :param s_id:
    :param status:
    :return:
    """
    # 获取商店对象
    store = models.Store.objects.get(pk=s_id)
    # 商店状态
    store.status = int(status)
    # 保存
    store.save()
    # 判断商店状态
    if store.status == 2:
        #返回商店界面
        return redirect(reverse("store:list"))
    else:
        # 返回商店详情
        # return render(req,"store/detail.html",{"store":store})
        return redirect(reverse("store:detail", kwargs={"s_id": store.id}))


# 登录验证
@login_required
def zhao_shang(request):
    """
    :param request:
    :return:
    """
    # 用户开店界面
    return render(request,"store/zhao_shang.html")


# 商家模块
def shang_jia(request):
    """
    :param request:
    :return:
    """
    # 返回商家
    return render(request,"store/shang_jia.html")