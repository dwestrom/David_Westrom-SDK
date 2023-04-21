from src.theoneapi_dwestrom import the_one_api
import unittest

class GetMoviesTest(unittest.TestCase):
    def test_get_movies(self):
        movies_dict = the_one_api.get_movies()
        movie_id = movies_dict["docs"][0]['_id']
        self.assertTrue(movies_dict["total"] >= 1, 'movies set is empty')
        self.assertTrue(type(movie_id) == str, 'movie_id is not a string')