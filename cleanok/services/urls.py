"""Services URL configuration."""

from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'uslugi_details', views.ServiceCategory_DetailsViewSet)
router.register(r'uslugi_list', views.ServiceCategory_ListViewSet)
router.register(r'', views.ServiceViewSet)
router.register(r'work_items', views.WorkItemViewSer)


urlpatterns = [
    path('', include(router.urls)),
]
