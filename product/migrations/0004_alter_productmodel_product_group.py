# Generated by Django 4.0.5 on 2022-07-06 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_documentproductmodel_protocol_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='product_group',
            field=models.CharField(blank=True, choices=[('MR', 'маргарин'), ('OIL', 'масло'), ('GSN', 'жиры специального назначения'), ('ZMG', 'заменитель молочного жира'), ('OTH', 'прочее')], max_length=5, null=True),
        ),
    ]
