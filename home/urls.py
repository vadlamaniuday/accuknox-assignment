from django.urls import path
from .views import trigger_signal_view

urlpatterns = [
    path("", trigger_signal_view, name="trigger_signal_view"),
]
