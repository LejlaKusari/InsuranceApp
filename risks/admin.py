from django.contrib import admin
from .models import RiskType, RiskField


class RiskFieldInline(admin.StackedInline):
    model = RiskField
    extra = 5


class RiskTypeAdmin(admin.ModelAdmin):
    inlines = [RiskFieldInline]


admin.site.register(RiskType, RiskTypeAdmin)
