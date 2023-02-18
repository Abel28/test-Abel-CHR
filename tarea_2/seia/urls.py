from django.urls import path
from . import views

app_name = "projects"


urlpatterns = [
    path('api/', views.load_data, name="api"),
    path('json/', views.get_json, name="json"),
    path('', views.ProyectListView.as_view(), name="list"),
]