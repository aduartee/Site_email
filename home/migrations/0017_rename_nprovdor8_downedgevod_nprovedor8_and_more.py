# Generated by Django 4.1.1 on 2023-01-15 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_rename_origin6_downoriginvod_origin8'),
    ]

    operations = [
        migrations.RenameField(
            model_name='downedgevod',
            old_name='nprovdor8',
            new_name='nprovedor8',
        ),
        migrations.AlterField(
            model_name='downoriginvod',
            name='origin8',
            field=models.CharField(default='EMAIL', max_length=30),
        ),
    ]