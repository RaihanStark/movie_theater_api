import json

DESCRIPTION_PLACEHOLDER = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus hendrerit eros nec urna porta, vel maximus felis pharetra. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Donec mattis pellentesque nibh, ut dignissim nisi maximus in. Sed egestas luctus nisl. Morbi interdum orci tellus, quis varius turpis aliquam vel. In sed neque blandit, commodo sapien nec, tristique enim. Vestibulum finibus facilisis placerat. Mauris placerat scelerisque tristique."
THEATER_THUMBNAIL_URL_DEFAULT = "https://www.dailynews.com/wp-content/uploads/2018/03/sgt-l-movie-theaters-0223-1-1.jpg"
MOVIE_THUMBNAIL_URL_DEFAULT = "https://everyfad.com/static/images/movie_poster_placeholder.29ca1c87.svg"

showtime = {
    "times":["{}:00 WIB".format(i) for i in range(10,24) if i % 2 == 0]
}
SHOWTIME_DATA_DEFAULT = json.dumps(showtime)