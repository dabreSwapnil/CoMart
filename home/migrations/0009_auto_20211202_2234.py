# Generated by Django 2.1.5 on 2021-12-02 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20211202_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carts',
            name='amazon_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carts',
            name='dmart_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carts',
            name='flipkart_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carts',
            name='jiomart_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
