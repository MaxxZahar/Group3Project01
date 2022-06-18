from django.db import models


class FooterModel(models.Model):
    left_bottom_text = models.CharField(blank=True, null=True, max_length=255, verbose_name='Текст слева внизу')
    right_bottom_text = models.CharField(blank=True, null=True, max_length=255, verbose_name='Текст справа внизу')

    def __str__(self):
        return 'Футер'

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футер'


class ContactsModel(models.Model):
    title = models.CharField(blank=True, null=True, max_length=255, verbose_name='Заголовок')
    phone = models.CharField(blank=True, null=True, max_length=255, verbose_name='Заголовок')
    mail = models.CharField(blank=True, null=True, max_length=255, verbose_name='Заголовок')
    footer = models.ForeignKey(FooterModel, on_delete=models.CASCADE, related_name='footer_contacts',
                               verbose_name='Футер')

    def __str__(self):
        return f'{self.title} {self.phone} {self.mail}'

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class ApplicationModel(models.Model):
    text = models.CharField(blank=True, null=True, max_length=255, verbose_name='Текст')
    link = models.CharField(blank=True, null=True, max_length=255, verbose_name='Ссылка', default='#')
    link_text = models.CharField(blank=True, null=True, max_length=255, verbose_name='Текст на ссылке')
    footer = models.ForeignKey(FooterModel, on_delete=models.CASCADE, related_name='footer_application',
                               verbose_name='Футер')

    def __str__(self):
        return f'{self.text} {self.link_text}'

    class Meta:
        verbose_name = 'Заявление'
        verbose_name_plural = 'Заявления'


class LocationModel(models.Model):
    city = models.CharField(max_length=255, verbose_name='Город')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    footer = models.ForeignKey(FooterModel, on_delete=models.CASCADE, related_name='footer_location',
                               verbose_name='Футер')

    def __str__(self):
        return f'{self.city} {self.address}'

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class LinksModel(models.Model):
    link = models.CharField(max_length=255, verbose_name='Ссылка', default='#')
    name = models.CharField(max_length=255, verbose_name='Название')
    footer = models.ForeignKey(FooterModel, on_delete=models.CASCADE, related_name='footer_links',
                               verbose_name='Футер')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Ссылки'
        verbose_name_plural = 'Ссылки'
