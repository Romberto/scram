from django.shortcuts import render
from django.views import View
from contacts.models import ClientModel
from contacts.forms import ClientForm


class SearchContAllView(View):
    """ Все контакты """

    def get(self, request):
        clients = ClientModel.objects.all().order_by('-id')
        client_form = ClientForm()

        return render(request, './contacts/contacts.html', {'clients': clients,
                                                            'client_form': client_form})


class SearchOrg(View):
    """ поиск по оранизациям"""

    def get(self, request):
        search = request.GET.get('search')
        query = ClientModel.objects.filter(name__icontains=search)
        return render(request, './contacts/contacts.html', {'clients': query,
                                                            'client_form': ClientForm()})


class SearchTel(View):
    """ поиск по номеру телефона"""

    def get(self, request):
        search = request.GET.get('search')
        clean_search = ''
        for el in search:
            if el == '+' or el.isdigit():
                clean_search += el
        phone1 = ClientModel.objects.filter(phone=clean_search)
        phone2 = ClientModel.objects.filter(phone2=clean_search)
        phone3 = ClientModel.objects.filter(phone3=clean_search)
        if phone1:
            query = phone1
            return render(request, './contacts/contacts.html', {'clients': query,
                                                                'client_form': ClientForm()})
        elif phone2:
            query = phone2
            return render(request, './contacts/contacts.html', {'clients': query,
                                                                'client_form': ClientForm()})
        elif phone3:
            query = phone3
            return render(request, './contacts/contacts.html', {'clients': query,
                                                                'client_form': ClientForm()})
        else:
            message = 'клиент с таким номером не найден'
            return render(request, './contacts/contacts.html', {'message': message,
                                                                'client_form': ClientForm()})
class SearchFace(View):
    """поиск по контактному лицу """

    def get(self, request):
        search = request.GET.get('search')
        query = ClientModel.objects.filter(contact_face__icontains=search)
        if query:
            return render(request, './contacts/contacts.html', {'clients': query,
                                                                'client_form': ClientForm()})
        else:
            message = 'клиент с таким именем не найден'
            return render(request, './contacts/contacts.html', {'message': message,
                                                                'client_form': ClientForm()})
