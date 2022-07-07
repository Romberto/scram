window.addEventListener('load', function(){
    $('.js_form__contact-close').on('click', function(e){
        $('.form__contact').fadeOut()
    })

    $('.js_form__contact').on('click', function(e){
        e.preventDefault()
        $('.form__contact').fadeIn()
    })

    $('.js_traid_status').on('click', function(e){
        $(this).fadeOut()
        $('.traid__form_status').fadeIn()
    })

    $('.js_traid__close_ntn').on('click', function(e){
        $('.traid__form_info-block').fadeOut()
        $('.traid__info_description_block').fadeIn()
        $('.traid__form_status').fadeOut()
        $('.js_traid_status').fadeIn()
        $('.traid__dop_comment').fadeOut()
    })
    $(document).mouseup( function(e){ // событие клика по веб-документу
		var div = $( ".traid__form_status, .traid__form_info-block, .traid__dop_comment" ); // тут указываем ID элемента
		if ( !div.is(e.target) // если клик был не по нашему блоку
		    && div.has(e.target).length === 0 ) { // и не по его дочерним элементам
			div.hide(); // скрываем его
            $('.js_traid_status').fadeIn()
            $('.traid__info_description_block').fadeIn()
		}
	});

    $('.js_traid_terms').on('click', function(){
        $('.traid__info_description_block').fadeOut()
        $('.traid__form_info-block').fadeIn()
    })

    $('.js_traid_comment_btn').on('click', function(e){
        $('.traid__dop_comment').fadeIn()
    })

})