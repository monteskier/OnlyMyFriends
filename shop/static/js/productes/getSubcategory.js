$(document).ready(function() {
	
	console.log("hem carregat jquery");
	$('#navlist ul.MenuFather li').click(function(event){
		if (event.stopPropagation) event.stopPropagation(); else event.cancelBubble = true;
		$(".MenuChilds").hide(200);
		$(".MenuChilds").remove();
	    var id = $(this).attr('id');
	    var value = $(this).attr('value');
	     $.get("/shop/categoryChilds/"+value, function(data){
	     	data = JSON.parse(data);
	     	console.log(data);
	     	console.log(id);
	        $("#"+id).append("<ul class='MenuChilds'>");
	        $(".MenuChilds").hide();
	     	$.each(data, function(fId, fVal){
  				$('#'+id+' .MenuChilds').append("<li><a href='/shop/category/"+fVal.pk+"/'>"+fVal.fields.name+"</a></li>");
			});
			$("#"+id+" .MenuChilds").append("</ul>");
			$(".MenuChilds").show(200);
	     });
	        
	});
	
});
