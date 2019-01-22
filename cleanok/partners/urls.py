from django.urls import include, path
from rest_framework import routers
from partners import views

router = routers.DefaultRouter()
router.register(r'categories', views.ListPartnerCategoriesView)
router.register(r'partners', views.ListPartnersView)

urlpatterns = [
    path('', include(router.urls))
]