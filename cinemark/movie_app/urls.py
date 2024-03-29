from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', views.movie_details, name='movie_details'),
    path('movies/add/', views.movie_add, name='movie_add'),
    path('movies/<int:movie_id>/update/', views.movie_update, name='movie_update'),
    path('movies/<int:movie_id>/delete/', views.movie_delete, name='movie_delete'),
]
