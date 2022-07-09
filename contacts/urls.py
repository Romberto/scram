from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactsView.as_view(), name='contacts'),
    path('<int:id>', views.ContactItemView.as_view(), name='client'),
    path('delete/<int:id>', views.DeleteContactView.as_view(), name='del_client')
]
