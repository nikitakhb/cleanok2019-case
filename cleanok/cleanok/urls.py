from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from news import views as news_views
from reviews import views as reviews_views
from galery import views as galery_views

router = routers.DefaultRouter()
router.register(r'news', news_views.ListNewsView)
router.register(r'reviews', reviews_views.ListReviewsView)
router.register(r'galery/albums', galery_views.ListAlbumsView)
router.register(r'galery/pictures', galery_views.ListPicturesView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
