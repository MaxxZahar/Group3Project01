from django.db import models
from cases.models import CasePage


class TechnologiesBlockModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    subtitle = models.CharField(blank=True, null=True, max_length=255, verbose_name='Подзаголовок')
    text_1 = models.TextField(blank=True, null=True, verbose_name='Верхний текст')
    big_text = models.TextField(blank=True, null=True, verbose_name='Большой текст')
    text_2 = models.TextField(blank=True, null=True, verbose_name='Нижний текст')
    case = models.ForeignKey(CasePage, on_delete=models.CASCADE, related_name='case_technologies_block',
                             verbose_name='Кейс')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок технологий'
        verbose_name_plural = 'Блок технологий'


class TechnologyModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    block = models.ForeignKey(TechnologiesBlockModel, on_delete=models.CASCADE, related_name='block_technology',
                              verbose_name='Блок')
    order = models.IntegerField(verbose_name='Порядок отображения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'
