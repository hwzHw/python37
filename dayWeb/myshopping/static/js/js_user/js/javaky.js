
	function $(id){
		return document.getElementById(id);
	}
	var txt=$('sotext');
	var list=$('search_list');
	txt.oninput=txt.onpropertychange=function(){
		if(this.value!==''){
			var oScript=document.createElement('script');
			oScript.src='https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd='+this.value+'&cb=callback';
			document.body.appendChild(oScript);
			document.body.removeChild(oScript);
		}else{
			list.innerHTML='';
		}
	}
	function callback(oData){
		var sHtml='';
		for(var i=0;i<oData.s.length;i++){
			sHtml+='<li>'+oData.s[i]+'</li>';
		}
		list.innerHTML=sHtml;
		console.log(oData)
	}
	
	var txt1=$('sotext1');
	var list1=$('search_list1');
	txt.oninput=txt.onpropertychange=function(){
		if(this.value!==''){
			var oScript=document.createElement('script');
			oScript.src='https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd='+this.value+'&cb=callback';
			document.body.appendChild(oScript);
			document.body.removeChild(oScript);
		}else{
			list.innerHTML='';
		}
	}
	function callback(oData){
		var sHtml='';
		for(var i=0;i<oData.s.length;i++){
			sHtml+='<li>'+oData.s[i]+'</li>';
		}
		list.innerHTML=sHtml;
	}

	/*var
       		btn=$('.sobtn'),
       		text=$('.sotext'),
       		list=$('#search_list');
    text.oninput=text.onpropertychange=function(){
    	if(text.value!==''){
			var $oScript=$('<script>');
			oScript.src = 'https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd='+this.value+'&cb=callback';
			document.body.appendChild($oScript);
			document.body.removeChild($oScript);
    	}else{
			list.innerHTML='';
    	}
    } 
    function $(id) {
		return document.getElementById(id);
	}
    function callback(oData) {
		var sHtml = '';
		for(var i =0; i < oData.s.length; i++) {
			sHtml += '<li>' + oData.s[i]+ '</li>';
		}
			list.innerHTML = sHtml;
	}
*/