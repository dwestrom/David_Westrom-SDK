class InternalServerError(Exception):
    pass


class MovieDoesNotExistError(Exception):
    pass


class UnauthorizedError(Exception):
    pass

class TooManyRequests(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "MovieNotExistsError": {
     "message": "Movie with given id doesn't exists",
     "status": 400
    },
    "UnauthorizedError": {
     "message": "Invalid username or password",
     "status": 401
    },
    "TooManyRequests": {
        "message": "Invalid username or password",
        "status": 429
    }
}