from rest_framework import serializers
from .models import Exam
from apps.question.serializers import SubjectSerializer
from apps.question.models import Subject


class ExamSerializer(serializers.ModelSerializer):
    subjects = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Subject.objects.all()
    )
    start_time = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M", input_formats=["%Y-%m-%d %H:%M"]
    )
    end_time = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M", input_formats=["%Y-%m-%d %H:%M"]
    )

    class Meta:
        model = Exam
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation["subjects"] = [
            {"id": subject.id, "name": subject.name}
            for subject in instance.subjects.all()
        ]

        return representation
