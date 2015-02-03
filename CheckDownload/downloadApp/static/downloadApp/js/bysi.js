$(function(){
	var page = 1;
	var is_end = false;
	var is_ready = true;
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
		function callback(data){
			loaded();
			id_end = data.is_end;
			$('.content').prepend(data.funny_page);
			$("img.data-img").scrollLoading();
		}
		if(!is_end&&is_ready){
			page++;
			$.ajax({
		      url:'/downloadApp/bysi/?page=' + page,
			  dataType:"json",
			  success:callback
			});
			is_ready=false;
			loading();
		}else{
			$('.warning').show();
			var t=setTimeout("$('.warning').hide()",1000);
		}
	});
	$("img.data-img").scrollLoading();
});