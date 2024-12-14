from django.db import models
from apps.common.models import BaseModel
from apps.question.models import Subject, Question, SubSubject


class Test(BaseModel):
    name = models.CharField(max_length=255)
    subjects = models.ManyToManyField(Subject)
    subsubjects = models.ManyToManyField(SubSubject)
    attempts_count = models.PositiveIntegerField(default=1)
    count_question = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)
    status = models.CharField(
        max_length=50,
        choices=(
            ("oraliq_nazorat", "Oraliq nazorat"),
            ("joriy_nazorat", "Joriy nazorat"),
            ("imtixon", "Imtixon"),
        ),
        default="joriy_nazorat",
    )
    questions = models.ManyToManyField(Question, blank=True)
    score = models.FloatField(default=100.0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration_test = models.TimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Tests"
