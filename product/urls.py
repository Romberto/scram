from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListProductView.as_view(), name='product'),
    path('<int:id_el>', views.ProductGroupView.as_view(), name='group'),
    path('article/<int:article>', views.ProductItemView.as_view(), name='product_item')
]
