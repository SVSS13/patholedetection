from django.urls import path
from .views import analyze_traffic

urlpatterns = [
    path('analyze/', analyze_traffic),
]