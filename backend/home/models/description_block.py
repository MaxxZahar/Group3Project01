from django.db import models


class DescriptionBlockModel(models.Model):
    title_1 = models.CharField(max_length=255, verbose_name='Заголовок')
    top_text = models.TextField(blank=True, null=True, verbose_name='Верхний текст')
    title_2 = models.CharField(blank=True, null=True, max_length=255, verbose_name='Второй заголовок')
    text = models.TextField(blank=True, null=True, verbose_name='Текст')

    def __str__(self):
        return self.title_1

    class Meta:
        verbose_name = 'Блок описания'
        verbose_name_plural = 'Блоки описания'


class Problem(models.Model):
    number = models.IntegerField(blank=True, null=True, verbose_name='Номер')
    description = models.TextField(verbose_name='Описание')
    block = models.ForeignKey(DescriptionBlockModel, on_delete=models.CASCADE, related_name='description_block_problem', verbose_name='Блок')
    order = models.IntegerField(verbose_name='Порядок отображения', default=0)

    def __str__(self):
        return f'{self.number}. {self.description}'

    class Meta:
        verbose_name = 'Проблема'
        verbose_name_plural = 'Проблемы(Блок описания)'
        ordering = ['order']


class ProblemPart(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='problem_part', verbose_name='Проблема')
    order = models.IntegerField(verbose_name='Порядок отображения', default=0)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Часть проблемы'
        verbose_name_plural = 'Части проблемы'
        ordering = ['order']
