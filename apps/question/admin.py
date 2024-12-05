from django.contrib import admin
from .models import Question, Answer, Subject, UploadQuestion


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["text", "subject", "created_at", "updated_at"]
    search_fields = ["text"]
    list_editable = ["subject"]
    list_per_page = 10


admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ["text", "question", "is_correct", "created_at", "updated_at"]
    search_fields = ["text"]
    list_editable = ["is_correct"]
    list_per_page = 10


admin.site.register(Answer, AnswerAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    list_per_page = 10


admin.site.register(Subject, SubjectAdmin)
admin.site.register(UploadQuestion)
