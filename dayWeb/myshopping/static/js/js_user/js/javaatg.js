$(function(){
	$(window).scroll(function(){
		var $scrollTop=$(window).scrollTop();
		if($scrollTop>470){
			$('.atgleft').addClass('pfixed');
		}else{
			$('.atgleft').removeClass('pfixed');
		}
	})
	$(function(){
		$('.timesdjs').countdown('2016/10/1', function(event) {
			$(this).text(event.strftime('%D 天 %H 时 %M 分 %S 秒'));
		});
	})
	$('.atgright>li').each(function(index){
		$(this).hover(function(){
			$('.atgright>li').css({'border':'2px solid #fff'});
			$('.atgright>li').eq(index).css({'border':'2px solid red'});			
		});
	})
	
})
