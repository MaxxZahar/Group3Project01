from django.contrib import admin
from ..models import TechnologiesBlockModel, TechnologyModel


@admin.register(TechnologiesBlockModel)
class TechnologiesBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(TechnologyModel)
class TechnologyAdmin(admin.ModelAdmin):
    pass
