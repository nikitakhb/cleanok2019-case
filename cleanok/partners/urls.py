"""Partners URL configuration."""

from django.urls import include, path
from rest_framework import routers

from partners import views

router = routers.DefaultRouter()
router.register(r'', views.ListPartnerCategoriesView)

urlpatterns = [
    path('', include(router.urls))
]
