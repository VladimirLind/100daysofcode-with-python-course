import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    with open(local) as f:
        reader = csv.DictReader(f)
        dict_movies = {}
        for row in reader:
            if int(row['title_year'] or 0) >= MIN_YEAR:
                movie_tuple = Movie(row['movie_title'].strip(),int(row['title_year'] or 0),float(row['imdb_score']))
                if row['director_name'] not in dict_movies:
                    dict_movies[row['director_name']] = [movie_tuple]
                else:
                    dict_movies[row['director_name']].append(movie_tuple)
    return dict_movies


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    list_score = [movie.score for movie in movies]
    return round(sum(list_score)/len(list_score), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    return sorted([(director,calc_mean_score(movies)) for director, movies in directors.items() if len(movies) >= 4], key=lambda x: x[1], reverse=True)
