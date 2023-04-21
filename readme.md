**David_Westrom-SDK***

This SDK is meant to help simplify interaction with [The One API](https://the-one-api.dev/).

***Install***

`python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps theoneapi-dwestrom`

***Usage***

`from theoneapi_dwestrom import the_one_api`

***Exposed Functions***

NOTE: All methods include an optional token parameter for you to supply your own token when using the SDK. [Sign up](https://the-one-api.dev/sign-up) to create a token.

```the_one_api.get_movies(token)``` - Returns a dictionary of LOTR movies.
```the_one_api.get_movie_details(movie_id, token)```  - Returns details about the movie specified by `movie_id`.
```the_one_api.get_movie_quotes(token)``` - Returns a (potentially empty) list of quotes from the movie specified by `movie_id`.

***Test***

Run tests using this command:
`python -m unittest`

***TODO***
- Hook up a .env file. There was some mysterious problem trying to install dotenv package so I decided to punt on this).
- Integrate more of The One API functionality into this SDK.
- More tests!