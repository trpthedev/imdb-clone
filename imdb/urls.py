from django.urls import path, include
from imdb.views import movie_detail, movie_list

urlpatterns = [
    path('list/', movie_list, name='movie_list'),
    path('list/<int:movie_id>/', movie_detail, name='movie_detail')
]
