from django.db import models
from garpix_page.models import BasePage


class FormPage(BasePage):
    template = "pages/form.html"

    def get_context(self, request=None, *args, **kwargs):
        from home.models import HeaderModel, FooterModel
        from home.serializers import HeaderSerializer, FooterSerializer
        from .form import FormModel
        from ..serializers import FormSerializer
        context = super().get_context(request, *args, **kwargs)
        header = HeaderSerializer(HeaderModel.objects.first()).data
        footer = FooterSerializer(FooterModel.objects.first()).data
        form = FormSerializer(FormModel.objects.first()).data
        context.update({
            'header': header,
            'footer': footer,
            'form': form,
        })
        return context

    class Meta:
        verbose_name = "Форма"
        verbose_name_plural = "Формы"
        ordering = ("-created_at",)
