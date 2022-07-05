from garpix_page.models import BasePage


class CasePage(BasePage):
    template = "pages/case.html"

    def get_context(self, request=None, *args, **kwargs):
        from blocks.models import TopBlockModel
        from home.models import HeaderModel
        from blocks.models import DescriptionBlockModel
        from blocks.models import ImplementationBlockModel
        from blocks.models import TeamBlockModel
        from blocks.models import TechnologiesBlockModel
        from home.models import FooterModel
        from blocks.models import ColorModel
        from blocks.serializers import TopBlockSerializer, DescriptionBlockSerializer, \
            ImplementationBlockSerializer, TeamBlockSerializer, TechnologiesBlockSerializer, \
            ColorSerializer
        from home.serializers import HeaderSerializer, FooterSerializer
        context = super().get_context(request, *args, **kwargs)
        top_block = TopBlockSerializer(TopBlockModel.objects.filter(case=self.id).first()).data
        header = HeaderSerializer(HeaderModel.objects.first()).data
        description_blocks = DescriptionBlockSerializer(DescriptionBlockModel.objects.filter(case=self.id),
                                                        many=True).data
        implementation_block = ImplementationBlockSerializer(ImplementationBlockModel.objects.filter(case=self.id)
                                                             .first()).data
        team_block = TeamBlockSerializer(TeamBlockModel.objects.filter(case=self.id).first()).data
        technologies_block = TechnologiesBlockSerializer(TechnologiesBlockModel.objects.filter(case=self.id).first())\
            .data
        footer = FooterSerializer(FooterModel.objects.first()).data
        color = ColorSerializer(ColorModel.objects.filter(case=self.id).first()).data
        context.update({
            'header': header,
            'top_block': top_block,
            'description_blocks': description_blocks,
            'implementation_block': implementation_block,
            'team_block': team_block,
            'technologies_block': technologies_block,
            'footer': footer,
            'color': color,
        })
        return context

    class Meta:
        verbose_name = "Кейс"
        verbose_name_plural = "Кейсы"
        ordering = ("-created_at",)
