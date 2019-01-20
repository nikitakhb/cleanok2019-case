from django.urls import include, path
from rest_framework import routers
from news import views

router = routers.DefaultRouter()
router.register('', views.ListNewsView)

urlpatterns = [
    path('', include(router.urls))
]
