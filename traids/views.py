import datetime

from django.shortcuts import render

# Create your views here.
from django.views import View

from auth_user.views import auth_decoration


class TraidsView(View):
    """отображает все сделки """

    @auth_decoration
    def get(self, request):
        today = datetime.datetime.today()
        return render(request, 'traids/traids.html',
                      {
                          'today': today
                      })
