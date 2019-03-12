from django.shortcuts import render,redirect,reverse
from django.views.decorators.http import require_POST

from shopcart.models import ShopCart
from goods.models import Goods
from users.models import Address
from . import models


# @require_POST
def confirm(request):
    """
    把对应商品添加到订单上，确认订单信息
    :param request:
    :return:
    """
    # 收货地址
    # count = request.POST.getlist("count")
    # 获取购物车中数据的id，把对应商品添加到订单中
    g_ids = request.POST.getlist("s_id")
    shopCarts = ShopCart.objects.filter(pk__in=g_ids)
    address = Address.objects.filter(user=request.user)
    shopcarts1 = ShopCart.objects.filter(user=request.user)
    print(shopcarts1)
    # 计算总价
    i = 0
    for zj in shopcarts1:
        i += zj.allTotal
        print(i)

    return render(request,'orders/confirm.html',{"shopCarts":shopCarts,"address":address,"i":i})


def pay(request):       # 支付，待完善
    pass


def done(request):
    """
    将订单中的商品存储到数据库中，然后根据订单中的商品计算总额
    :param request:
    :return:
    """

    # 从界面获取购物车商品ID
    c_ids = request.POST.getlist("c_id")
    # 从界面获取选择的地址ID
    address_id = request.POST["address"]
    # 获取地址对象
    address = Address.objects.get(pk=address_id)
    # 编辑存入订单里的地址
    _address = address.province + " " + address.city + " " + address.area + "  " + address.desc
    # 生成订单
    order = models.Orders(recv_address=_address,user=request.user,recv_name=address.recv_name,recv_tel=address.recv_tel,all_price=0,remark='')
    order.save()

    allCount = 0
    # 获取购物车里的商品对象
    shopcars = ShopCart.objects.filter(pk__in=c_ids)
    # 遍历购物车里的商品，将订单提交到数据库
    for s in shopcars:
        g = s.goods
        orderItem = models.orders_item(goods_id=g.id,goods_img=g.goodsimages_set.all().first().path,goods_name=g.name,goods_price=g.price,goods_count=s.count,goods_price_all=s.allTotal,order=order)
        orderItem.save()
        allCount += s.allTotal
    # 小计
    order.all_price = allCount
    order.save()

    return redirect(reverse("orders:list"))


# 查看订单
def list(request):
    """
    查询所有的订单信息
    :param request:
    :return:
    """
    # 查询订单所属的用户
    orders = models.Orders.objects.filter(user=request.user)
    # 查询商品属于那个订单
    orderitem = models.orders_item.objects.filter(order=orders)

    return render(request,"orders/list1.html",{"orders":orders,"orderItem":orderitem})


# 商品详情
def detail(request, o_id):
    """
    查看单个订单的所有商品
    :param request:
    :param o_id:
    :return:
    """
    orderItem = models.orders_item.objects.filter(order_id=o_id)

    return render(request,"orders/detail.html",{"orderItem": orderItem})


def delete_order(request, o_id):
    """
    删除订单，从数据库中删除
    :param request:
    :param o_id:
    :return:
    """
    order = models.Orders.objects.get(pk=o_id)
    order.delete()

    return redirect(reverse("orders:list"))



