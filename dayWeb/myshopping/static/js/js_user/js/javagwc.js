$(function(){
	$('.modify-colorsize').hover(function(){
		$('.modify-colorsize').css({'border':'1px dashed #666'});
		$('.modify-colorsize>i').css({'display':'block'});
	},function(){
		$('.modify-colorsize').css({'border':'1px solid #fffcf1'});
		$('.modify-colorsize>i').css({'display':'none'})
	})
	$('.pricetj').hover(function(){
		$('.pricetjtwo').stop(true).slideDown(500);
	},function(){
		$('.pricetjtwo').stop(true).slideUp(500);
	});
	$('.pricetjtwo').hover(function(){
		$('.pricetjtwo').stop(true).slideDown(500);
	},function(){
		$('.pricetjtwo').stop(true).slideUp(500);
	})
	/*-------------------------------增减数量----------------------------------------------------*/
		$('#goodnum').text($('.sl1').val());
		$('.zj1').on('click',function(){
			$('.paymoney').css({'background':'#ff5000'})
			var oValue=$('.sl1').val();
			oValue++;
			$('.sl1').val(oValue); //form表单中用val(input框)  若是文本就用text
			$('#goodnum').text($('.sl1').val());
			$('#goodsmoney').text('¥'+$('.sl1').val()*59.00+'.00');
		});
		$('.js1').on('click',function(){			
			var oValue=$('.sl1').val();
			oValue--;
			if(oValue<0){
				oValue=0
			}
			$('.sl1').val(oValue);
			$('#goodnum').text($('.sl1').val());
			$('#goodsmoney').text('¥'+$('.sl1').val()*59.00);
		})	
		$('#goodsmoney').text('¥'+$('.sl1').val()*59.00+'.00');
/*---------------------------------获取购物车-----------------------------------------*/
	$(function () {				
		// 创建购物车
		$(window).on("load", function () {
			loadCart();
		});	
		function loadCart() {
			var carts = new CartHelper().Read();// 读取购物车中的数据
			//$("#goods1").children().remove();
			// 加载到页面上
			/******************* 加载购买商品信息 BEGIN***********************/
			/*$.each(carts.Items, function(index,cartItem) {
				// console.log(index + "---" + cartItem);
				// console.log(value);
				
				updateCartPage(cartItem.Id, cartItem.Name, cartItem.Count, cartItem.Price, cartItem.imgPath);
			});*/
			/******************* 加载购买商品信息 END***********************/
			// 加载购物结算信息
			$('.sl1').val(8)
			
			/*$(".totalCount").text(carts.Count);
			$(".totalPrice").text(carts.Total);*/
		}
		/*function updateCartPage(id, goodsName, count, price, imgPath) {
			var $tdId = $("<td>");// 商品编号列
			var $tdImg = $("<td>");// 商品图片列
			var $tdName = $("<td>");//商品名称列
			var $tdPrice = $("<td>");// 商品单价列
			var $tdCount = $("<td>");// 购买数量列
			var $tdSubtotal = $("<td>");// 小计价格列
			
			var $trItem = $("<tr>");
			// 更新数据
			$tdId.text(id);
			$tdImg.append($("<img>").attr("src", imgPath));
			$tdName.text(goodsName);
			$tdPrice.text(price);
			$tdCount.text(count);
			$tdSubtotal.text(count * price);
			
			$trItem.append($tdId);
			$trItem.append($tdImg);
			$trItem.append($tdName);
			$trItem.append($tdPrice);
			$trItem.append($tdCount);
			$trItem.append($tdSubtotal);		
			$("#goods1").append($trItem);
		}*/
	});
		
		
});
