# Generated by Django 4.2.4 on 2023-11-17 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savingproducts',
            name='mtrt_int',
            field=models.TextField(),
        ),
    ]
