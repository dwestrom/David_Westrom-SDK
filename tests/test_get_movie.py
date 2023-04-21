from src.theoneapi_dwestrom import the_one_api
import src.theoneapi_dwestrom.resources.errors as errors
import unittest


class GetMovieTest(unittest.TestCase):
    def test_get_valid_movie(self):
        # first get the list of movies and find a valid movie id
        movies_dict = the_one_api.get_movies()
        movie_id = movies_dict["docs"][0]['_id']
        self.assertTrue(len(movie_id) > 0, 'movie_id is empty')
        self.assertTrue(type(movie_id) == str, 'movie_id is not a string')

        # now check that we can retrieve the movie by id and that it has a name
        movie_dict = the_one_api.get_movie_details(movie_id)
        self.assertEqual(movie_id, movie_dict["docs"][0]['_id'], 'unable to retrieve same movie')
        self.assertIn('name', movie_dict["docs"][0], 'movie name not defined')

    def test_get_missing_movie(self):
        missing_movie_id = '12345'
        with self.assertRaises(errors.MovieDoesNotExistError):
            movie_dict = the_one_api.get_movie_details(missing_movie_id)
