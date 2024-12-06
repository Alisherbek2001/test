from rest_framework import serializers
from .models import Exam
from apps.question.serializers import SubjectSerializer
from apps.question.models import Subject, Question
from random import shuffle


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

    def create(self, validated_data):
        subjects = validated_data.pop("subjects")
        count_question = validated_data.get("count_question")

        exam = Exam.objects.create(**validated_data)
        exam.subjects.set(subjects)

        questions = Question.objects.filter(subject__in=subjects)
        if count_question:
            questions = questions.order_by("?")[:count_question]

        exam.questions.set(questions)
        return exam

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation["subjects"] = [
            {"id": subject.id, "name": subject.name}
            for subject in instance.subjects.all()
        ]

        representation["questions"] = [
            {
                "id": question.id,
                "name": question.text,
                "answers": self.get_random_answers(question),
            }
            for question in instance.questions.all()
        ]

        return representation

    def get_random_answers(self, question):
        answers = [
            {"id": answer.id, "text": answer.text} for answer in question.answers.all()
        ]
        shuffle(answers)
        return answers
