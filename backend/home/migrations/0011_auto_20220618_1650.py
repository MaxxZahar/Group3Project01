# Generated by Django 3.1 on 2022-06-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20220618_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='functionalitymodel',
            options={'ordering': ['order'], 'verbose_name': 'Элемент функционала', 'verbose_name_plural': 'Элементы функционала'},
        ),
        migrations.AddField(
            model_name='functionalitymodel',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Порядок отображения'),
        ),
    ]