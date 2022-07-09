from django import forms
from .models import ClientModel


class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientModel
        fields = ['name', 'phone', 'phone2', 'phone3','mail', 'ur_adress',
                  'fac_adress', 'contact_face', 'comment']


    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "название юр лица"
        self.fields['name'].widget.attrs['class'] = 'add__form_input'
        self.fields['phone'].label = "телефон"
        self.fields['phone'].widget.attrs['class'] = 'add__form_input'
        self.fields['phone2'].label = "телефон №2"
        self.fields['phone2'].widget.attrs['class'] = 'add__form_input'
        self.fields['phone3'].label = "телефон №3"
        self.fields['phone3'].widget.attrs['class'] = 'add__form_input'
        self.fields['mail'].label = "почта"
        self.fields['mail'].widget.attrs['class'] = 'add__form_input'
        self.fields['ur_adress'].label = "юр адрес"
        self.fields['ur_adress'].widget.attrs['class'] = 'add__form_input'
        self.fields['fac_adress'].label = "факт адрес"
        self.fields['fac_adress'].widget.attrs['class'] = 'add__form_input'
        self.fields['contact_face'].label = "контактное лицо"
        self.fields['contact_face'].widget.attrs['class'] = 'add__form_input'
        self.fields['comment'].label = "комментарий"
        self.fields['comment'].widget.attrs['class'] = 'add__form_input'


    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get("phone")
        phone2 = cleaned_data.get('phone2')
        phone3 = cleaned_data.get('phone3')
        if len(phone) != 17:
            msg = "не корректный номер телефона"
            self.add_error('phone', msg)
        if phone2:
            if len(phone2) != 17:
                msg = "не корректный номер телефона"
                self.add_error('phone', msg)
        if phone3:
            if len(phone3) != 17:
                msg = "не корректный номер телефона"
                self.add_error('phone', msg)

