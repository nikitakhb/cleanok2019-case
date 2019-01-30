"""cleanok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('recomends/', include('recomend.urls')),
    path('galery/', include('galery.urls')),
    path('promotions/', include('promotions.urls')),
    path('services/', include('services.urls')),
    path('certificates/', include('certificates.urls')),
    path('vacancies/', include('vacancies.urls')),
    path('benefits/', include('benefits.urls')),
    path('partnership/', include('partners.urls')),
    path('advices/', include('advices.urls')),
    path('contacts/', include('contacts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
