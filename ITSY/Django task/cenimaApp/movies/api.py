from ninja import NinjaAPI
from movies.models import Movie
from movies.serializers import MovieSerializer
from typing import List

api = NinjaAPI()

@api.post('/movies')
def create_movie(request, movie: MovieSerializer):
    movie_obj = movie.dict()
    movie_instance = Movie.objects.create(**movie_obj)
    return movie_instance

@api.get('/movies')
def list_movies(request) -> List[MovieSerializer]:
    movies = Movie.objects.all()
    return list(movies)
