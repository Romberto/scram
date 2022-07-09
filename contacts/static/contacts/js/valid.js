document.addEventListener("DOMContentLoaded", () => {
    var selector = $('#id_phone')
    var im = new Inputmask("+7(999)-999-99-99");
    im.mask(selector);

    var selector2 = $('#id_phone2')
    var im = new Inputmask("+7(999)-999-99-99");
    im.mask(selector2);

    var selector3 = $('#id_phone3')
    var im = new Inputmask("+7(999)-999-99-99");
    im.mask(selector3);


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
        phone2: {
            required: true,
            function: (name, value) => {

            var phon = document.getElementById('id_phone2')
            phone = phon.inputmask.unmaskedvalue()
                return Number(phone) && phone.length === 10
            }
        },
        phone3: {
            required: true,
            function: (name, value) => {

            var phon = document.getElementById('id_phone3')
            phone = phon.inputmask.unmaskedvalue()
                return Number(phone) && phone.length === 10
            }
        },


    }
    });

});