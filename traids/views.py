from django.shortcuts import render

# Create your views here.
from django.views import View


class TraidsView(View):
    """отображает все сделки """

    def get(self, request):
        return render(request, 'traids/traids.html')
