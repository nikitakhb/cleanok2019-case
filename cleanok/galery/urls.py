from django.urls import include, path
from rest_framework import routers
from galery import views

router = routers.DefaultRouter()
router.register(r'', views.ListAlbumsView)
router.register(r'pictures', views.ListPicturesView)

urlpatterns = [
    path('', include(router.urls))
]
