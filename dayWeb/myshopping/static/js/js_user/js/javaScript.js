$(function(){	
	var Btn=true;	
	$('.bclick').on('click',function(){		
		if(Btn==true){
			$('.midliftmid').css({'height':'198'});
			$('.imga').attr('src','../images/midleftshangla.png');
			Btn=false;
		}else if(Btn==false){
			$('.midliftmid').css({'height':'135'});
			$('.imga').attr('src','../images/midxiala.png');
			Btn=true;
		}
	});
	/*--------------------------菜单吸顶---------------------------------------------*/
	$(window).scroll( function() {
		var $scrolltop=$(window).scrollTop();
		if($scrolltop>840){
			$('.scrollbox').css({'display':'block'});
		}else{
			$('.scrollbox').css({'display':'none'});
		}
	});
	/*-----------------------------------------------------------------------------*/
	var swiper = new Swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        slidesPerView: 1,
        paginationClickable: true,
        spaceBetween: 0,
        loop: true
  });
	/*----------------------------跨域----------------------------------------------*/
	/*var 
		oSearchText   = $(".sotext"),
		oSearchResult = $(".search-result"),
		iSearchIndex  = -1;
	
	oSearchText.on('input propertychange',function(){
		var 
			keyWord 		= oSearchText.val();	
			
		oSearchResult.html('');	
		$.ajax({
			type:"GET",
			url:"https://suggest.taobao.com/sug?code=utf-8&q="+keyWord+"&_ksTS=1468669738868_6223&callback=jsonp6224&area=b2c&code=utf-8&k=1&bucketid=19&src=tmall_pc&isg=Ar29RUOTtlZ0FBI3YsYlccc8zBkhHgJHO932FH8CUJRBtt_oTatpfJAgFl8B&isg2=ApiYJkQEkbNCYMCsIe1DSSl36MgqKPwJ",
			dataType:"jsonp",
			error:function(){
				console.log("error");
			},
			datafilter:function(data){
				return data;
			},
			success:function(data,ts,JQXHR){			
				if(data.result.length > 0){					
					for(var j = 0; j < data.result.length; j++){
						var $li=$('<li data-key = "'+data.result[j][0]+'" class="list"><a href="javascript:;"><b>'+data.result[j][0]+'</b><span>约有'+data.result[j][1]+'个结果</span></a></li>');						
						oSearchResult.append($li);
					}					
					oSearchResult.css({display:"block"});
				}else{
					oSearchResult.css({display:"none"});
					oSearchResult.html('');
				}
			},
		});
	}).focusout(function(){
		oSearchResult.css({'display':"none"});
		oSearchResult.html('');
		oSearchText.val("");
	}).keyup(function (ev) {
		var
			ev = ev || window.event,
			
			aLi = $('.search-result li');
		if(ev.keyCode === 38 || ev.keyCode === 40) {
			if(ev.keyCode === 38 && iSearchIndex > 0) {
				iSearchIndex--;
			} else if(ev.keyCode === 40 && iSearchIndex < aLi.length - 1) {	
				iSearchIndex++;
			}
			oSearchResult.val(aLi.removeClass('active').eq(iSearchIndex).addClass('active').data('key'));
			oSearchText.val(aLi.eq(iSearchIndex).find("b").eq(0).text());
		}
	});*/
	
	/*-----------------------------轮播下面的图片特效--------------------------------------*/
	$('.pinpai-picone>a').each(function(index){
		$(this).hover(function(){
			$('.pinpai-picone a img').eq(index).stop(true).animate({'left':-10},200);
		},function(){
			$('.pinpai-picone a img').eq(index).stop(true).animate({'left':0},200);
		});
	});
	$('.pinpai-pictwo>a').each(function(index){
		$(this).hover(function(){
			$('.pinpai-pictwo a img').eq(index).stop(true).animate({'left':-10},200);
		},function(){
			$('.pinpai-pictwo a img').eq(index).stop(true).animate({'left':0},200);
		});
	});
	/*---------------------------------------------------------------------------------------*/
	$('.co').each(function(index){
		$(this).hover(function(){
			$('.co').removeClass('on');
			$('.co').eq(index).addClass('on');
			$('.dllist').css({'display':'none'});
			$('.dllist').eq(index).css({'display':'block'});			
		});
	});
	$('.Tj>dd').each(function(index){
		$(this).hover(function(){
			if(index==0){
				$('.Tj>dd').eq(index+1).stop(true).animate({'top':52+(index+1)*52},500);
				$('.Tj>dd').eq(index+2).stop(true).animate({'top':52+(index+2)*52},500);
			}else if(index==1){
				$('.Tj>dd').eq(index).stop(true).animate({'top':52},500);
				$('.Tj>dd').eq(index+1).stop(true).animate({'top':52+(index+1)*52},500);
			}
		});
	});
	$('.Rx>dd').each(function(index){
		$(this).hover(function(){
			if(index==0){
				$('.Rx>dd').eq(index+1).stop(true).animate({'top':52+(index+1)*52},500);
				$('.Rx>dd').eq(index+2).stop(true).animate({'top':52+(index+2)*52},500);
			}else if(index==1){
				$('.Rx>dd').eq(index).stop(true).animate({'top':52},500);
				$('.Rx>dd').eq(index+1).stop(true).animate({'top':52+(index+1)*52},500);
			}
		});
	});
	/*-------------------------------------------------------------------------------*/
	$('.smalllist>li').each(function(index){
		$(this).hover(function(){
			$('.smalllist>li').eq(index).addClass('op');
			$('.biglist').stop(true).animate({'left':-index*400},300)
		},function(){
			$('.smalllist>li').eq(index).removeClass('op');
			//$('.biglist>li').eq(index).animate({'left':-((2-index)*400)},300)
		});
	});
	
	
	
	
	/*-----------------倒计时---------------------------------*/
	$(function(){
		$('.clock').countdown('2016/10/1', function(event) {
			$(this).text(event.strftime('%D 天 %H:%M:%S'));
		});
	})
	/*------------------------------banner特效--------------------------------------*/
	$('.leftsport').each(function(index){
		$(this).hover(function(){
			$('.sport').eq(index).stop(true).animate({'left':41},200);
			$('.leftsport').eq(index).css({'border-right':'none'});
			$('.showbox').eq(index).css({'display':'block'});
			$('.sc').on('click',function(){
				$('.showbox').eq(index).css({'display':'none'});
			});
		},function(){
			$('.sport').eq(index).animate({'left':21},200);
			$('.leftsport').css({'border-right':'1px solid #ccc'});
			$('.showbox').eq(index).css({'display':'none'});
		});
	})
	/*-----------------------轮播下面原型小图标--------------------------------*/
	$('.doing-img').each(function(index){
		$(this).hover(function(){;
			$('.doing-img>a').eq(index).stop(true).animate({'top':'-20'},300);
			$('.doing-img>b').eq(index).stop(true).animate({'top':'-20'},200);
		},function(){
			$('.doing-img>a').eq(index).stop(true).animate({'top':'10'},300);
			$('.doing-img>b').eq(index).stop(true).animate({'top':'10'},200);
		})
	});
	/*-----------------------左侧吸顶特效--------------------------------------*/
	$(window).scroll( function() {
		var $scrolltop=$(window).scrollTop();		
		$('.allleft_fly>a').each(function(index){
			$(this).hover(function(){
				$('.allleft_fly a i').eq(index).css({'display':'block'});
			},function(){
				$('.allleft_fly a i').eq(index).css({'display':'none'});
			});
		});
		if($scrolltop>806&&$scrolltop<3430){
			$('.allleft_fly').css({'display':'block'});
		}else{
			$('.allleft_fly').css({'display':'none'});
		}
		if($scrolltop>806&&$scrolltop<1401){
			$('.a1>i').css({'display':'block'})
		}else{
			$('.a1>i').css({'display':'none'})
		} 
		if($scrolltop>1401&&$scrolltop<1955){
			$('.a2>i').css({'display':'block'})
		}else{
			$('.a2>i').css({'display':'none'})
		}
		if($scrolltop>1955&&$scrolltop<2520){
			$('.a3>i').css({'display':'block'})
		}else{
			$('.a3>i').css({'display':'none'})
		}
		if($scrolltop>2520&&$scrolltop<3080){
			$('.a4>i').css({'display':'block'})
		}else{
			$('.a4>i').css({'display':'none'})
		}
		if($scrolltop>3080&&$scrolltop<3430){
			$('.a5>i').css({'display':'block'})
		}else{
			$('.a5>i').css({'display':'none'})
		}
	});
	$('.allleft_fly>a').each(function(index){
			$(this).on('click',function(){
				console.log(index);
				$("html,body").animate({'scrollTop':index * 560 +1060},500);
			});
		});	
		
		$('.right_fhdb').on('click',function(){
			$("html,body").stop(true).animate({'scrollTop':0},500)
		});	
	/*--------------------------右侧特效---------------------------------------*/
	$('.right_news').hover(function(){
		$('.allright_libox').stop(true).animate({'left':'-80'},300);
	},function(){
		$('.allright_libox').stop(true).animate({'left':'34'},300);
	})
	$('.right_hostory').hover(function(){
		$('.hostory').stop(true).animate({'left':'-80'},300);
	},function(){
		$('.hostory').stop(true).animate({'left':'34'},300);
	})
	$('.right_zxkf').hover(function(){
		$('.zxkf').stop(true).animate({'left':'-80'},300);
	},function(){
		$('.zxkf').stop(true).animate({'left':'34'},300);
	})
	$('.right_pxew').hover(function(){
		$('.pxew').css({'display':'block'})
		$('.pxew>img').stop(true).animate({'left':'0'},300);
	},function(){
		$('.pxew>img').stop(true).animate({'left':'175'},300);
	})
	$('.right_fhdb').hover(function(){
		$('.fhdb').stop(true).animate({'left':'-80'},300);
	},function(){
		$('.fhdb').stop(true).animate({'left':'34'},300);
	})
	
	
	$('.allright-top').hover(function(){
		$('.allright-topleft').css({'display':'block'})
		$('.top-left').stop(true).animate({'left':'0'},300);		
	},function(){
		$('.top-left').stop(true).animate({'left':'262'},300);
	});
	$('.top-left').mouseenter(function(){
		$('.allright-topleft').css({'display':'block'})
		$('.top-left').stop(true).animate({'left':'0'},300);
	})
	
	$('.top-left').mouseleave(function(){
		$('.top-left').stop(true).animate({'left':'262'},300);
	})
	
	/*---------------------------精选推荐特效-----------------------------*/
	$('.ppaixe_turn_twoli p').each(function(index){
		$(this).hover(function(){
			var $linebox=$('.linebox');
			$linebox.stop(true).animate({'left':index * 90},300);
			$('.cxlist').css({'display':'none'});
			$('.cxlist').eq(index).css({'display':'block'});
		},function(){
			$('.linebox').eq(index).stop(true).animate({'left':index * 90},300);
			
		})
	});	
	/*-------------------------换一批--------------------------------*/
	/*$('.paixie_turn_doing').on('click',function(){
			var pp=0;
			pp++;
			$('.cxlist').eq(pp).removeClass('cx').css({'display':'block'});
			$('.cxlist').find('.cx').css({'display':'none'})
			$('.cxlist').eq(pp).addClass('cx');			
			if(pp>1){
				pp=0;
			}

		})*/
		
		
	/*-------------------------- F楼层特效   --------------------------------------*/
	$('.F1>a').each(function(index){
		$(this).hover(function(){
			var $lipic=$('.Fpic1');
			$lipic.stop(true).animate({'left':index * 100 + 35},100);
			$('.Fa').css({'display':'none'});
			$('.Fa').eq(index).css({'display':'block'});			
		});
	});
	$('.F2>a').each(function(index){
		$(this).hover(function(){
			var $lipic=$('.Fpic2');
			$lipic.stop(true).animate({'left':index * 100 + 40},100);
			$('.Fb').css({'display':'none'});
			$('.Fb').eq(index).css({'display':'block'});			
		});
	});
	$('.F3>a').each(function(index){
		$(this).hover(function(){
			var $lipic=$('.Fpic3');
			$lipic.stop(true).animate({'left':index * 100 + 40},100);
			$('.Fc').css({'display':'none'});
			$('.Fc').eq(index).css({'display':'block'});			
		});
	});
	$('.F4>a').each(function(index){
		$(this).hover(function(){
			var $lipic=$('.Fpic4');
			$lipic.stop(true).animate({'left':index * 100 + 40},100);
			$('.Fd').css({'display':'none'});
			$('.Fd').eq(index).css({'display':'block'});			
		});
	});
	$('.F5>a').each(function(index){
		$(this).hover(function(){
			var $lipic=$('.Fpic5');
			$lipic.stop(true).animate({'left':index * 100 + 40},100);
			$('.Fe').css({'display':'none'});
			$('.Fe').eq(index).css({'display':'block'});			
		});
	});	
	/*--------------------------------------------------------------------------------*/
	
	$('.dolinkshow').on('click',function(){
		if(Btn==true){
			$('.foot_linkText').css({'height':'80'});
			$('.dolinkshow').css({'background':'url(../images/xiala.jpg) no-repeat'});
			Btn=false;
		}else if(Btn==false){
			$('.foot_linkText').css({'height':'20'});
			$('.dolinkshow').css({'background':'url(../images/zuola.jpg) no-repeat'});
			Btn=true;
		}
	});
});
	
