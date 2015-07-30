var refreshCart = setInterval( function() 
    {
		$.get("/shop/refreshShopingCart", function(data){
			$(".itemsCart").html("");
  			$(".itemsCart").append(data);
		});
    }, 5000);
refreshCart;
