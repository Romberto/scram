from django.db import models


class GroupProductModel(models.Model):
    group_title = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.group_title)

    class Meta:
        verbose_name = "группа продукта"
        verbose_name_plural = "группы продуктов"


class ProductModel(models.Model):
    article = models.CharField(max_length=50, unique=True)
    product_name = models.CharField(max_length=200)
    product_group = models.ForeignKey(GroupProductModel, on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return str(self.article)

    class Meta:
        verbose_name = "перечень продукта"
        verbose_name_plural = "перечень продуктов"


def content_file_name(instance, filename):
    return '/'.join(['doc', instance.article_pro.article, filename])


class DocumentProductModel(models.Model):
    article_pro = models.ForeignKey(ProductModel, on_delete=models.CASCADE, blank=True, null=True)
    declination = models.FileField(null=True, blank=True,
                                   upload_to=content_file_name)
    protocol = models.FileField(null=True, blank=True, upload_to=content_file_name)
    specification = models.FileField(null=True, blank=True, upload_to=content_file_name)
    quality_certificate = models.FileField(null=True, blank=True, upload_to=content_file_name)

    class Meta:
        verbose_name = "документ"
        verbose_name_plural = "документы"

    def __str__(self):
        return str(self.article_pro)

    def get_path(self):
        return str(self.article_pro)
