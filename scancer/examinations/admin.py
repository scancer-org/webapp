from django.contrib import admin

from .models import Examination


class ExaminationAdmin(admin.ModelAdmin):
    list_display = ("kind", "date", "patient", "healthcare_professional", "priority")
    list_filter = ("priority",)


admin.site.register(Examination, ExaminationAdmin)
