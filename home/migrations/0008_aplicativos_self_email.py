# Generated by Django 4.1.1 on 2022-11-23 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_aplicativos_alter_vod_origin2'),
    ]

    operations = [
        migrations.AddField(
            model_name='aplicativos',
            name='self_email',
            field=models.CharField(default='EMAIL', max_length=40),
        ),
    ]