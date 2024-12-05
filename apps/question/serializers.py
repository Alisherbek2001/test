from rest_framework import serializers
from .models import Answer, Question, Subject, UploadQuestion
from .utily import import_questions_from_excel


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "text", "is_correct", "created_at", "updated_at"]


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    subject = SubjectSerializer()

    class Meta:
        model = Question
        fields = ["id", "text", "subject", "answers", "created_at", "updated_at"]


class UploadQuestionSerializer(serializers.ModelSerializer):
    subject = serializers.CharField()  # Subject uchun string nom kiritiladi

    class Meta:
        model = UploadQuestion
        fields = "__all__"

    def create(self, validated_data):
        subject_name = validated_data.pop("subject")

        subject, created = Subject.objects.get_or_create(name=subject_name)

        validated_data["subject"] = subject

        upload_question = super().create(validated_data)

        import_questions_from_excel(upload_question.questions.path, subject.id)

        return upload_question
