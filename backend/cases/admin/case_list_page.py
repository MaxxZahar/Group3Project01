from ..models.case_list_page import CaseListPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(CaseListPage)
class CaseListPageAdmin(BasePageAdmin):
    pass
