from django.db import models
from apps.common.models import BaseModel


class Subject(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"


class Question(BaseModel):
    text = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Answear(BaseModel):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(models.ForeignKey, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = "Answear"
        verbose_name_plural = "Answears"
