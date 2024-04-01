from celery import shared_task
from .models import Movie

@shared_task
def update_movie_rankings():
    upcoming_movies = Movie.objects.filter(status='coming_up')
    for movie in upcoming_movies:
        movie.ranking += 10
        movie.save()