$(document).ready(function() {
	console.log("hem carregat jquery");
     $('#navlist ul li').click(function(){
	    var id = $(this).attr('id');
	     $.get("/shop/categoryChilds/"+id, function(data){
	        $("#"+id).append("<ul>");
	     	/*data.each(function(index){
  				$("#"+id ul).append("<li>"+this+"</li>");
			});
			$("#"+id).append("</ul>");
	    
	     /*$('#likes').hide();*/
	     });
	        
	});
});
