from django.shortcuts import render

from goods.models import GoodsType,Goods


# 展示首页数据
def index(request):
    """
    在商品节目展示数据类型，将数据返回到界面
    :param request:
    :return:
    """

    # 第一个一级类型数据
    good_type1 = GoodsType.objects.filter(pk=10001)
    # 一级类型所对应的二级类型
    good_type1_2 = GoodsType.objects.filter(parent = good_type1)
    # fffff
    goods1_list = Goods.objects.filter(goodstype__in=good_type1_2)

    # 第二个一级类型数据
    good_type2 = GoodsType.objects.filter(pk=10002)
    # 一级类型所对应的二级类型
    good_type2_2 = GoodsType.objects.filter(parent = good_type2)
    # fffff
    goods2_list = Goods.objects.filter(goodstype__in = good_type2_2)

    # 第三个一级类型数据
    good_type3 = GoodsType.objects.filter(pk=10003)
    # 一级类型所对应的二级类型
    good_type3_2 = GoodsType.objects.filter(parent = good_type3)
    # fffff
    goods3_list = Goods.objects.filter(goodstype__in = good_type3_2)

    # 第四个一级类型数据
    good_type4 = GoodsType.objects.filter(pk=10004)
    # 一级类型所对应的二级类型
    good_type4_2 = GoodsType.objects.filter(parent = good_type4)
    # fffff
    goods4_list = Goods.objects.filter(goodstype__in = good_type4_2)

    # 第五个一级类型数据
    good_type5 = GoodsType.objects.filter(pk=10005)
    # 一级类型所对应的二级类型
    good_type5_2 = GoodsType.objects.filter(parent = good_type5)
    # fffff
    goods5_list = Goods.objects.filter(goodstype__in = good_type5_2)

    allGoodsType = GoodsType.objects.filter(parent__isnull=True)

    return render(request, "index.html", {"allGoodsType": allGoodsType,
                                          "goods1_list": goods1_list,
                                          "goods2_list": goods2_list,
                                          "goods3_list": goods3_list,
                                          "goods4_list": goods4_list,
                                          "goods5_list": goods5_list
                                          })
    # return render(request,'blog/index.html')