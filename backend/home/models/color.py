from django.db import models
from app.fields import ColorField


class ColorModel(models.Model):
    default = models.BooleanField(default=True, verbose_name='Оставить настройки по умолчанию')
    color = ColorField(default='#ffffff', verbose_name='Выбрать цвет')

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
