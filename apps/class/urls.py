from django.urls import path
from .views import GroupListCreateAPIView, GroupRetrieveAPIView

urlpatterns = [
    path("group/", GroupListCreateAPIView.as_view(), name="group-list"),
    path("group/<int:pk>/", GroupRetrieveAPIView.as_view(), name="group-retrieve"),
]
