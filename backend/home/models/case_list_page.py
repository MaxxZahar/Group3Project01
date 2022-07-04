from django.db import models
from garpix_page.models import BaseListPage


class CaseListPage(BaseListPage):
    paginate_by = 25
    template = 'pages/case_list.html'

    class Meta:
        verbose_name = "Список кейсов"
        verbose_name_plural = "Список кейсов"
        ordering = ('-created_at',)
