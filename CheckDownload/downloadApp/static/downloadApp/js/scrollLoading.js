(function($){
	$.fn.scrollLoading = function(callbacks,options){
		var defaults = {
			attr:"data-url"
		}
		var params = {}
		params.data = []
		$.extend(params,defaults,options||{});
		$(this).each(function(){
			var o = $(this), tag = this.nodeName.toLowerCase(),url = $(this).attr(params["attr"]);
			var d = {
				obj:o,
				tag:tag,
				url:url
			}
			params.data.push(d);
		});

		var loading = function(){
			valid = false;
			st = $(window).scrollTop(); sth = st + $(window).height();
			$.each(params.data,function(i,data){
				var o = data.obj, tag = data.tag, url = data.url;
				if(o){
					var t = o.position().top, th = t + o.height();
					if((t>st&&t<sth)||(th>st&&th<sth)){
						if(tag === "img"){
							o.attr("src",url);
						}else{
							o.load(url);
						}
						valid = true;
						data.obj = null;
					}
				}

			});
			if(valid&&callbacks){
				callbacks();
				valid = false;
			}
			return false;
		}

		loading();
		$(window).scroll(loading);
	}
})(jQuery);