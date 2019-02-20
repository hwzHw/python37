$(function(){
	//$('#btn').on('submit',function(){
		var $passtwo=$('#passwordtwo').val();
		var $psw_val=$('#password').val();
		$('#password').focusout(function(){
			var $psw_val=$('#password').val();
			var psw_reg=/^[a-z0-9_-]{6,18}$/;
			if($psw_val.length==0){
				$('.pass>b').text('请输入密码');
				return false;
			}else if(!psw_reg.test($psw_val)){
				$('.pass>b').text('您输入的密码不合法');
				return false;
			}else{
				$('.pass>b').text('');
				return true;
			}
		})
		$('#passwordtwo').focusout(function(){
			var oVal=$(this).val();
			if(oVal!==$('#password').val()){
				$('.passtwo>b').text('两次输入密码不一致');
			}else{
				$('.passtwo>b').text('');
			}
			
		})
		$('#usename').focusout(function(){
			var $use_val=$('#usename').val();
			var use_reg=/^1\d{10}$/;
			var email_reg=/^[a-z\d]+(\.[a-z\d]+)*@([\da-z](-[\da-z])?)+(\.{1,2}[a-z]+)+$/;
			if($use_val.length==0){
				$('.usename>b').html('用户名不能为空')
				return false;
			}else if(!use_reg.test($use_val)&&!email_reg.test($use_val)){
				$('.usename>b').html('输入不合法');
				return false;
			}else{
				$('.usename>b').text('');
				return true;
			}
		})
	//})
	
	
});
