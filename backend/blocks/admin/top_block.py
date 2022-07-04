from django.contrib import admin
from ..models import TopBlockModel


@admin.register(TopBlockModel)
class TopBlockAdmin(admin.ModelAdmin):
    pass
