from django.contrib import admin

from .models import  ProductModel, DocumentProductModel, GroupProductModel

admin.site.register(GroupProductModel)
admin.site.register(ProductModel)
admin.site.register(DocumentProductModel)
