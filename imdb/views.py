from django.shortcuts import render
from imdb.models import Movie
from django.http import JsonResponse

def movie_list(request):
    movies = Movie.objects.all()
    return JsonResponse({'movies': list(movies.values())})

def movie_detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        return JsonResponse({'movie': {
            'id': movie.id,
            'name': movie.name,
            'description': movie.description,
            'active': movie.active
        }})
    except Movie.DoesNotExist:
        return JsonResponse({'error': 'Movie not found'}, status=404)
