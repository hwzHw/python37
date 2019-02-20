$(function(){
	$('.head_menushow').hover(function(){
		$('.body_topleft').css({'display':'block'});
	},function(){
		$('.body_topleft').css({'display':'none'});
	})
	$('.body_topleft').hover(function(){
		$('.body_topleft').css({'display':'block'});
	},function(){
		$('.body_topleft').css({'display':'none'});
	})
	
	/*-----------------------------放大镜--------------------------------------------*/
	$('.listleftmid>a').each(function(index){
		$(this).hover(function(){
			$('.listleftmid>a').removeClass('active')
			$('.listleftmid>a').eq(index).addClass('active')
			$('.listlefttop>img').attr({'src':$(this).children("img").attr("src")});
			$('.listleftsmall>img').attr({'src':$(this).children('img').attr('src')})
		},function(){
			$('.listleftmid>a').removeClass('active')
		});
	})
	$('.listlefttop').hover(function(){
		$('.zoom-area').css({'display':'block'});
		$('.listleftsmall').css({'display':'block'});
	},function(){
		$('.zoom-area').css({'display':'none'});
		$('.listleftsmall').css({'display':'none'});
	});
	var 		
	$area	 = $(".zoom-area"),
	$middle = $(".listlefttop"),
	$middleImg=$('.listlefttop img')
	$bigImg = $(".listleftsmall img"),
	$big    = $(".listleftsmall");	
	rata = $bigImg.width()/$middleImg.width();    //大图与小图的比例
	//移动
	$middle.mousemove(function(e){
	   	var 
	   		xmax=$(".listlefttop").width()-$(".zoom-area").width(),
	 		ymax=$(".listlefttop").height()-$(".zoom-area").height();
	   		l = e.pageX-$(this).offset().left-$(".zoom-area").width()/2;
	   		t = e.pageY-$(this).offset().top-$(".zoom-area").height()/2;
		if(l<0){
			l=0;
		}else if(l>xmax){
			l=xmax;
		}
		if(t<0){
			t=0;
		}else if(t>ymax)
		{
			t=ymax;
		}
		$(".zoom-area").css({
			left:l,
			top:t
		});
		$bigImg.css({
			top:-parseInt($(".zoom-area").css('top'))*rata+'px',
			left:-parseInt($(".zoom-area").css('left'))*rata+'px'
		});
	});
/*-----------------------------------------------------------------------------*/
	$('.loaddz>i').on('click',function(){
		$('.dzlist').css({'display':'block'})
	});
	$('.dzlist').hover(function(){
		$('.dzlist').css({'display':'block'})
	},function(){
		$('.dzlist').css({'display':'none'})
	});
	$('.dzlist li a').each(function(index){     //遍历dzlist li a
		$(this).on('click',function(){
			$('.dzlist').css({'display':'none'})
			$('.loaddz>p').text($(this).html()); //把loadzd里的内容替换成dzlist li a的内容
		})
	})
	/*-----------------------------------------------------------------------*/
	var bBtn=true;
	$('.goodscolor>i').on('click',function(){
		if(bBtn==true){
			$('.goodscolor i img').attr({'src':'../images/tupianbj.jpg'});
			$('.goodscolor i img').css({'border':0});
			bBtn=false;
		}else if(bBtn==false){
			$('.goodscolor i img').attr({'src':'../images/tupian.jpg'});
			$('.goodscolor i img').css({'border':'2px solid #ccc'});
			bBtn=true;
		}
	})
	$('.num p').each(function(index){
		
		$('.num p').eq(index).click(function(){
			$('.num p').css({'background':'url(../images/cimatp2.jpg) no-repeat 0 0'})
			$('.num p').eq(index).css({'background':'url(../images/cimatp.jpg) no-repeat 0 0'});
			$('#cmnum').text($('.num').eq(index).val())//把鞋码输入到购物车页
		})
	})
	/*----------------------------增减数量----------------------------------------------*/
	$('.zj').each(function(i){  //点击之后每次的数都不一致  所以先遍历
		$(this).on('click',function(){
			var oValue=$('.sl').eq(i).text();
			oValue++;
			$('.sl').eq(i).text(oValue); 
		})
	});
	$('.js').each(function(i){
		$(this).on('click',function(){
			
			var oValue=$('.sl').eq(i).text();
			oValue--;
			if(oValue<0){
				oValue=0
			}
			$('.sl').eq(i).text(oValue);			
		})
	});
	/*-----------------------------------------------------------------------------*/
	$('.goodsgm>p').hover(function(){
		$('.zifufs').css({'display':'block'});
	},function(){
		$('.zifufs').css({'display':'none'});
	})
	$('.zifufs').hover(function(){
		$('.zifufs').css({'display':'block'});
	},function(){
		$('.zifufs').css({'display':'none'});
	})
	/*--------------------------------------------*/
	$('.tabbar>span').each(function(index){
		$(this).on('click',function(){
			$(window).scrollTop(774)
			console.log(index)
			$('.tabbar>span').css({'border-botttom':'1px solid red','color':'#000','bottom-top':'1px solid #ccc','margin-top':5})
			$('.tabbar>span').removeClass('current');
			$('.tabbar>span').eq(index).addClass('current');
			$('.tabbar>span').eq(index).css({'border-botttom':'none','color':'red','margin-top':0,'width':137,})			
		});
	});
	$('.tabbar p img').hover(function(){
		$('.mobfone').css({'display':'block'});
	},function(){
		$('.mobfone').css({'display':'none'});
	});
	
	/*--------------------------------------------------------------------------*/
	/*$(window).on('scroll',function(){
		var $scrolltop=$(window).scrollTop();
		console.log($scrolltop)
		if($scrolltop>954){	
			$('.subleft').addClass('subleftfixed');
		}else{
			$('.subleft').removeClass('subleftfixed');
		}
	})*/
	
	$(window).scroll(function(){
		var $scrolltop=$(window).scrollTop();
		if($scrolltop>954){	
			$('.subleft').addClass('subleftfixed');
		}else{
			$('.subleft').removeClass('subleftfixed');
		}
	});
	/*---------------------------购物车---------------------------------------------*/
	$(".gwc").on("click", function() {
		// 获取商品id
		var id = $('.listright h2').text();
		// 获取图片路径
		var imgPath = $('.goodscolor i').children("img").attr("src");
		// 获取名称
		var goodsName ='';
		// 获取单价
		var price = $('.texttwo span').text();
		// 获取购买数量
		var count = $('.sl').text();
		//获取购买鞋码
		var gdsize=$('.num p').text();
		// 写购物车到cookie中
		new CartHelper().Add(id, goodsName, count, price, imgPath);
		
		// 加载购物车中的数据
		loadCart();
	});

});
