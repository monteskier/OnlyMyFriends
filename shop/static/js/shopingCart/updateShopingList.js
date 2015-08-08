function update_shoping_list(product_id, total, size, color,id){
		total = $(id).val();
		$.get( "/shop/addToShopingCart/"+total+"/"+product_id+"/"+color+"/"+size, function( data ) {
			url="/shop/shopingList/";
			$(location).attr("href", url);			
		});
	};
	