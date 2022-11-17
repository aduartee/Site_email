# Generated by Django 4.1.1 on 2022-11-14 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_vod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aplicativos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=43)),
                ('stb', models.CharField(max_length=50)),
                ('ios', models.CharField(max_length=50)),
                ('apks', models.CharField(max_length=60)),
                ('email3', models.CharField(max_length=62)),
                ('demanda3', models.CharField(max_length=5)),
                ('nprovedor2', models.CharField(max_length=52)),
            ],
        ),
        migrations.AlterField(
            model_name='vod',
            name='origin2',
            field=models.CharField(max_length=70),
        ),
    ]