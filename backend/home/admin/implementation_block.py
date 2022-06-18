from django.contrib import admin
from ..models import ImplementationBlockModel, FunctionalityColumnModel, FunctionalityModel, BottomSlide


@admin.register(ImplementationBlockModel)
class ImplementationBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(FunctionalityColumnModel)
class FunctionalityColumnAdmin(admin.ModelAdmin):
    pass


@admin.register(FunctionalityModel)
class FunctionalityAdmin(admin.ModelAdmin):
    pass


@admin.register(BottomSlide)
class BottomSlideAdmin(admin.ModelAdmin):
    pass
