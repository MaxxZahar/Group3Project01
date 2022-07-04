from django.contrib import admin
from ..models import DescriptionBlockModel
from ..models import Problem
from ..models import ProblemPart


class ProblemPartInline(admin.TabularInline):
    model = ProblemPart
    fk_name = 'problem'


class ProblemInline(admin.TabularInline):
    model = Problem
    fk_name = 'block'


@admin.register(DescriptionBlockModel)
class DescriptionBlockAdmin(admin.ModelAdmin):
    inlines = [
        ProblemInline,
    ]


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    inlines = [
        ProblemPartInline,
    ]


# @admin.register(ProblemPart)
# class ProblemPartAdmin(admin.ModelAdmin):
#     pass
