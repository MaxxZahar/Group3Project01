from django.db import models


class TeamBlockModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок команды'
        verbose_name_plural = 'Блок команды'


class TeamItemModel(models.Model):
    item = models.CharField(max_length=255, verbose_name='Элемент команды')
    block = models.ForeignKey(TeamBlockModel, on_delete=models.CASCADE, related_name='block_team_member',
                              verbose_name='Блок')

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = 'Элемент команды'
        verbose_name_plural = 'Элементы команды'
