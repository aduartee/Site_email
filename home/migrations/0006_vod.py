# Generated by Django 4.1.1 on 2022-11-06 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_cdntv_demanda_cdntv_provedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='VOD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin2', models.CharField(max_length=50)),
                ('edge2', models.CharField(max_length=45)),
                ('email2', models.CharField(max_length=60)),
                ('demanda2', models.CharField(max_length=5)),
                ('nprovedor', models.CharField(max_length=200)),
            ],
        ),
    ]
