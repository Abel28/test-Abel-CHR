from django.urls import path
from . import views

app_name = "bike"

urlpatterns = [
    path('api/', views.api_bikes, name="bikes_api"),
    path('', views.StationsListView.as_view(), name="list"),
    path('detail/<pk>/', views.StationsDetailView.as_view(), name="detail")
]