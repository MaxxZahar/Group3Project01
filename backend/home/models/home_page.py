from django.db import models
from garpix_page.models import BasePage


class HomePage(BasePage):
    template = "pages/home.html"

    def get_context(self, request=None, *args, **kwargs):
        from .top_block import TopBlockModel
        from .header import HeaderModel
        from .description_block import DescriptionBlockModel
        from .implementation_block import ImplementationBlockModel
        from .team_block import TeamBlockModel
        from .technologies_block import TechnologiesBlockModel
        from .footer import FooterModel
        from .color import ColorModel
        from ..serializers import TopBlockSerializer, HeaderSerializer, DescriptionBlockSerializer,\
            ImplementationBlockSerializer, TeamBlockSerializer, TechnologiesBlockSerializer, FooterSerializer, \
            ColorSerializer
        context = super().get_context(request, *args, **kwargs)
        top_block = TopBlockSerializer(TopBlockModel.objects.first()).data
        header = HeaderSerializer(HeaderModel.objects.first()).data
        description_block = DescriptionBlockSerializer(DescriptionBlockModel.objects.first()).data
        implementation_block = ImplementationBlockSerializer(ImplementationBlockModel.objects.first()).data
        team_block = TeamBlockSerializer(TeamBlockModel.objects.first()).data
        technologies_block = TechnologiesBlockSerializer(TechnologiesBlockModel.objects.first()).data
        footer = FooterSerializer(FooterModel.objects.first()).data
        color = ColorSerializer(ColorModel.objects.first()).data
        context.update({
            'header': header,
            'top_block': top_block,
            'description_block': description_block,
            'implementation_block': implementation_block,
            'team_block': team_block,
            'technologies_block': technologies_block,
            'footer': footer,
            'color': color,
        })
        return context

    class Meta:
        verbose_name = "Main"
        verbose_name_plural = "Main"
        ordering = ("-created_at",)
