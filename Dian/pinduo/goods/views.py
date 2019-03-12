from django.shortcuts import render,redirect,reverse
from django.views.decorators.http import require_GET
from django.core.serializers import serialize
from django.http import HttpResponse

from . import models
from store.models import Store
from goods.models import Goods,GoodsImages,GoodsType


# 添加商品函数
def add(request):
    """
    添加商品，并将商品品存储到数据库中
    :param request:
    :return:
    """

    # GET请求
    if request.method =="GET":
        # 添加商品页面
        return render(request,"goods/add.html",{})
    else:
        # 获取页面对应的值
        name = request.POST["name"]
        price = request.POST["price"]
        stock = request.POST["stock"]
        store_id = request.POST["store"]
        type2 = request.POST["type2"]
        intro = request.POST["intro"]
        cover = request.FILES["cover"]

        # 验证
        # 获取商店的id
        store = Store.objects.get(pk=store_id)
        # 获取商品
        goodsType = models.GoodsType.objects.get(pk=type2)
        # 保存数据
        goods = models.Goods(name=name,price=price,stock=stock,intro=intro,store=store,goodstype=goodsType)
        goods.save()
        # 保存数据
        goodImage = models.GoodsImages(path=cover,goods=goods)
        goodImage.save()
        # 重定向页面，并返回商铺的ID

        return redirect(reverse("store:detail",kwargs={"s_id":store_id}))


@require_GET
# 获取商品
def findTypeBuId(request):
    """
    周凯博
    获取商品信息
    :param request:
    :return:
    """

    # 获取商品的id  parent_id
    parent_id = request.GET["parent_id"]
    # 根据parent_id获取对应商品
    type2s = models.GoodsType.objects.filter(parent=parent_id)
    # 将获取到商品以json字符串的形式返回到页面

    return HttpResponse(serialize('json',type2s))


@require_GET
# 展示商品
def detail(request,g_id):
    """
    展示商品信息，并将信息返回到界面上
    :param request:
    :param g_id:
    :return:
    """

    # 获取商品信息
    goods = models.Goods.objects.get(pk=g_id)
    # 跳转到页面并返回商品信息

    return render(request,"goods/detail.html",{"goods":goods})


# @require_GET
# 修改商品信息
def update_goods(request, s_id, g_id):
    """
    修改商品信息
    :param request:
    :param s_id:
    :param g_id:
    :return:
    """
    # 根据商店id获取商店
    store = models.Store.objects.get(pk=s_id)
    # 根据g_id获取单个商品对象
    goods_one = Goods.objects.get(id=g_id)
    # 根据g_id获取 商品图片的对象
    goodimage = GoodsImages.objects.get(goods_id=g_id)
    # 获取商品信息
    if request.method == "GET":
        # 获取商品类型一
        type1 = GoodsType.objects.filter(null_id__isnull=True)
        # 根据商店id获取所有商品（获取商店内所有的商品）
        # goods = Goods.objects.filter(goods_store=store)

        return render(request,'Goods/update_goods.html',{"store":store,"type1":type1,"goods_one":goods_one,"g_id":g_id," goodimage": goodimage})
    else:
        # 商品名称
        name = request.POST["name"]
        # 商品单价
        price = request.POST["price"]
        # 商品库存
        stock = request.POST["stock"]
        # # 商品所属商店id
        # store_id = request.POST["store"]
        # 商品介绍
        desc = request.POST["desc"]

        goods_one.name = name
        goods_one.price = price
        goods_one.stock = stock
        goods_one.desc = desc
        goods_one.goods_store = store

        # 存储商品
        # goods_one.save()
        # 存储商品图片
        # goodimage.path = cover
        # goodimage.goods_id = g_id
        # goodimage.save()
        try:
            # 商品图片
            cover = request.FILES["cover"]
            # 商品类型
            type2 = request.POST["type2"]
            # 获取商品类型
            goodstype = models.GoodsType.objects.get(pk=type2)

            goods_one.goods_detail_type = goodstype
            # 存储商品
            goods_one.save()
            # 存储商品图片
            goodimage.path = cover
            goodimage.goods_id = g_id
            goodimage.save()
        except:
            # 存储商品
            goods_one.save()
            # goodimage.goods_id = g_id
            # goodimage.save()

            return redirect(reverse("store:detail",kwargs={"s_id":s_id}))


# 删除商品信息
def delete_goods(request,s_id ,g_id):
    """
    删除商品信息，从数据库中删除
    :param request:
    :param s_id:
    :param g_id:
    :return:
    """
    # 根据g_id获取单个商品
    good_one = Goods.objects.get(id=g_id)
    print(g_id)
    try:
        # 根据g_id获取单个商品的所属图片Goodsimage
        goodimage = GoodsImages.objects.get(goods_id=g_id)
        # 删除单个商品
        good_one.delete()
        # 删除单个商品所属的图片
        goodimage.delete()
    except:
        # 删除单个商品
        good_one.delete()

    return redirect(reverse("store:detail", kwargs={"s_id":s_id}))


