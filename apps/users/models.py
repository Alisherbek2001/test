from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.common.models import BaseModel


class CustomUser(AbstractUser, BaseModel):
    fullname = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    role = models.CharField(
        max_length=10,
        choices=(
            ("student", "Student"),
            ("teacher", "Teacher"),
            ("admin", "Admin"),
        ),
        default="student",
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.username
