from django.contrib import admin
from ..models import TeamBlockModel, TeamItemModel


class TeamItemInline(admin.TabularInline):
    model = TeamItemModel
    fk_name = 'block'


@admin.register(TeamBlockModel)
class TeamBlockAdmin(admin.ModelAdmin):
    inlines = [
        TeamItemInline,
    ]


@admin.register(TeamItemModel)
class TeamItemAdmin(admin.ModelAdmin):
    pass
