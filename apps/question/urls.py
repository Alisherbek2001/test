from django.urls import path
from .views import QuestionListCreateAPIView, UploadQuestionListCreateAPIView

urlpatterns = [
    path("question/", QuestionListCreateAPIView.as_view(), name="question-list"),
    path(
        "upload-question/",
        UploadQuestionListCreateAPIView.as_view(),
        name="upload-question",
    ),
]
