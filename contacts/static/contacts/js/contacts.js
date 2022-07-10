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
    // закрывает попар для удаления
	$('.js_no').on('click', function(e){
	    e.preventDefault()
	    $('.new__contact_form').css({'filter': 'none'})
	    $('.popup_inner').fadeOut()
	})
    // открывает панель поиска контактов
	$('.js_contact_search').on('click', function(e){
	    $('.contact__table').css({'filter': 'blur(5px)'})
	    $('.popup_inner').fadeIn()
	});
    // закрывает панель поиска
    	$('.popup_search_btn').on('click', function(e){
	    $('.contact__table').css({'filter': 'none'})
	    $('.popup_inner').fadeOut()
        $('.link__block').fadeIn()
        $('.search_orgaiz, .search_tel, .search_contact_face').fadeOut()
//        $('.search_tel').fadeOut()
//        $('.search_contact_face').fadeOut()

	});

	// открывает поиск по организациям
	    $('.js_org').on('click', function(e){
	    e.preventDefault()
	    $('.link__block').fadeOut()
	    $('.search_orgaiz').fadeIn()
	    });
    //  открывает поиск по телефону
        $('.js_tel').on('click', function(e){
        e.preventDefault()
        $('.link__block').fadeOut()
        $('.search_tel').fadeIn()

        });

    // открывает поиск по имени контактного лица
        $('.js_face').on('click', function(e){
        e.preventDefault()
        $('.link__block').fadeOut()
        $('.search_contact_face').fadeIn()

        });

})