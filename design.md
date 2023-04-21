***Design Thoughts***

I think you can get the gist from the readme + the code. The intention is to provide a set of functions that map 1-1 to The One API movie endpoints.

The SDK consolidates requests into one base_get_request() in order to reduce duplicate code and provide one location for common error handling, with room for more custom error handling e.g. get_Movie() with incorrect ID.

I've hard coded my auth token simply for convenience, I wouldn't do this in a SDK meant to be used beyond a handful of folks. I've also included easy ways to override with your own token and called out how to get that generated in the readme.

A small test of tests are included which exercise both the highway and a few edge cases.

This was fun!

David Westrom