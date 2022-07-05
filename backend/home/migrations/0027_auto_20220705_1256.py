# Generated by Django 3.1 on 2022-07-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20220628_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='headermodel',
            name='extended_logo',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Логотип для развёрнутого меню'),
        ),
        migrations.AddField(
            model_name='headermodel',
            name='extended_logo_alt',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание логотипа для развёрнутого меню'),
        ),
    ]
