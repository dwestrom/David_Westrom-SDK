import src.theoneapi_dwestrom.resources.errors as errors
import requests
import json

movies_endpoint = "/movie"
movie_endpoint = "/movie/{}"
quote_endpoint = "/movie/{}/quote"

root_url = "https://the-one-api.dev/v2"
bearer_token = 'Bearer 22dHzCmf2dTe4NDketi_'

def get_movies(token=bearer_token):
    url = root_url + movies_endpoint
    return _base_get_request(url, {'Authorization': token})


def get_movie_details(movie_id, token=bearer_token):
    url = root_url + movie_endpoint.format(movie_id)
    try:
        return _base_get_request(url, {'Authorization': token})
    except errors.InternalServerError:
        raise errors.MovieDoesNotExistError


def get_movie_quotes(movie_id, token=bearer_token):
    url = root_url + quote_endpoint.format(movie_id)
    return _base_get_request(url, {'Authorization': token})


def _base_get_request(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 401:
        raise errors.UnauthorizedError
    if response.status_code == 429:
        raise errors.TooManyRequests
    if response.status_code == 500:
        raise errors.InternalServerError
    return json.loads(response.text)