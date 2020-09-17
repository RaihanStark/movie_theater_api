from django.db import models
from .string import DESCRIPTION_PLACEHOLDER, THEATER_THUMBNAIL_URL_DEFAULT, MOVIE_THUMBNAIL_URL_DEFAULT, SHOWTIME_DATA_DEFAULT
import json
# Create your models here.
        
class Movie(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(default=DESCRIPTION_PLACEHOLDER)
    image_url = models.CharField(
        max_length=255,
        default=MOVIE_THUMBNAIL_URL_DEFAULT)
    
    def __str__(self):
        return self.name

class Theater(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image_url = models.CharField(
        max_length=100, 
        default=THEATER_THUMBNAIL_URL_DEFAULT)
    showtime = models.ManyToManyField(
        'Showtime',
        blank=True,
        related_name='showtime')
        
    def __str__(self):
        return self.name

class Showtime(models.Model):
    theater = models.ForeignKey(
        Theater, 
        related_name='theater', 
        on_delete=models.CASCADE)

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_times = models.TextField(default=SHOWTIME_DATA_DEFAULT)

    def get_showtime(self):
        return json.loads(self.start_times)
    
    def set_showtime(self, times_list):
        showtime = {
            "times":times_list
        }

        self.start_times = json.dumps(showtime)
        return True

    def __str__(self):
        return "{}'s Showtime in {}".format(self.movie,self.theater)