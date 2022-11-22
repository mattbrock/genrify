# Genrify

Select tracks from Saved Albums or Playlists on Spotify based on Artist Genre and add to new Playlist or Queue.

## Requirements

* [Python 3](https://www.python.org/)
* [Spotipy Python library](https://spotipy.readthedocs.io/)
* A [Spotify](https://www.spotify.com/) account

## Setup

* Create Spotify app, get Client ID and Secret.
* Copy _setup_template_ to _setup_ and add Client ID and Secret.
* Import setup environment variables with `. setup`.

## Improvements

* Code could be made more modular by splitting parts off into more repeatable functions.
* Select from albums other than the 50 most recently added.
* Be able to handle more than 50 playlists, and format playlist list better.
* Improve interface, ideally by migrating to a web-based UI.
