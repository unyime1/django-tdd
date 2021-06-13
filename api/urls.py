from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = {
    path('bucketlists/', views.CreateView.as_view(), name="create"),
    path('bucketlists/<int:pk>/', views.DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)