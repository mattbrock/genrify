# Genrify

Select tracks from Saved Albums or Playlists on Spotify based on Artist Genre and add them to Queue or to a new Playlist.

## Requirements

* A [Spotify](https://www.spotify.com/) account.
* [Python 3](https://www.python.org/).
* [Spotipy](https://spotipy.readthedocs.io/) Python library.

## Setup

* Create Spotify app, get Client ID and Secret.
* Copy _setup_template_ to _setup_ and add Client ID and Secret.
* (Assuming you're using Bash or similar) import setup environment variables with `. setup`.

## Usage

Assuming `python` is a symlink to `python3`:

    python genrify.py

## Improvements

* Add breakpoints to UI so that CTRL-C is not necessary to quit.
* Code could be made more modular by splitting parts off into more repeatable functions.
* Select from albums other than the 50 most recently added.
* Be able to handle more than 50 playlists, and format playlist list better.
* Improve interface, ideally by migrating to a web-based UI.
