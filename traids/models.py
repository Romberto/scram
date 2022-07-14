from django.db import models
from contacts.models import ClientModel
from product.models import ProductModel


class TraidModel(models.Model):
    name = models.CharField(max_length=100)
    contact = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)



    class Meta:
        verbose_name = "сделка"
        verbose_name_plural = "сделки"
