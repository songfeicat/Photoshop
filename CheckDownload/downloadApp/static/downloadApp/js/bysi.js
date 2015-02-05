var page = 1;
var is_end = false;
var is_ready = true;
$(function(){
	$('.nav_l').on('click',function(){
		var loading = function(){
			$('.load').show();
			$('.nav_l').addClass('rotation');
			$('.load img').addClass('rotation');
		}
		var loaded = function(){
			$('.load').hide();
			$('.nav_l').removeClass('rotation');
			$('.load img').removeClass('rotation');
		}
		$.ajax({
			url:'/downloadApp/bysi/?new=1',
		    dataType:"json",
		    success:callback
		});

		function callback(data){
			if(data=='0'){
				$('.warning').show();
				var t=setTimeout("$('.warning').hide()",1000);
			}else{
				function callback(data){
					alert(JSON.parse(data));
					loaded();
					$('.content').prepend(JSON.parse(data));
					$("img.data-img").scrollLoading();
				}
				$.ajax({
					url:'/downloadApp/fetchnew/',
					success:callback
				});
				loading();
			}
		}
	});
	$("img.data-img").scrollLoading();
});
function load_more(){
		function callback(data){
			is_end = data.is_end;
			$('.content').append(data.funny_page);
			$("img.data-img").scrollLoading();
			is_ready=true;
		}
		if(is_end=='False'||!is_end&&is_ready){
			page++;
			$.ajax({
		      url:'/downloadApp/bysi/?new=0&page=' + page,
			  dataType:"json",
			  success:callback
			});
			is_ready=false;
		}else{
			$('.warning').show();
			var t=setTimeout("$('.warning').hide()",1000);
		}
}
window.onscroll=function(){
	var a = document.body.scrollTop;
	var b = document.documentElement.clientHeight;
	var c = document.body.scrollHeight;
	if(a+b>=c){
		load_more();
	}
}