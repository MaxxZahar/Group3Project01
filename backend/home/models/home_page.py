from django.db import models
from garpix_page.models import BasePage


class HomePage(BasePage):
    template = "pages/home.html"

    def get_context(self, request=None, *args, **kwargs):
        from .top_block import TopBlockModel
        from ..serializers import TopBlockSerializer
        context = super().get_context(request, *args, **kwargs)
        top_block = TopBlockSerializer(TopBlockModel.objects.first()).data
        context.update({
            'top_block': top_block
        })
        return context

    class Meta:
        verbose_name = "Main"
        verbose_name_plural = "Main"
        ordering = ("-created_at",)
