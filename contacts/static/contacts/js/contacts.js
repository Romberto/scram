window.addEventListener('load', function(){

    $('.js_new_client').on('click', function(e){
        e.preventDefault()
        $('.new__contact').fadeIn()
    })


    $('.js_new__contact_close').on('click', function(e){
        e.preventDefault()
        $('.new__contact').fadeOut()
    })

        $(document).mouseup( function(e){ // событие клика по веб-документу
		var div = $(".form_errors" ); // тут указываем ID элемента
		if ( !div.is(e.target) // если клик был не по нашему блоку
		    && div.has(e.target).length === 0 ) { // и не по его дочерним элементам
			div.hide(); // скрываем его

		}
	});
    // убрать сообщение о неудачном сохранение нового контакта
	$('.form_errors_close_btn').on('click', function(e){
	    e.preventDefault()
        $('.form_errors').fadeOut()
	});

	// попар об удаление контакта
	$('.js_del_client').on('click', function(e){
	   e.preventDefault()
	   $('.new__contact_form').css({'filter': 'blur(5px)'})
	   $('.popup_inner').fadeIn()
	});

	$('.js_no').on('click', function(e){
	    $('.new__contact_form').css({'filter': 'none'})
	    $('.popup_inner').fadeOut()
	})








})