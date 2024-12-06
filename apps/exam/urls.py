from django.urls import path
from .views import ExamListCreateAPIView, ExamRetrieveAPIView

urlpatterns = [
    path("exam/", ExamListCreateAPIView.as_view(), name="exam-list"),
    path("exam/<int:pk>/", ExamRetrieveAPIView.as_view(), name="exam-retrieve"),
]
