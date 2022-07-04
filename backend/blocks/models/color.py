from django.db import models
from app.fields import ColorField
from cases.models import CasePage


class ColorModel(models.Model):
    default = models.BooleanField(default=True, verbose_name='Оставить настройки по умолчанию')
    color = ColorField(default='#4036ba', verbose_name='Выбрать цвет')
    description_font_color = ColorField(default='#4036ba', verbose_name='Выбрать цвет текста в блоке описания')
    secondary_color = ColorField(default='#24d7ff', verbose_name='Выбрать второй цвет')
    order = models.IntegerField(default=0, verbose_name='Применяется схема с наименьшим номером')
    case = models.ForeignKey(CasePage, on_delete=models.CASCADE, related_name='color_block',
                             verbose_name='Кейс')

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
        ordering = ['order']
