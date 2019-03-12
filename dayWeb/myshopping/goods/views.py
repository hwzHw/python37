from django.shortcuts import render, redirect, reverse

# Create your views here.
from goods.models import GoodsType
from store.models import Store
from users.models import UserInfo
from . import models
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#ajax序列化
from django.core.serializers import serialize


#所有商品类型
def index(req):
    allGoodsType = GoodsType.objects.filter(parent__isnull=True)
    return render(req, 'goods/index.html', {'allGoodsType': allGoodsType})


#所有商品列表
def list(req, sid):
    store = Store.objects.get(pk=sid)
    goods = models.Goods.objects.filter(store=store)
    return render(req, 'goods/list.html', {'store': store, 'goods': goods})


def add(req, sid):
    if req.method =='GET':
        type1 = GoodsType.objects.filter(parent__isnull=True)
        store = models.Store.objects.get(pk=sid)
        return render(req, 'goods/add.html', {"store": store, 'type1': type1})
    else:
        name = req.POST['name']
        price = req.POST['price']
        stock = req.POST['stock']
        store_id = req.POST['store']
        type2 = req.POST['type2']
        intro = req.POST['intro']
        cover = req.FILES['cover']

        # 验证  建议前端加后端

        store = Store.objects.get(pk=store_id)
        goodstype = models.GoodsType.objects.get(name=type2)
        print(goodstype)

        goods = models.Goods(name=name, price=price, stock=stock, intro=intro, store=store, goodstype=goodstype)
        goods.save()

        goodsImage = models.GoodsImage(path=cover, goods=goods)
        goodsImage.save()
        return redirect(reverse('goods:list', args=(store.id,)))


def delete(req, sid, gid):
    goods = models.Goods.objects.get(pk=gid)
    goods.delete()
    return redirect(reverse('goods:list', args=(sid,)))


def update(req, gid):
    if req.method =='GET':
        type1 = GoodsType.objects.filter(parent__isnull=True)
        goods = models.Goods.objects.get(pk=gid)
        return render(req, 'goods/update.html', {'goods': goods, 'type1': type1})
    else:
        name = req.POST['name']
        price = req.POST['price']
        stock = req.POST['stock']
        type2 = req.POST['type2']
        intro = req.POST['intro']
        cover = req.FILES['cover']

        # 验证  建议前端加后端

        goods = models.Goods.objects.get(pk=gid)
        goodstype = models.GoodsType.objects.get(name=type2)
        goodsImage = models.GoodsImage.objects.get(goods=goods)

        goods.name = name
        goods.price = price
        goods.stock = stock
        goods.intro = intro
        goods.goodstype = goodstype
        goodsImage.path = cover
        goodsImage.save()
        goods.save()

        return redirect(reverse('goods:list', args=(goods.store.id,)))


#购买时候的商品详情
@login_required()
def detail(req, gid):
    user = UserInfo.objects.get(user=req.user)
    goods = models.Goods.objects.get(pk=gid)

    return render(req, 'goods/detail.html', {'goods': goods, 'users': user})


#ajax获得数据  一级类型和二级类型
@require_GET
def findTypePid(req):
    parent_id = req.GET['parent_id']
    type2s = models.GoodsType.objects.filter(parent=parent_id)
    return HttpResponse(serialize('json', type2s))










