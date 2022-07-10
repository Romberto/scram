from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ProductModel, DocumentProductModel, GroupProductModel
from django.views import View
from .forms import *
import os


class ListProductView(View):
    """отображает все группы товаров"""

    def get(self, request):
        list_product = GroupProductModel.objects.all()
        return render(request, 'product/documents.html', {'list_product': list_product})


class ProductGroupView(View):
    """ отображает продукты определённой группы"""

    def get(self, request, id_el):
        gruop = GroupProductModel.objects.get(id=id_el)
        query = ProductModel.objects.filter(product_group=gruop)
        add_form = AddProductForm()
        return render(request, 'product/group.html', {'group': gruop, 'query': query, 'add_form': add_form})

    def post(self, request, id_el):
        gruop = GroupProductModel.objects.get(id=id_el)
        query = ProductModel.objects.filter(product_group=gruop)
        add_form = AddProductForm()

        if 'add_form_btn' in request.POST:
            form = AddProductForm(request.POST)
            if form.is_valid():
                article = form.cleaned_data['article']
                product_name = form.cleaned_data['product_name']
                new_product = ProductModel(
                    article=article,
                    product_name=product_name,
                    product_group=gruop
                )
                new_product.save()

        return render(request, 'product/group.html', {'group': gruop, 'query': query, 'add_form': add_form})


class ProductItemView(View):
    """отображает перечень документов конкретного товара """

    def get(self, request, article):
        itemProduct = ProductModel.objects.get(article=article)
        try:
            documents = DocumentProductModel.objects.get(article_pro=itemProduct.id)
        except DocumentProductModel.DoesNotExist:
            documents = None
        dec_form = DeclarationForm()
        pro_form = ProtocolForm()
        spe_form = SpecificationForm()
        qua_form = QualityCertificateForm()
        return render(request, 'product/product_item.html', {'item': itemProduct,
                                                             'document': documents,
                                                             'dec_form': dec_form,
                                                             'pro_form': pro_form,
                                                             'spe_form': spe_form,
                                                             'qua_form': qua_form
                                                             })

    def post(self, request, article):
        itemProduct = ProductModel.objects.get(article=article)
        try:
            documents = DocumentProductModel.objects.get(article_pro=itemProduct.id)
        except DocumentProductModel.DoesNotExist:
            documents = DocumentProductModel(article_pro=itemProduct)
            documents.save()
        dec_form = DeclarationForm()
        pro_form = ProtocolForm()
        spe_form = SpecificationForm()
        qua_form = QualityCertificateForm()
        data = {'item': itemProduct,
                'document': documents,
                'dec_form': dec_form,
                'pro_form': pro_form,
                'spe_form': spe_form,
                'qua_form': qua_form
                }

        if 'declination' in request.POST and 'declination' in request.FILES:
            form = DeclarationForm(request.POST, request.FILES)
            if form.is_valid():
                if documents.declination:
                    path_file = f'product/media/{documents.declination}'
                    if os.path.exists(path_file):
                        os.remove(path_file)
                documents.declination = form.cleaned_data['declination']
                documents.save()
        elif 'protocol' in request.POST:
            form = ProtocolForm(request.POST, request.FILES)
            if form.is_valid():
                if documents.protocol:
                    file_path = f'product/media/{documents.protocol}'
                    print(file_path)
                    if os.path.exists(f'{file_path}'):
                        print('*********** ok ***********')
                        os.remove(f'{file_path}')
                documents.protocol = form.cleaned_data['protocol']
                documents.save()
        elif 'specification' in request.POST:
            form = SpecificationForm(request.POST, request.FILES)
            if form.is_valid():
                if documents.specification:
                    file_path = f'product/media/{documents.specification}'
                    if os.path.exists(file_path):
                        os.remove(file_path)
                documents.specification = form.cleaned_data['specification']
                documents.save()
        elif 'quality_certificate' in request.POST:
            form = QualityCertificateForm(request.POST, request.FILES)
            if form.is_valid():
                if documents.quality_certificate:
                    file_path = f'product/media/{documents.quality_certificate}'
                    if os.path.exists(file_path):
                        os.remove(file_path)
                documents.quality_certificate = form.cleaned_data['quality_certificate']
                documents.save()

        return render(request, 'product/product_item.html', data)
