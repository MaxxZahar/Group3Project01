from modeltranslation.translator import TranslationOptions, register
from ..models import CaseListPage


@register(CaseListPage)
class CaseListPageTranslationOptions(TranslationOptions):
    pass
