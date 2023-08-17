from django.urls import path
from .views import PollView

urlpatterns = [
    path("poll/", PollView.as_view(), name="poll-list-create"),
    path('poll/<str:pk>/', PollView.as_view(), name='poll-put-delete'), 
]