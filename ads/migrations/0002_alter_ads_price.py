# Generated by Django 4.2.1 on 2023-06-19 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='price',
            field=models.SmallIntegerField(),
        ),
    ]
