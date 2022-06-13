from django.db import models


class TopBlockModel(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    top_right_text = models.CharField(max_length=255, verbose_name='Текст в верхнем правом углу')
    text = models.TextField(verbose_name='Текст')
    img = models.FileField(verbose_name='Главное изображение')
    img_alt = models.CharField(max_length=255, verbose_name='Описание изображения')
    logo = models.FileField(verbose_name='Логотип')
    logo_alt = models.CharField(max_length=255, verbose_name='Описание логотипа')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Верхний блок'
        verbose_name_plural = 'Верхние блоки'
