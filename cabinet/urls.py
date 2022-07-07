from django.urls import path

from . import views

urlpatterns = [
    path('', views.CabinetView.as_view(), name='cabinet')
]
