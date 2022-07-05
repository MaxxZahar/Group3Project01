from django.db import models
from .form import FormModel


class ServiceModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Услуга')
    form = models.ForeignKey(FormModel, on_delete=models.CASCADE, related_name='form_service', verbose_name='Форма')
    order = models.IntegerField(verbose_name='Порядок отображения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['order']
