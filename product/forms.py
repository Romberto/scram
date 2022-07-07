from django import forms
from .models import DocumentProductModel, ProductModel


class DeclarationForm(forms.ModelForm):
    class Meta:
        model = DocumentProductModel
        fields = ['declination']


class ProtocolForm(forms.ModelForm):
    class Meta:
        model = DocumentProductModel
        fields = ['protocol']


class SpecificationForm(forms.ModelForm):
    class Meta:
        model = DocumentProductModel
        fields = ['specification']


class QualityCertificateForm(forms.ModelForm):
    class Meta:
        model = DocumentProductModel
        fields = ['quality_certificate']



#
class AddProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['article', 'product_name']
        widgets = {
            'article': forms.TextInput(attrs={'class': 'input__article',}),
            'product_name': forms.Textarea(attrs={'class': 'input__product_name'}),
        }
