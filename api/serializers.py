from rest_framework import serializers

from .models import Movie, Theater, Showtime

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','name','description','image_url')

class ShowtimeSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Showtime
        fields = ('id','theater','movie','start_times')

class TheaterSerializer(serializers.ModelSerializer):
    showtime = ShowtimeSerializer(many=True, read_only=True)
    class Meta:
        model = Theater
        fields = ('id','name','image_url', 'showtime')

        def validate(self, validated_data):
            validated_data.showtime = validated_data.showtime.get_showtime()

            return validated_data

