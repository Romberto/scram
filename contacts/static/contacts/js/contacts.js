window.addEventListener('load', function(){

    $('.js_new_client').on('click', function(e){
        e.preventDefault()
        $('.new__contact').fadeIn()
    })


    $('.js_new__contact_close').on('click', function(e){
        e.preventDefault()
        $('.new__contact').fadeOut()
    })

})