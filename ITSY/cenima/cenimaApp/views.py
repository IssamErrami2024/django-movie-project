from ninja import Api, AsgiWebSocketConsumer
from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer

class MovieListAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.order_by('-ranking')  # Order by ranking (highest first)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MovieCreateAPIView(APIView):
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from .schemas import MovieSchema, MovieListSchema, MovieCreateSchema

class MovieAPI(Api):

    @get('/movies/', response=MovieListSchema)
    def list_movies(self, request):
        movies = Movie.objects.order_by('-ranking')
        return MovieListSchema(results=movies)

    @post('/movies/', response=MovieSchema)
    def create_movie(self, request, data: MovieCreateSchema):
        movie = Movie(**data.data)
        movie.save()
        return MovieSchema.from_orm(movie)