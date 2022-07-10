from django.urls import path

from . import views

urlpatterns = [
    path('', views.SearchContAllView.as_view(), name='searchAll'),
    path('org/', views.SearchOrg.as_view(), name='search_org') ,
    path('tel/', views.SearchTel.as_view(), name='search_tel'),
    path('contactName/', views.SearchFace.as_view(), name='search_face'),
    ]