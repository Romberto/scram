# Generated by Django 4.0.5 on 2022-07-06 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_productmodel_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='article',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
