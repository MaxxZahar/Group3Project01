from django.contrib import admin
from ..models import ImplementationBlockModel
from ..models import FunctionalityModel


@admin.register(ImplementationBlockModel)
class ImplementationBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(FunctionalityModel)
class FunctionalityAdmin(admin.ModelAdmin):
    pass
