from django.contrib import admin
from .models import Exam


class ExamAdmin(admin.ModelAdmin):
    list_display = ["name", "start_time", "end_time", "created_at", "updated_at"]
    list_editable = ["start_time", "end_time"]
    search_fields = ["name"]
    list_per_page = 10


admin.site.register(Exam, ExamAdmin)
