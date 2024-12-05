from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Question, UploadQuestion
from .serializers import QuestionSerializer, UploadQuestionSerializer


class QuestionListCreateAPIView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class UploadQuestionListCreateAPIView(ListCreateAPIView):
    queryset = UploadQuestion.objects.all()
    serializer_class = UploadQuestionSerializer
