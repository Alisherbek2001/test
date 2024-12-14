from django.db import models
from apps.common.models import BaseModel
from apps.users.models import CustomUser


class Subject(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"


class SubSubject(BaseModel):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="subsubjects"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "SubSubject"
        verbose_name_plural = "SubSubjects"


class Question(BaseModel):
    text = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    sub_subject = models.ForeignKey(
        SubSubject, on_delete=models.CASCADE, null=True, blank=True
    )
    owner = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True
    )
    language = models.CharField(
        max_length=2, choices=(("uz", "Uz"), ("ru", "Ru")), default="uz"
    )

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
