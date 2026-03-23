from django.urls import path
from .views import smart_transport_control

urlpatterns = [
    path('control/', smart_transport_control),
]