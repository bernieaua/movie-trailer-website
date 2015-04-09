# create class to store movie related information
class Movie():
    """ This class provides a way to store movie related information. """

    def __init__(self, title, releasedate, rating, storyline, director, stars, poster_image, trailer_url):
        self.title = title
        self.releasedate = releasedate
        self.rating = rating
        self.storyline = storyline
        self.director = director
        self.stars = stars
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url
