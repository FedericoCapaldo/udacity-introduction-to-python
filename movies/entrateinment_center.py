import fresh_tomatoes
import media 

toy_story = media.Movie('Toy Story', 
                        'A story of a boy and his toys come to life', 
                        'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg', 
                        'https://www.youtube.com/watch?v=vwyZH85NQC4')
# print(toy_story.storyline)

avatar = media.Movie('Avatar', 
                        'A marine that goes very far in life', 
                        'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg', 
                        'https://www.youtube.com/watch?v=-9ceBgWV8io')
# print(avatar.storyline)

a_beatiful_mind = media.Movie('A Beatufiul Mind',
                              'A Beautiful Mind is a 2001 American biographical drama film based on the life of John Nash, a Nobel Laureate in Economics',
                              'https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg',
                              'https://www.youtube.com/watch?v=WFJgUm7iOKw')

# a_beatiful_mind.show_trailer()

school_of_rock = media.Movie('School of Rock',
                             'Storyline',
                             'https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
                             'https://www.youtube.com/watch?v=3PsUJFEBC74')

ratatouille = media.Movie('Ratatouille',
                          'Storyline',
                          'https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg',
                          'https://www.youtube.com/watch?v=c3sBBRxDAqk')

midnight_in_paris = media.Movie('Midnight in Paris',
                                'Storyline',
                                'https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg',
                                'https://www.youtube.com/watch?v=atLg2wQQxvU')

hunger_games = media.Movie('Hunger Games',
                           'Storyline',
                           'https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg',
                           'https://www.youtube.com/watch?v=PbA63a7H0bo')
movies = [toy_story, avatar, a_beatiful_mind, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)

