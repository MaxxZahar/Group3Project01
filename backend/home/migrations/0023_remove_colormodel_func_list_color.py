# Generated by Django 3.1 on 2022-06-20 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20220621_0212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colormodel',
            name='func_list_color',
        ),
    ]