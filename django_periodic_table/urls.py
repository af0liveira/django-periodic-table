"""django_periodic_table URL Configuration"""
from django.urls import path
from .views import IndexView

urlpatterns = [
    path(r'', IndexView.as_view(), name="periodic_table"),
]
