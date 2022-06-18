from django.contrib import admin
from ..models import TeamBlockModel, TeamItemModel


@admin.register(TeamBlockModel)
class TeamBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(TeamItemModel)
class TeamItemAdmin(admin.ModelAdmin):
    pass
