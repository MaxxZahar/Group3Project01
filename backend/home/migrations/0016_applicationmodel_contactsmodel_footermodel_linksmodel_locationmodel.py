# Generated by Django 3.1 on 2022-06-18 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_technologiesblockmodel_technologymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_bottom_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст слева внизу')),
                ('right_bottom_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст справа внизу')),
            ],
            options={
                'verbose_name': 'Футер',
                'verbose_name_plural': 'Футер',
            },
        ),
        migrations.CreateModel(
            name='LocationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='footer_location', to='home.footermodel', verbose_name='Футер')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='LinksModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default='#', max_length=255, verbose_name='Ссылка')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='footer_links', to='home.footermodel', verbose_name='Футер')),
            ],
            options={
                'verbose_name': 'Ссылки',
                'verbose_name_plural': 'Ссылки',
            },
        ),
        migrations.CreateModel(
            name='ContactsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('mail', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='footer_contacts', to='home.footermodel', verbose_name='Футер')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='ApplicationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст')),
                ('link', models.CharField(blank=True, default='#', max_length=255, null=True, verbose_name='Ссылка')),
                ('link_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст на ссылке')),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='footer_application', to='home.footermodel', verbose_name='Футер')),
            ],
            options={
                'verbose_name': 'Заявление',
                'verbose_name_plural': 'Заявления',
            },
        ),
    ]
