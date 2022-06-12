from django.db import models


class ImplementationBlockModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    top_subtitle = models.CharField(max_length=255, verbose_name='Верхний подзаголовок')
    bottom_subtitle = models.CharField(max_length=255, verbose_name='Нижний подзаголовок')
    top_text = models.TextField(verbose_name='Верхний текст')
    bottom_text = models.TextField(verbose_name='Нижний текст')
    top_img = models.ImageField(verbose_name='Верхнее изображение')
    top_img_alt = models.CharField(max_length=255, verbose_name='Описание верхнего изображения')
    bottom_left_img = models.ImageField(verbose_name='Левое нижнее изображение')
    bottom_left_img_alt = models.CharField(max_length=255, verbose_name='Описание левого нижнего изображения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок реализации'
        verbose_name_plural = 'Блок реализации'


class FunctionalityModel(models.Model):
    item = models.CharField(max_length=255, verbose_name='Элемент функционала')
    block = models.ForeignKey(ImplementationBlockModel, on_delete=models.CASCADE, related_name='block_functionality', verbose_name='Блок')

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = 'Элемент функционала'
        verbose_name_plural = 'Элементы функционала'