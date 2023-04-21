from src.theoneapi_dwestrom import the_one_api
import src.theoneapi_dwestrom.resources.errors as errors
import unittest


class AuthFailureTest(unittest.TestCase):
    def test_auth_failure(self):
        with self.assertRaises(errors.UnauthorizedError):
            movies_dict = the_one_api.get_movies(token="bad token")
