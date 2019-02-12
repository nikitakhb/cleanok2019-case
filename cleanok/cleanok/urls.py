"""Cleanok URL configuration."""

from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('recomends/', include('recomend.urls')),
    path('galery/', include('galery.urls')),
    path('promo/', include('promo.urls')),
    path('services/', include('services.urls')),
    path('certificates/', include('certificates.urls')),
    path('vacancies/', include('vacancies.urls')),
    path('benefits/', include('benefits.urls')),
    path('partnership/', include('partners.urls')),
    path('advices/', include('advices.urls')),
    path('contacts/', include('contacts.urls')),
    path('leads/', include('leads.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
