/**
 * Created by Administrator on 2016/9/9.
 */
$(function () {
    //=======================右侧小广告===============
    $('#last_gotoback').on('click',function () {
        $(window).scrollTop(0);
    });
    //=====================右侧栏================
    $('.my-car').click(function () {
        $('#shopcar-right').toggle();
    });




})