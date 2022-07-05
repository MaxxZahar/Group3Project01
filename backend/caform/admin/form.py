from ..models import FormModel, ServiceModel
from django.contrib import admin


class ServiceInline(admin.TabularInline):
    model = ServiceModel
    fk_name = 'form'


@admin.register(FormModel)
class FormAdmin(admin.ModelAdmin):
    inlines = [
        ServiceInline,
    ]
