from django.urls import include, path
from .views import ListAlbumsView

urlpatterns = [
    path('', ListAlbumsView.as_view(), name="albums-all")
]
