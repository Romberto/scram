document.addEventListener("DOMContentLoaded", () => {
    var selector = $('#id_phone')
    var im = new Inputmask("+7(999)-999-99-99");
    im.mask(selector);

    new JustValidate(".new__contact_form", {
    rules: {
        phone: {
            required: true,
            function: (name, value) => {

            var phon = document.getElementById('id_phone')
            phone = phon.inputmask.unmaskedvalue()
                return Number(phone) && phone.length === 10
            }
        },


    }
    });

});