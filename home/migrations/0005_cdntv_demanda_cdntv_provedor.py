# Generated by Django 4.1.1 on 2022-11-03 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_cdntv_demandinha_remove_cdntv_provedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdntv',
            name='demanda',
            field=models.CharField(default='VALOR', max_length=5),
        ),
        migrations.AddField(
            model_name='cdntv',
            name='provedor',
            field=models.CharField(default='VALOR', max_length=50),
        ),
    ]
