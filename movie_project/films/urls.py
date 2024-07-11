from django.urls import path
from .views import add_film, films_list

urlpatterns = [
    path('add/', add_film, name='add_film'),
    path('', films_list, name='films_list'),
]
