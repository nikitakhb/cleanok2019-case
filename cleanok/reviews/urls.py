from django.urls import include, path
from rest_framework import routers
from reviews import views

router = routers.DefaultRouter()
router.register('', views.ListReviewsView)

urlpatterns = [
    path('', include(router.urls))
]
