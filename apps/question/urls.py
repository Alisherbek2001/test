from django.urls import path
from .views import (
    QuestionListCreateAPIView,
    UploadQuestionCreateAPIView,
    QuestionRetrieveAPIView,
    SubjectListCreateAPIView,
    SubjectRetrieveAPIView,
    SubSubjectListCreateAPIView,
    SubSubjectRetrieveAPIView,
)

urlpatterns = [
    path("question/", QuestionListCreateAPIView.as_view(), name="question-list"),
    path(
        "question/<int:pk>/",
        QuestionRetrieveAPIView.as_view(),
        name="question-retrieve",
    ),
    path("subject/", SubjectListCreateAPIView.as_view(), name="Subject-list"),
    path(
        "subject/<int:pk>/", SubjectRetrieveAPIView.as_view(), name="Subject-retrieve"
    ),
    path("subsubject/", SubSubjectListCreateAPIView.as_view(), name="SubSubject-list"),
    path(
        "subsubject/<int:pk>/",
        SubSubjectRetrieveAPIView.as_view(),
        name="SubSubject-retrieve",
    ),
    path(
        "upload-question/",
        UploadQuestionCreateAPIView.as_view(),
        name="upload-question",
    ),
]
