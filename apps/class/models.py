from django.db import models
from apps.users.models import CustomUser
from apps.common.models import BaseModel

class Group(BaseModel):
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"
