from ninja import Query
from .models import Movie
from .serializers import MovieSerializer
from datetime import datetime
from celery import app
from .tasks import update_ranking
from ninja import NinjaAPI


api = NinjaAPI()

# Create Celery task for updating movie rankings
@app.on_startup
def start_celery_worker():
    app.worker_main(['-A', 'cenimaApp', 'worker', '--loglevel=INFO'])

# API endpoint for adding new movies
@api.post("/movies")
def create_movie(request, movie: MovieSerializer):
    movie_obj = movie.dict()
    movie_instance = Movie.objects.create(**movie_obj)
    return movie_instance

# API endpoint for listing movies based on their rankings
@api.get("/movies")
def list_movies(request, ranking: str = Query(None)):
    if ranking == 'higher_first':
        movies = Movie.objects.order_by('-ranking')
    else:
        movies = Movie.objects.all()
    return list(movies)
