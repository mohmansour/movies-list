#import the modules you need to complete the project-webbrowser give us the ability to access online URLs
import webbrowser

#define a new Class (Movie) to represent the initial form of movies 
class Movie():
    #here is the documentation of class
    """this is the initial class for movies before definition for each movie"""
    #Constructor of class
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #attribute/function to show trailers
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
