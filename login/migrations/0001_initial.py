# Generated by Django 4.1.1 on 2022-11-14 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastrar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario2', models.CharField(max_length=50)),
                ('email2', models.CharField(max_length=50)),
                ('senha2', models.CharField(max_length=50)),
                ('confirmasenha', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
    ]
