function update_shoping_list(product_id, total){
		total = $(total).val(),product_id;
		$.get( "/shop/addToShopingCart/"+total+"/"+product_id, function( data ) {
			url="/shop/shopingList/";
			$(location).attr("href", url);			
		});
	};
	