from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .models import ClientModel
from .forms import ClientForm


class ContactsView(View):
    """отоюражает последние пять контактов"""

    def get(self, request):
        clients = ClientModel.objects.order_by('-id')[:5]
        client_form = ClientForm()

        return render(request, 'contacts/contacts.html', {'clients': clients,
                                                          'client_form': client_form})

    """ добавление нового клиента"""

    def post(self, request):
        form = ClientForm(request.POST)
        clients = ClientModel.objects.order_by('-id')[:5]
        if form.is_valid():
            phone = ''
            for i in form.cleaned_data['phone']:
                if i == '+' or i.isdigit():
                    phone += i
            phone2 = ''
            if form.cleaned_data['phone2']:
                for i in form.cleaned_data['phone2']:
                    if i == '+' or i.isdigit():
                        phone2 += i
            phone3 = ''
            if form.cleaned_data['phone3']:
                for i in form.cleaned_data['phone3']:
                    if i == '+' or i.isdigit():
                        phone3 += i
            inn = form.cleaned_data['inn']
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            if not mail:
                mail = None
            ur_adress = form.cleaned_data['ur_adress']
            if not ur_adress:
                ur_adress = ''

            fac_adress = form.cleaned_data['fac_adress']
            if not fac_adress:
                fac_adress = ''
            contact_face = form.cleaned_data['contact_face']
            comment = form.cleaned_data['comment']
            new_client = ClientModel(
                name=name,
                phone=phone,
                phone2=phone2,
                phone3=phone3,
                mail=mail,
                inn=inn,
                ur_adress=ur_adress,
                fac_adress=fac_adress,
                contact_face=contact_face,
                comment=comment
            )
            new_client.save()

            return render(request, 'contacts/contacts.html', {'clients': clients,
                                                              'client_form': ClientForm})

        else:
            return render(request, 'contacts/contacts.html', {'clients': clients,
                                                              'client_form': form,
                                                              })


class ContactItemView(View):
    """отображает отдельный контакт с целью изменения данных"""

    def get(self, request, id):
        client = ClientModel.objects.get(id=id)
        form = ClientForm(instance=client)
        data = {
            'client': client,
            'form': form
        }
        return render(request, 'contacts/client.html', data)

    """меняет данные клиента"""

    def post(self, request, id):
        clients = ClientModel.objects.order_by('-id')[:5]
        client = ClientModel.objects.get(id=id)
        form = ClientForm(request.POST)
        if form.is_valid():
            # телефон
            phone = ''
            for i in form.cleaned_data['phone']:
                if i == '+' or i.isdigit():
                    phone += i
            client.phone = phone
            # телефон2
            phone2 = ''
            if form.cleaned_data['phone2']:
                for i in form.cleaned_data['phone2']:
                    if i == '+' or i.isdigit():
                        phone2 += i
            client.phone2 = phone2
            # телефон3
            phone3 = ''
            if form.cleaned_data['phone3']:
                for i in form.cleaned_data['phone3']:
                    if i == '+' or i.isdigit():
                        phone3 += i
            client.phone3 = phone3
            # инн
            client.inn = form.cleaned_data['inn']
            # наименование
            client.name = form.cleaned_data['name']
            # почта


            mail = form.cleaned_data['mail']
            # юридический адрес
            ur_adress = form.cleaned_data['ur_adress']
            if not ur_adress:
                client.ur_adress = ''
            else:
                client.ur_adress = ur_adress
            # фактический адрес
            fac_adress = form.cleaned_data['fac_adress']
            if not fac_adress:
                client.fac_adress = ''
            else:
                client.fac_adress = fac_adress
            # контактное лицо
            client.contact_face = form.cleaned_data['contact_face']
            # комментарий
            client.comment = form.cleaned_data['comment']
            client.save()
            return render(request, 'contacts/contacts.html', {'clients': clients,
                                                              'client_form': ClientForm})
        return render(request, 'contacts/client.html', {'client': client,
                                                        'form': form})
class DeleteContactView(View):
    '''Удаляет контакт клиента'''
    def get(self,request, id):
        delete_client = ClientModel.objects.get(id=id)
        delete_client.delete()
        return redirect(to='/contacts')


