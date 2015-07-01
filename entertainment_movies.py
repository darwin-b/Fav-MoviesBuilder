import my_movies
import media


toy_story = media.Movie("Toy Story ", "A story of a boy and his toys that come to life." ,
        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)
big_hero = media.Movie("Big Hero 6","storyline ",
                       "http://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
                       "https://www.youtube.com/watch?v=z3biFxZIJOQ")

avatar = media.Movie("Avatar", "A marine on an alien planet.", 
        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", 
        "https://www.youtube.com/watch?v=5PSNL1qE6VY")


the_dark_knight = media.Movie("The Dark Knight", "Storyline", 
        "http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", 
        "https://www.youtube.com/watch?v=yQ5U8suTUw0")

interstellar = media.Movie("Interstellar", "Storyline", 
        "http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", 
        "https://www.youtube.com/watch?v=zSWdZVtXT7E")

inception = media.Movie("Inception", "Storyline", 
        "http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg", 
        "https://www.youtube.com/watch?v=8hP9D6kZseM")

hunger_games = media.Movie("Hunger Games", "Storyline ", 
        "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", 
        "https://www.youtube.com/watch?v=PbA63a7H0bo")




movies= {toy_story,avatar,the_dark_knight,interstellar,inception,big_hero,hunger_games}
my_movies.open_movies_page(movies)


#checking
"""
#hunger_games.show_trailer()
midnight_in_paris.show_trailer()
ratatouille.show_trailer()
#school_of_rock.show_trailer()
avatar.show_trailer()
toy_story.show_trailer()
"""

