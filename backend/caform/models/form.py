from django.db import models


class FormModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=255, verbose_name='Подзаголовок')
    filter_title = models.CharField(max_length=255, verbose_name='Текст на фильтре')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница формы'
        verbose_name_plural = 'Страницы формы'
