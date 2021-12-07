# Generated by Django 3.2.8 on 2021-10-22 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=122)),
                ('Email', models.EmailField(max_length=122, unique=True)),
                ('Number', models.CharField(max_length=12)),
                ('Subject', models.CharField(max_length=122)),
                ('Message', models.CharField(max_length=200)),
                ('Date', models.DateField()),
            ],
        ),
    ]