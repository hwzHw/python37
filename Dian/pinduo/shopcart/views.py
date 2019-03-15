from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth import authenticate, login, logout # 引入商品种类表
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from goods.models import Goods
from . import models


@require_GET
@login_required
def add(request):
    """
    把商品添加到购物车功能，
    :param request:
    :return:
    """
    # 添加商品
    count = request.GET['count']
    goods_id = request.GET['goods_id']
    goods = Goods.objects.get(pk=goods_id)
    user = request.user

    try:
        # 将商品添加到订单中
        shopCart = models.ShopCart.objects.get(user=user,goods=goods)
        shopCart.count += int(count)
        shopCart.allTotal = shopCart.count * goods.price
        shopCart.save()
    except:
        # 异常不添加
        shopCart = models.ShopCart(goods=goods,user=user)
        shopCart.count = int(count)
        shopCart.allTotal = shopCart.count * goods.price
        shopCart.save()

    return redirect(reverse("shopcart:listt"),kwargs={})


@login_required
def listt(requst):
    """
    # 购物车
    # 将购物车中数据按事件倒叙排序展示到界面
    :param requst:
    :return:
    """
    shopcarts = models.ShopCart.objects.filter(user=requst.user).order_by("-addTime")
    print(shopcarts)
    # 计算总价
    i = 0
    for a in shopcarts:
        i += a.allTotal
        print(i)

    return render(requst,"shopcart/list.html", {"shopcarts": shopcarts, "i": i})


# 修改商品
def update(request):
    """
    # 获取界面数据,修改商品
    :param request:
    :return:
    """
    # 获取界面数据
    count = request.GET['count']
    goods_id = request.GET['goods_id']
    goods = Goods.objects.get(pk=goods_id)
    user = request.user
    # 修改数据并保存数据库
    shopCart = models.ShopCart.objects.get(user=user, goods=goods)
    count1 = request.POST["count"]
    shopCart.count = int(count1)
    shopCart.allTotal = shopCart.count * goods.price
    shopCart.save()


@require_POST
@csrf_exempt
def zj(request):
    """
    购物车上的商品的标动，添加到数据库中
    # 接收界面变化的数据
    :param request:
    :return:
    """
    zz = request.POST["zj"]
    jj = request.POST["sl"]
    # 将变更的数据修改到数据库中
    s_id = request.POST["s_id"]
    shopcart = models.ShopCart.objects.get(pk=s_id)
    shopcart.count = jj
    shopcart.allTotal = zz
    shopcart.save()

    return HttpResponse("hello")
