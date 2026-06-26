from django.urls import path
from .views import HealthAPIView, AnalyzeTicketAPIView

urlpatterns = [
    path("health/", HealthAPIView.as_view(), name="health"),
    path("analyze-ticket/", AnalyzeTicketAPIView.as_view(), name="analyze-ticket"),
]