from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Exam
from .serializers import ExamSerializer


class ExamListCreateAPIView(ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
