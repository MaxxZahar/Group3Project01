from ..models.form_page import FormPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(FormPage)
class FormPageAdmin(BasePageAdmin):
    pass
