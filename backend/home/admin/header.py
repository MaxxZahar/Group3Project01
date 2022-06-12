from django.contrib import admin
from ..models import HeaderModel


@admin.register(HeaderModel)
class HeaderAdmin(admin.ModelAdmin):
    pass
