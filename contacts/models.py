from django.db import models


# Create your models here.

class ClientModel(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=20)
    mail = models.EmailField(max_length=150, null=True, blank=True)
    ur_adress = models.CharField(max_length=200, null=True, blank=True)
    fac_adress = models.CharField(max_length=200, null=True, blank=True)
    contact_face = models.CharField(max_length=120)
    comment = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name = "контакт"
        verbose_name_plural = "контакты"

    def __str__(self):
        return str(self.name)

    # def save(self,):
    #     client = ClientModel.objects.get(self.id)
    #     super.client.save( update_fields=['name'])
