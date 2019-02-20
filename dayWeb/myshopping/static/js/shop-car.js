/**
 * Created by Administrator on 2016/9/7.
 */

//    购物车
  /*  $(".Tr02").clone().appendTo(".product-list");

     $(".Tr02").eq(1).find("img").attr({"src":"../img/104a091c-bad7-4c58-994d-3c24c7718765.jpg"});
     $(".Tr02").eq(1).find(".pPrice span").html("399");*/

//    购物车添加多件商品
    $('.shop_car_con').clone().appendTo('shop_table');
//    单击增加数量
    $('.plus_3').each(function (i) {
        $(this).on('click',function () {
            var oValue=$('.txt_3').eq(i).val();
            oValue++;
            $('.txt_3').eq(i).val(oValue);//数量
        //    计算总价
            $(".total_price").eq(i).html(oValue * 19.9);
            $('.goods_amount').html(oValue);//商品件数
        })
    });
//  单击减少数量
    $('.reduce_3').each(function (i) {
        $(this).on('click',function () {
            var oValue=$('.txt_3').eq(i).val();
            if(oValue>0){
                oValue--;
                $('.txt_3').eq(i).val(oValue);//数量
                //    计算总价
                $(".total_price").eq(i).html(oValue * 19.9);
                $('.goods_amount').html(oValue);//商品件数
            }
        })
    })






});