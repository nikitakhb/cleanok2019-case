"""Advices URL configuration."""

from django.urls import include, path
from rest_framework import routers

from advices import views

router = routers.DefaultRouter()
router.register('', views.ListAdvicesView)

urlpatterns = [
    path('', include(router.urls))
]
