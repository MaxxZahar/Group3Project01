from django.db import models


class ImplementationBlockModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    subtitle_1 = models.CharField(blank=True, null=True, max_length=255, verbose_name='Верхний подзаголовок')
    subtitle_2 = models.CharField(blank=True, null=True, max_length=255, verbose_name='Нижний подзаголовок')
    text_1 = models.TextField(blank=True, null=True, verbose_name='Верхний текст')
    text_2 = models.TextField(blank=True, null=True, verbose_name='Текст под вторым подзаголовком')
    bottom_text = models.TextField(blank=True, null=True, verbose_name='Нижний текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок реализации'
        verbose_name_plural = 'Блок реализации'


class FunctionalityColumnModel(models.Model):
    title = models.CharField(blank=True, null=True, max_length=255, verbose_name='Элемент функционала')
    block = models.ForeignKey(ImplementationBlockModel, on_delete=models.CASCADE, related_name='block_column',
                              verbose_name='Блок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Колонка функционала'
        verbose_name_plural = 'Колонки функционала'


class FunctionalityModel(models.Model):
    item = models.CharField(max_length=255, verbose_name='Элемент функционала')
    column = models.ForeignKey(FunctionalityColumnModel, on_delete=models.CASCADE, related_name='column_functionality',
                               verbose_name='Колонка', default=1)
    order = models.IntegerField(verbose_name='Порядок отображения', default=0)

    def __str__(self):
        return f'{self.order}.{self.item}'

    class Meta:
        verbose_name = 'Элемент функционала'
        verbose_name_plural = 'Элементы функционала'
        ordering = ['order']


class BottomSlide(models.Model):
    img = models.ImageField(verbose_name='Изображение')
    img_alt = models.CharField(max_length=255, verbose_name='Описание изображения')
    block = models.ForeignKey(ImplementationBlockModel, on_delete=models.CASCADE, related_name='block_slider_image',
                              verbose_name='Блок')
    order = models.IntegerField(verbose_name='Порядок отображения', default=0)

    def __str__(self):
        return self.img_alt

    class Meta:
        verbose_name = 'Изображение слайдера'
        verbose_name_plural = 'Изображения слайдера'
        ordering = ['order']
