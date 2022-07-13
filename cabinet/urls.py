from django.urls import path

from . import views

urlpatterns = [
    path('', views.CabinetView.as_view(), name='cabinet'),
    path('<int:id>', views.ProlileView.as_view(), name='profile_lk')
]
