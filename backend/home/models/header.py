from django.db import models


class HeaderModel(models.Model):
    phone = models.CharField(blank=True, null=True, max_length=30, verbose_name='Телефон')
    phone_url = models.CharField(blank=True, null=True, max_length=30, verbose_name='Телефон ссылка')
    logo = models.FileField(verbose_name='Логотип')
    logo_alt = models.CharField(max_length=255, verbose_name='Описание логотипа')
    extended_logo = models.FileField(blank=True, null=True, verbose_name='Логотип для развёрнутого меню')
    extended_logo_alt = models.CharField(blank=True, null=True, max_length=255,
                                         verbose_name='Описание логотипа для развёрнутого меню')

    def __str__(self):
        return 'Телефон и логотип для верхушки сайта'

    class Meta:
        verbose_name = 'Верхушка сайта'
        verbose_name_plural = 'Верхушка сайта'
