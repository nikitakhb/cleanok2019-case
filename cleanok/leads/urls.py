from django.urls import include, path
from rest_framework import routers

from leads import views

router = routers.DefaultRouter()
router.register('', views.LeadsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
