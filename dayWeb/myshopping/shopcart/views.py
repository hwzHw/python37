from django.shortcuts import render, redirect, reverse

# Create your views here.

from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from goods.models import Goods
from . import models


@require_GET
@login_required
def add(req, count, goods_id):
    goods = Goods.objects.get(pk=goods_id)
    user = req.user

    try:
        shopCart = models.ShopCart.objects.get(user=user, goods=goods)
        shopCart.count += int(count)
        shopCart.allTotal = shopCart.count * goods.price
        shopCart.save()
    except:
        shopCart = models.ShopCart(goods=goods, user=user)
        shopCart.count = int(count)
        shopCart.allTotal = shopCart.count * goods.price
        shopCart.save()

    return redirect(reverse('shopcart:list'))


#购物车的列表
@login_required
def list(req):
    shopcarts = models.ShopCart.objects.filter(user=req.user).order_by('-addTime')

    return render(req, 'shopcart/list.html', {'shopcarts': shopcarts})


#购物车的删除
def delete(req, shopcart_id):
    shopCart = models.ShopCart.objects.get(pk=shopcart_id)
    shopCart.delete()
    return redirect(reverse('shopcart:list'))























