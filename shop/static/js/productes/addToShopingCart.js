$(document).ready(function() {
	$(".addCart").click(function(event){
		var total = $("#quantity").val();
		var product_id = $("#product_id").val();
		console.log(total);
		$.get( "/shop/addToShopingCart/"+total+"/"+product_id, function( data ) {
  			$(".itemsCart").empty();
  			$(".itemsCart").append(data);
		});	
	});
});