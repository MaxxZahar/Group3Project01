# Generated by Django 3.1 on 2022-06-28 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20220627_1006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='functionalitycolumnmodel',
            options={'verbose_name': 'Колонка функционала', 'verbose_name_plural': 'Колонки функционала(Блок реализации)'},
        ),
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ['order'], 'verbose_name': 'Проблема', 'verbose_name_plural': 'Проблемы(Блок описания)'},
        ),
    ]
