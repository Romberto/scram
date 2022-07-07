# Generated by Django 4.0.5 on 2022-07-06 13:02

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_documentproductmodel_article_pro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentproductmodel',
            name='protocol',
            field=models.FileField(blank=True, null=True, upload_to=product.models.content_file_name),
        ),
        migrations.AlterField(
            model_name='documentproductmodel',
            name='quality_certificate',
            field=models.FileField(blank=True, null=True, upload_to=product.models.content_file_name),
        ),
        migrations.AlterField(
            model_name='documentproductmodel',
            name='specification',
            field=models.FileField(blank=True, null=True, upload_to=product.models.content_file_name),
        ),
    ]
