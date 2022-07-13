from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from auth_user.models import Profile


class AuthForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            if field == 'username':
                self.fields[field].widget.attrs['placeholder'] = 'login'
            elif field == 'password':
                self.fields[field].widget.attrs['placeholder'] = 'password'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'position')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].label = "телефон"
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['position'].label = 'должность'
        self.fields['position'].widget.attrs['class'] = 'form-control'
