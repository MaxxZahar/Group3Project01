from django.contrib import admin
from ..models import ImplementationBlockModel, FunctionalityColumnModel, FunctionalityModel, BottomSlide


class FunctionalityInline(admin.TabularInline):
    model = FunctionalityModel
    fk_name = 'column'


class BottomSlideInline(admin.TabularInline):
    model = BottomSlide
    fk_name = 'block'


class FunctionalityColumnInline(admin.TabularInline):
    model = FunctionalityColumnModel
    fk_name = 'block'


@admin.register(ImplementationBlockModel)
class ImplementationBlockAdmin(admin.ModelAdmin):
    inlines = [
        BottomSlideInline, FunctionalityColumnInline,
    ]


@admin.register(FunctionalityColumnModel)
class FunctionalityColumnAdmin(admin.ModelAdmin):
    inlines = [
        FunctionalityInline,
    ]


@admin.register(FunctionalityModel)
class FunctionalityAdmin(admin.ModelAdmin):
    pass


@admin.register(BottomSlide)
class BottomSlideAdmin(admin.ModelAdmin):
    pass
