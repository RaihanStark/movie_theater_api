from django.contrib import admin

from .models import Theater, Movie, Showtime

models = [Theater, Movie, Showtime]
# Register your models here.
admin.site.register(models)