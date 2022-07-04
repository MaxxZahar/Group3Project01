from django.contrib import admin
from ..models import ColorModel


@admin.register(ColorModel)
class ColorAdmin(admin.ModelAdmin):
    pass
