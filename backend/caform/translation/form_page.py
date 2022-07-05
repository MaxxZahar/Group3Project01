from modeltranslation.translator import TranslationOptions, register
from ..models import FormPage


@register(FormPage)
class FormPageTranslationOptions(TranslationOptions):
    pass
