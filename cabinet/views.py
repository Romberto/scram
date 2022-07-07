from django.shortcuts import render

# Create your views here.
from django.views import View


class CabinetView(View):
    def get(self, request):
        return render(request, 'cabinet/lk.html')
