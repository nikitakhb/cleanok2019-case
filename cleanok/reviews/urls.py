from django.urls import path
from .views import ListReviewsView

urlpatterns = [
    path('', ListReviewsView.as_view(), name="reviews-all")
]
