from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Question, UploadQuestion, Subject
from .serializers import QuestionSerializer, UploadQuestionSerializer, SubjectSerializer


class QuestionListCreateAPIView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SubjectListCreateAPIView(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class UploadQuestionCreateAPIView(CreateAPIView):
    queryset = UploadQuestion.objects.all()
    serializer_class = UploadQuestionSerializer
