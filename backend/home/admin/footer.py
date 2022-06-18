from django.contrib import admin
from ..models import FooterModel, ContactsModel, ApplicationModel, LocationModel, LinksModel


@admin.register(FooterModel)
class FooterAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactsModel)
class ContactsAdmin(admin.ModelAdmin):
    pass


@admin.register(ApplicationModel)
class ApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(LocationModel)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(LinksModel)
class LinksAdmin(admin.ModelAdmin):
    pass
