from django.contrib import admin
from ..models import FooterModel, ContactsModel, ApplicationModel, LocationModel, LinksModel


class ContactsInline(admin.TabularInline):
    model = ContactsModel
    fk_name = 'footer'


class ApplicationInline(admin.TabularInline):
    model = ApplicationModel
    fk_name = 'footer'


class LocationInline(admin.TabularInline):
    model = LocationModel
    fk_name = 'footer'


class LinksInline(admin.TabularInline):
    model = LinksModel
    fk_name = 'footer'


@admin.register(FooterModel)
class FooterAdmin(admin.ModelAdmin):
    inlines = [
        ContactsInline, ApplicationInline, LocationInline, LinksInline,
    ]


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
