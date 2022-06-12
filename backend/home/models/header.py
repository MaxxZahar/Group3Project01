from django.db import models


class HeaderModel(models.Model):
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    phone_url = models.CharField(max_length=30, verbose_name='Телефон ссылка')
    logo = models.FileField(verbose_name='Логотип')
    logo_alt = models.CharField(max_length=255, verbose_name='Описание логотипа')

    def __str__(self):
        return 'Телефон и логотип для верхушки сайта'

    class Meta:
        verbose_name = 'Верхушка сайта'
        verbose_name_plural = 'Верхушка сайта'
