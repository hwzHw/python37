from django.shortcuts import render, redirect, reverse

# Create your views here.
#会话判断登录
from django.contrib.auth.decorators import login_required
from . import models
#只允许GET请求进入视图函数
from django.views.decorators.http import require_GET




@login_required
def add(req):
    if req.method == 'GET':
        return render(req, 'store/add.html', {})
    else:
        name = req.POST['name']
        intro = req.POST['intro']
        try:
            cover = req.FILES['cover']
            store = models.Store(name=name, intro=intro, cover=cover, user=req.user)
        except:
            store = models.Store(name=name, intro=intro)

    store.save()
    return redirect(reverse('store:detail', args=(store.id,)))


@require_GET
@login_required
def list(req):
    stores = models.Store.objects.filter(user=req.user, status__in=[0, 1])
    return render(req, 'store/list.html', {'stores': stores, })


@login_required
def detail(req, sid):
    store = models.Store.objects.get(pk=sid)
    return render(req, 'store/detail.html', {'store': store,})


@login_required
def update(req, sid):
    if req.method == 'GET':
        store = models.Store.objects.get(pk=sid)
        return render(req, 'store/update.html', {'store': store})

    else:
        name = req.POST['name']
        intro = req.POST['intro']
        store = models.Store.objects.get(pk=sid)
        try:
            cover = req.FILES['cover']
            store.cover =cover
        except:
            pass
    store.name = name
    store.intro = intro
    store.save()
    return redirect(reverse('store:detail', args=(store.id,)))



@require_GET
def change(req, sid, cid):
    store = models.Store.objects.get(pk=sid)
    store.status = int(cid)
    store.save()
    return render(req, 'store/detail.html', {'store': store, })
