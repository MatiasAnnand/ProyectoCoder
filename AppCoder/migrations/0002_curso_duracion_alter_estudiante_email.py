# Generated by Django 4.0.4 on 2022-04-26 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='duracion',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
