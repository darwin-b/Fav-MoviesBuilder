import my_movies
import media
import json


fav_movies_list =[]
with open('fav_movieslist.json', 'r') as f:
    data = json.load(f)
    print(data)
    for movie in data.values():
        fav_movies_list.append(media.Movie(movie["title"], movie["storyline"], movie["poster_image_url"], movie["trailer_youtube_url"]))
        
my_movies.open_movies_page(fav_movies_list)