$(document).ready(function() {
	$(".addCart").click(function(event){
		var total = $("#quantity").val();
		console.log(total);
		$.post( "/shop/addToShopingCart/"+total function( data ) {
  			$(".logoCart").empty();
		});	
	});
});