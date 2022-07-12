from django.db import models
from contacts.models import ClientModel
from product.models import ProductModel


class TraidModel(models.Model):
    contact = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "сделка"
        verbose_name_plural = "сделки"
