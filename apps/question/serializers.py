from rest_framework import serializers
from .models import Answer, Question, SubSubject, Subject, UploadQuestion
from .utily import import_questions_from_excel


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class SubSubjectSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())

    class Meta:
        model = SubSubject
        fields = ["id", "name", "subject", "created_at", "updated_at"]

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res["subject"] = SubjectSerializer(instance.subject, context=self.context).data
        return res


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "text", "is_correct", "created_at", "updated_at"]


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    subject = SubjectSerializer()
    sub_subject = SubSubjectSerializer()

    class Meta:
        model = Question
        fields = [
            "id",
            "text",
            "subject",
            "sub_subject",
            "answers",
            "created_at",
            "updated_at",
        ]


class UploadQuestionSerializer(serializers.ModelSerializer):
    subject = serializers.CharField()

    class Meta:
        model = UploadQuestion
        fields = "__all__"

    def create(self, validated_data):
        request = self.context.get("request")
        if not request or not request.user:
            raise serializers.ValidationError("Request object or user is missing.")
        subject_name = validated_data.pop("subject")

        subject, created = Subject.objects.get_or_create(name=subject_name)

        validated_data["subject"] = subject

        upload_question = super().create(validated_data)

        import_questions_from_excel(
            upload_question.questions.path, subject.id, request.user
        )

        return upload_question
