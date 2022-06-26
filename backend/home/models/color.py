from django.db import models
from app.fields import ColorField


class ColorModel(models.Model):
    default = models.BooleanField(default=True, verbose_name='Оставить настройки по умолчанию')
    color = ColorField(default='#4036ba', verbose_name='Выбрать цвет')
    description_font_color = ColorField(default='#4036ba', verbose_name='Выбрать цвет текста в блоке описания')
    secondary_color = ColorField(default='#24d7ff', verbose_name='Выбрать второй цвет')

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
