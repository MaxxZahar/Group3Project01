# Generated by Django 3.1 on 2022-06-13 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220612_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topblockmodel',
            name='top_left_text',
        ),
        migrations.AlterField(
            model_name='topblockmodel',
            name='img',
            field=models.FileField(upload_to='', verbose_name='Главное изображение'),
        ),
        migrations.AlterField(
            model_name='topblockmodel',
            name='logo',
            field=models.FileField(upload_to='', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='topblockmodel',
            name='title',
            field=models.TextField(verbose_name='Заголовок'),
        ),
    ]
