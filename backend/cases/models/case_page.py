from django.db import models
from garpix_page.models import BasePage


class CasePage(BasePage):
    template = "pages/case.html"

    def get_context(self, request=None, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        cases = CasePage.objects.all()
        print(self.id)

        return context

    class Meta:
        verbose_name = "Кейс"
        verbose_name_plural = "Кейсы"
        ordering = ("-created_at",)
