from django.contrib import admin
from .models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    list_filter = ["name"]
    list_per_page = 10
    search_fields = ["name"]


admin.site.register(Group, GroupAdmin)
