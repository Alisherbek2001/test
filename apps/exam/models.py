from django.db import models
from apps.common.models import BaseModel
from apps.question.models import Subject, Question


class Exam(BaseModel):
    name = models.CharField(max_length=255)
    subjects = models.ManyToManyField(Subject)
    count_question = models.PositiveIntegerField(default=0)
    questions = models.ManyToManyField(Question, blank=True)
    score = models.FloatField(default=100.0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Exam"
        verbose_name_plural = "Exams"
