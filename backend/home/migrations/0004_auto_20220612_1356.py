# Generated by Django 3.1 on 2022-06-12 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_functionalitymodel_headermodel_implementationblockmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headermodel',
            name='logo',
            field=models.FileField(upload_to='', verbose_name='Логотип'),
        ),
    ]
