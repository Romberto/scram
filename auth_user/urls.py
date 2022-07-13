from django.urls import path

from . import views

urlpatterns = [
    path('', views.AuthenticationView.as_view(), name='logIn'),
    path('logout/', views.LogOut.as_view(), name='logOut'),

]