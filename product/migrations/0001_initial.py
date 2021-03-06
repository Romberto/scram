# Generated by Django 4.0.5 on 2022-07-06 12:57

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_pro', models.CharField(blank=True, max_length=50, null=True)),
                ('declination', models.FileField(blank=True, null=True, upload_to=product.models.content_file_name)),
                ('protocol', models.FileField(blank=True, null=True, upload_to='doc/')),
                ('specification', models.FileField(blank=True, null=True, upload_to='doc/')),
                ('quality_certificate', models.FileField(blank=True, null=True, upload_to='doc/')),
            ],
            options={
                'verbose_name': 'документы',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=200)),
                ('product_group', models.CharField(blank=True, choices=[('MR', 'маргарин'), ('OIL', 'масло')], max_length=5, null=True)),
            ],
            options={
                'verbose_name': 'перечень продуктов',
            },
        ),
    ]
