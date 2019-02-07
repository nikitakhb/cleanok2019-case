"""News URL configuration."""

from django.urls import include, path
from rest_framework import routers

from news import views

router = routers.DefaultRouter()
router.register('', views.NewsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
