from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Question, UploadQuestion, Subject
from .serializers import QuestionSerializer, UploadQuestionSerializer, SubjectSerializer
from apps.common.permissions import IsTeacher, IsAdmin
from rest_framework.permissions import IsAuthenticated


class QuestionListCreateAPIView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsTeacher | IsAdmin]


class QuestionRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsTeacher, IsAdmin]


class SubjectListCreateAPIView(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class UploadQuestionCreateAPIView(CreateAPIView):
    queryset = UploadQuestion.objects.all()
    serializer_class = UploadQuestionSerializer
    permission_classes = [
        IsTeacher,
    ]
