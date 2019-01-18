from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'categories', views.ServiceCategoryViewSet)
router.register(r'', views.ServiceViewSer)
router.register(r'work_items', views.WorkItemViewSer)


urlpatterns = [
    path('', include(router.urls)),
]
