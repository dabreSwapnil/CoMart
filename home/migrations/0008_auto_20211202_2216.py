# Generated by Django 2.1.5 on 2021-12-02 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_carts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carts',
            name='price',
        ),
        migrations.AddField(
            model_name='carts',
            name='amazon_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carts',
            name='dmart_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carts',
            name='flipkart_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carts',
            name='jiomart_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
