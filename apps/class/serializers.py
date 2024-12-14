from .models import Group
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.users.models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "fullname", "username"]


class GroupSerializer(ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), many=True
    )

    class Meta:
        model = Group
        fields = ["id", "name", "students", "created_at", "updated_at"]

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res["students"] = [
            {
                "id": student.id,
                "fullname": student.fullname,
                "username": student.username,
            }
            for student in instance.students.all()
        ]

        return res
