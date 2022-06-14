from django.contrib import admin
from ..models import DescriptionBlockModel
from ..models import Problem
from ..models import ProblemPart


@admin.register(DescriptionBlockModel)
class DescriptionBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    pass


@admin.register(ProblemPart)
class ProblemPartAdmin(admin.ModelAdmin):
    pass
