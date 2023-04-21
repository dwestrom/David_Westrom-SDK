from src.theoneapi_dwestrom import the_one_api
import src.theoneapi_dwestrom.resources.errors as errors
import unittest


class GetMovieQuoteTest(unittest.TestCase):
    def test_get_movie_quotes(self):
        # first get the list of movies and find a valid movie id
        movies_dict = the_one_api.get_movies()
        movie_id = movies_dict["docs"][0]['_id']
        self.assertTrue(len(movie_id) > 0, 'movie_id is empty')
        self.assertTrue(type(movie_id) == str, 'movie_id is not a string')

        # now check that we can retrieve the movie by id and that it has a name
        quote_dict = the_one_api.get_movie_quotes(movie_id)
        self.assertTrue(quote_dict["total"] >= 0, 'quote total invalid')

