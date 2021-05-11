from django.contrib import admin

from .models import Examination, Scan


class ScanInline(admin.StackedInline):
    model = Scan
    extra = 1
    max_num = 10


class ExaminationAdmin(admin.ModelAdmin):
    inlines = [
        ScanInline,
    ]
    list_display = ("kind", "date", "patient", "healthcare_professional", "priority")
    list_filter = ("priority",)


admin.site.register(Examination, ExaminationAdmin)
