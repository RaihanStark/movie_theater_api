from django.shortcuts import render
from rest_framework import viewsets, filters

from .serializers import MovieSerializer, TheaterSerializer, ShowtimeSerializer
from .models import Movie, Theater, Showtime

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('id')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    serializer_class = MovieSerializer

class TheaterViewSet(viewsets.ModelViewSet):
    queryset = Theater.objects.all().order_by('id')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    serializer_class = TheaterSerializer

class ShowtimeViewSet(viewsets.ModelViewSet):
    queryset = Showtime.objects.all().order_by('id')
    serializer_class = ShowtimeSerializer

    