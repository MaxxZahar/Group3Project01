# Generated by Django 3.1 on 2022-06-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20220618_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='implementationblockmodel',
            name='text_2',
            field=models.TextField(blank=True, null=True, verbose_name='Текст под вторым подзаголовком'),
        ),
    ]
