from django.contrib import admin
from .models import Test


class TestAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "attempts_count",
        "count_question",
        "is_active",
        "status",
    ]
    list_filter = ["status", "is_active"]
    list_editable = ["attempts_count", "count_question", "status"]
    search_fields = ["name"]
    list_per_page = 10


admin.site.register(Test, TestAdmin)
