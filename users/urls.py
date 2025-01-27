from django.urls import path
from .views import UserScoresAPIView, UserScoresUpdateAPIView

urlpatterns = [
    path("user/scores/", UserScoresAPIView.as_view(), name="user-scores"),
    path(
        "user/scores/update/",
        UserScoresUpdateAPIView.as_view(),
        name="update-user-score",
    ),
]
