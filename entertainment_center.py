import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://pics.filmaffinity.com/toy_story_3-691147043-large.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

toy_story2 = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

toy_story3 = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://pics.filmaffinity.com/toy_story_3-691147043-large.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

toy_story4 = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

toy_story5 = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://pics.filmaffinity.com/toy_story_3-691147043-large.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

toy_story6 = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


movies = [toy_story,toy_story2,toy_story3,toy_story4,toy_story5,toy_story6]

fresh_tomatoes.open_movies_page(movies)
