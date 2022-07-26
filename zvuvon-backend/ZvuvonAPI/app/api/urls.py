from django.urls import path

from . import views

urlpatterns = [
    path('calculation/motion', views.calculate_motion)
]