# import needed modules
import fresh_tomatoes
import media

# create the movie instances and define the movie data
# title, release date, rating, story line, director, stars, poster link, youtube trailer url
jacobs_ladder       = media.Movie("Jacob's Ladder",
                                  "1990",
                                  "7.6",
                                  "Mourning his dead child, a haunted Vietnam war veteran attempts to discover his past while suffering from a severe case of dissociation. To do so, he must decipher reality and life from his own dreams, delusion, and perception of death.",
                                  "Adrian Lyne",
                                  "Tim Robbins, Elizabeth Pe&ntilde;a, Danny Aiello",
                                  "http://upload.wikimedia.org/wikipedia/en/7/70/Jacobsladderposter.jpg",
                                  "https://www.youtube.com/watch?v=U6lHSvKD4uk")

last_temptation     = media.Movie("The Last Temptation of Christ",
                                  "1988",
                                  "7.6",
                                  "The life of Jesus Christ, his journey through life as he faces the struggles all humans do, and his final temptation on the cross.",
                                  "Martin Scorsese",
                                  "Willem Dafoe, Harvey Keitel, Barbara Hershey",
                                  "http://upload.wikimedia.org/wikipedia/en/b/bb/The_Last_Temptation_of_Christ_poster.png",
                                  "https://www.youtube.com/watch?v=qJKxg4p-Alk")

close_encounters    = media.Movie("Close Encounters of the Third Kind",
                                  "1977",
                                  "7.7",
                                  "After an encounter with U.F.O.s, a line worker feels undeniably drawn to an isolated area in the wilderness where something spectacular is about to happen.",
                                  "Steven Spielberg",
                                  "Richard Dreyfuss, Fran&ccedil;ois Truffaut, Teri Garr",
                                  "http://upload.wikimedia.org/wikipedia/en/d/d9/Close_Encounters_poster.jpg",
                                  "https://www.youtube.com/watch?v=59iKRfdMRn0")

the_matrix          = media.Movie("The Matrix",
                                  "1999",
                                  "8.7",
                                  "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                                  "Andy Wachowski, Lana Wachowski",
                                  "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
                                  "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                                  "https://www.youtube.com/watch?v=qPBuOAxOb2E")

tropic_thunder      = media.Movie("Tropic Thunder",
                                  "2008",
                                  "7.0",
                                  "Through a series of freak occurrences, a group of actors shooting a big-budget war movie are forced to become the soldiers they are portraying.",
                                  "Ben Stiller",
                                  "Ben Stiller, Jack Black, Robert Downey Jr.",
                                  "http://upload.wikimedia.org/wikipedia/en/d/d6/Tropic_thunder_ver3.jpg",
                                  "https://www.youtube.com/watch?v=T-6YhRZowgc")

neverending_story   = media.Movie("The NeverEnding Story",
                                  "1984",
                                  "7.4",
                                  "A troubled boy dives into a wonderous fantasy world through the pages of a mysterious book.",
                                  "Wolfgang Petersen",
                                  "Noah Hathaway, Barret Oliver, Tami Stronach",
                                  "http://upload.wikimedia.org/wikipedia/en/9/9b/Neverendingstoryposter.jpg",
                                  "https://www.youtube.com/watch?v=jbncmdHxobg")

# set up an array holding all the movies
movies = [jacobs_ladder, last_temptation, close_encounters, the_matrix, tropic_thunder, neverending_story]

# using the fresh_tomatoes module, create the web page and open the page in a browser
fresh_tomatoes.open_movies_page(movies)

