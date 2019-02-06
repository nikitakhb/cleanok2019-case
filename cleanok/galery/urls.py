"""Galery URL configuration."""

from django.urls import include, path
from galery import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.ListAlbumsView)
router.register(r'pictures', views.ListPicturesView)

urlpatterns = [
    path('', include(router.urls))
]
