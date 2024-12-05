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


class Answer(BaseModel):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"


class UploadQuestion(BaseModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    questions = models.FileField(upload_to="questions")

    def __str__(self) -> str:
        return self.subject.name

    class Meta:
        verbose_name = "Upload Question"
        verbose_name_plural = "Upload Questions"
