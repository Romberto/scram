from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import ClientModel


class ContactsView(View):
    """отоюражает последние пять контактов"""
    def get(self, request):
        clients = ClientModel.objects.all()[0:5]
        return render(request, 'contacts/contacts.html', {'clients':clients})
