$(document).ready(function() {
	$(".addCart").click(function(event){
		var total = $("#quantity").val();
		console.log(total);
		$.post( "/shop/addToShopingCart/?total="+total+"&product_id="+1, function( data ) {
  			$(".logoCart").empty();
		});	
	});
});