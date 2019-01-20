from django.urls import path
from .views import ListNewsView

urlpatterns = [
    path('', ListNewsView.as_view(), name="news-all")
]
