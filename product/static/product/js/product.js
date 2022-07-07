window.addEventListener('load', function(){

    $('.js_item__doc_link').on('click', function(e){
        e.preventDefault()
        $(this).next().next().fadeIn()
        
    })

    $(document).mouseup( function(e){ // событие клика по веб-документу
		var div = $(".item__doc_vision, .item__form" ); // тут указываем ID элемента
		if ( !div.is(e.target) // если клик был не по нашему блоку
		    && div.has(e.target).length === 0 ) { // и не по его дочерним элементам
			div.hide(); // скрываем его

		}
	});

	$('.js_doc_replacement').on('click', function(e){
		e.preventDefault()
		var elem = $(this.closest('.item_block'))
		elem.find('.item__form').fadeIn()
	})

	$('.js_add_product').on('click', function(e){
	    e.preventDefault()
	    $('.add__form_wrapper').fadeIn()
	})

	$('.add__form_close').on('click', function(e){
	    e.preventDefault()
	    $('.add__form_wrapper').fadeOut()
	})
    

})