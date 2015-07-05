import webbrowser

class Video():

    def __init__(self, movie_title, movie_year, movie_duration):
        self.title = movie_title
        self.year = movie_year
        self.duration = movie_duration


class Movie(Video):
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_year, movie_storyline, poster_image, trailer_youtube, movie_duration):
        self.title = movie_title
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.duration = movie_duration

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)