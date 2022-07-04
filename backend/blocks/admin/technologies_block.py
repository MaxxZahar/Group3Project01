from django.contrib import admin
from ..models import TechnologiesBlockModel, TechnologyModel


class TechnologyInline(admin.TabularInline):
    model = TechnologyModel
    fk_name = 'block'


# @admin.register(TechnologyModel)
# class TechnologyAdmin(admin.ModelAdmin):
#     pass


@admin.register(TechnologiesBlockModel)
class TechnologiesBlockAdmin(admin.ModelAdmin):
    inlines = [
        TechnologyInline,
    ]
