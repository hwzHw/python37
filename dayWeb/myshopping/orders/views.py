from django.shortcuts import render, redirect, reverse

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from shopcart.models import ShopCart
from goods.models import Goods
from users.models import Address
from . import models


@require_POST
def confirm(req):
    s_ids = req.POST.getlist('s_id')
    shopCarts = ShopCart.objects.filter(pk__in=s_ids)
    addresses = Address.objects.filter(user=req.user)

    return render(req, 'orders/confirm.html', {'shopCarts': shopCarts, 'addresses': addresses})


def pay(req):
    #第三方插件 支付宝 微信 往上银行等
    pass


@require_POST
def done(req):
    s_ids = req.POST.getlist('s_id')
    address_id = req.POST['address']
    remark = req.POST['remark']
    shopCares = ShopCart.objects.filter(pk__in=s_ids)
    address = Address.objects.get(pk=address_id)

    #拼接收获地址
    _address = address.province + '|' +\
                address.city + '|' + address.area + '|' + address.street + '|' + address.desc


    # 生成订单
    order = models.Order(recv_address=_address, user=req.user, recv_name=address.recv_name, recv_tel=address.recv_tel,\
                         allPrice=0, remark=remark)
    order.save()

    allCount = 0

    for s in shopCares:
        g = s.goods
        orderItem = models.OrderItem(goods_id=g.id, goods_img=g.goodsimage_set.all().first().path,\
                         goods_name=g.name, goods_price=g.price, goods_count=s.count,\
                         goods_allprice=s.allTotal, order=order)
        orderItem.save()

        allCount += s.allTotal

    order.allPrice = allCount
    order.save()
    return redirect(reverse('orders:list'))


@login_required
def list(req):
    orders = models.Order.objects.filter(user=req.user)

    return render(req, 'orders/list.html', {'orders': orders,})


def delete(req, oid):
    order = models.Order.objects.get(pk=oid)
    order.delete()
    return redirect(reverse('orders:list'))


def detail(req, o_id):
    pass
