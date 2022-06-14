from django.db import models
from garpix_page.models import BasePage


class HomePage(BasePage):
    template = "pages/home.html"

    def get_context(self, request=None, *args, **kwargs):
        from .top_block import TopBlockModel
        from .header import HeaderModel
        from .description_block import DescriptionBlockModel
        from ..serializers import TopBlockSerializer, HeaderSerializer, DescriptionBlockSerializer
        context = super().get_context(request, *args, **kwargs)
        top_block = TopBlockSerializer(TopBlockModel.objects.first()).data
        header = HeaderSerializer(HeaderModel.objects.first()).data
        description_block = DescriptionBlockSerializer(DescriptionBlockModel.objects.first()).data
        context.update({
            'header': header,
            'top_block': top_block,
            'description_block': description_block,
        })
        return context

    class Meta:
        verbose_name = "Main"
        verbose_name_plural = "Main"
        ordering = ("-created_at",)
