# Generated by Django 4.2.4 on 2023-11-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0003_alter_savingoptions_fin_prdt_cd_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewDeposits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.IntegerField()),
                ('kor_co_nm', models.CharField(max_length=200)),
                ('fin_prdt_nm', models.CharField(max_length=200)),
                ('intr_rate_6', models.FloatField(blank=True, null=True)),
                ('intr_rate_12', models.FloatField(blank=True, null=True)),
                ('intr_rate_24', models.FloatField(blank=True, null=True)),
                ('intr_rate_36', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
