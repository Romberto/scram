from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views import View

from auth_user.forms import AuthForm, ProfileForm
from auth_user.views import auth_decoration


class CabinetView(View):
    @auth_decoration
    def get(self, request):
        return render(request, 'cabinet/lk.html')


class ProlileView(View):
    form_user = AuthForm()
    form_profile = ProfileForm()

    def get(self, request, id):
        user_model = User.objects.get(id=id)
        form_user = AuthForm(instance=user_model)
        form_profile = ProfileForm(instance=user_model)

        return render(request, 'cabinet/profile_lk.html', {
            'form_user': form_user,
            'form_profile': form_profile
        })
