$(function(){
	$('#textzh').on('focusin',function(){
		$('.textzh').css({'border':'1px solid #6cb8df'});
		$('.textzh').css({'background':'url(../images/dlyhm1.jpg) no-repeat 0 0'})
		$('.textzh>i').css({'background':'url(../images/qx.jpg) no-repeat 0 9px'})
		$('.textzh>i').on('click',function(){
			$('.textzh').css({'border':'1px solid #6cb8df'});
			$('.textzh>i').css({'background':'url(../images/qx.jpg) no-repeat 0 9px'})
			$('#textzh').val('')
		})
	})
	$('#textzh').on('focusout',function(){
		$('.textzh').css({'border':'1px solid #ccc'});
		$('.textzh').css({'background':'url(../images/dlyhm.jpg) no-repeat 0 0'});
		$('.textzh>i').css({'background':'url(../images/qx2.jpg) no-repeat 0 9px'});
	})
	$('#passwordma').on('focusin',function(){
		$('.passwordma').css({'border':'1px solid #6cb8df'});
		$('.passwordma').css({'background':'url(../images/pass1.jpg) no-repeat 0 0'});
		$('.passwordma>i').css({'background':'url(../images/qx.jpg) no-repeat 0 9px'});
		$('.passwordma>i').on('click',function(){
			$('.passwordma').css({'border':'1px solid #6cb8df'});
			$('.passwordma>i').css({'background':'url(../images/qx.jpg) no-repeat 0 9px'})
			$('#passwordma').val('')
		})
	})
	$('#passwordma').on('focusout',function(){
		$('.passwordma').css({'border':'1px solid #ccc'});
		$('.passwordma').css({'background':'url(../images/pass.jpg) no-repeat 0 0'})
		$('.passwordma>i').css({'background':'url(../images/qx2.jpg) no-repeat 0 9px'})
	})
	var Btn=true;	
	$('.dlewmimg').on('click',function(){		
		if(Btn==true){
			$('.dlewmimg>img').attr({'src':'../images/dlewm2.jpg'});
			$('.contentdl-right').css({'display':'none'})
			$('.pcdl').css({'display':'block'});
			Btn=false;
		}else if(Btn==false){
			//$('.midliftmid').css({'height':'135'});
			$('.dlewmimg>img').attr({'src':'../images/dlewm1.jpg'});
			$('.contentdl-right').css({'display':'block'})
			$('.pcdl').css({'display':'none'});
			Btn=true;
		}
	});
	/*---------------------------------表单验证----------------------------------------*/
	$('#textzh').focusout(function(){
		var $use_val=$('#textzh').val();
		var use_reg=/^1\d{10}$/;
		var email_reg=/^[a-z\d]+(\.[a-z\d]+)*@([\da-z](-[\da-z])?)+(\.{1,2}[a-z]+)+$/;		
		if($use_val.length==0){
			$('.textone').html('用户名不能为空')
			return false;
		}else if(!use_reg.test($use_val)&&!email_reg.test($use_val)){
			$('.textone').html('输入不合法');
			return false;
		}else{
			$('.textone').text('');
		}
	})
	$('#passwordma').focusout(function(){
		var $psw_val=$('#passwordma').val();
		var psw_reg=/^[a-z0-9_-]{6,18}$/;
		if($psw_val.length==0){
			$('.texttwo').html('请输入密码');
			return false;
		}else if(!psw_reg.test($psw_val)){
			$('.texttwo').html('您输入的密码不合法');
			return false;
		}else{
			$('.texttwo').text('');
		}
	})
	/*---------------------------------------------------------------------------------*/
});
