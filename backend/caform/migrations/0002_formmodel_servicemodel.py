# Generated by Django 3.1 on 2022-07-05 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Подзаголовок')),
                ('filter_title', models.CharField(max_length=255, verbose_name='Текст на фильтре')),
            ],
            options={
                'verbose_name': 'Страница формы',
                'verbose_name_plural': 'Страницы формы',
            },
        ),
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Услуга')),
                ('order', models.IntegerField(verbose_name='Порядок отображения')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_service', to='caform.formmodel', verbose_name='Форма')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'ordering': ['order'],
            },
        ),
    ]
