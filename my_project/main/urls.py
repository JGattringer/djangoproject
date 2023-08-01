from django.urls import path
from .views import MovieListView

app_name = "main"  # Substitua "app_main" por "app_name" para definir o nome da aplicação

urlpatterns = [
    path("", MovieListView, name="homepage"),  # Use a nova view MovieListView
]






