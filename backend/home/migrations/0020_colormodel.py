# Generated by Django 3.1 on 2022-06-20 17:07

import app.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20220620_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', app.fields.ColorField(default='#ffffff', max_length=10)),
            ],
        ),
    ]
