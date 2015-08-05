var refreshCart = setInterval( function() 
    {
		$.get("/shop/refreshShopingCart", function(data){
			$(".itemsCart").html("");
  			$(".itemsCart").append(data);
  			$(".itemsCart").attr("title","See your Cart!");
		});
    }, 5000);
refreshCart;
