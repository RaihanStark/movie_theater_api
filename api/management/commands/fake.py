from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate Fake Data'

    def handle(self, *args, **kwargs):
        theaters = [
            "METROPOLE XXI",
            "ONE BELPARK XXI",
            "PGC XXI",
            "PLAZA INDONESIA XXI",	
            "PLUIT JUNCTION XXI"
        ]

        movies = [
            "Batman",
            "Superman",
            "Spiderman",
            "Marvel",
            "Aquaman",
            "Fantastic Four"
        ]
        

        from api.models import Movie, Theater, Showtime
        
        list_of_movies = []
        # Iterate to Movies

        self.stdout.write("===== Adding Movies =====")
        for movies_name in movies:
            self.stdout.write(">{}".format(movies_name))
            # create movie
            current_movie = Movie(name=movies_name)
            current_movie.save()
            list_of_movies.append(current_movie)

        self.stdout.write("===== Adding Theater =====")
        for theater_name in theaters:
            self.stdout.write(">{}".format(theater_name))
            # create theater
            current_theater = Theater(name=theater_name)
            current_theater.save()

            # adding showtime to each movie in one theater
            for movie in list_of_movies:
                self.stdout.write(">{}'showtime added".format(movie.name))
                current_theater.showtime.create(theater=current_theater,movie=movie)

        self.stdout.write("Done")




