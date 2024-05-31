# Genrify

Select tracks from Saved Albums or Playlists on Spotify based on Artist Genre and add them to Queue or to a new Playlist.

## Purpose

I got frustrated at having a Spotify library of added albums and created playlists, but not being able to query my library by genre.
Basically, I wanted functionality like Smart Playlists in Apple's Music app (previously iTunes), where it's possible to say something like
"select all songs from recently added albums where the genre is darkwave". Therefore, with the goal in mind of being able to do something
similar with my Spotify library, I created this Python 3 app 
called Genrify which uses Spotify's API via the Spotipy Python library to achieve this functionality.

My Genrify app allows choosing a genre from recently added albums (Saved Albums) or from a Playlist, then it gives the choice of
adding all the tracks associated with that genre (obtained from the genre of the artist for each track) to the Queue or to a new Playlist.

The interface is currently rather rudimentary, especially given that it uses a basic CLI in a terminal,
but it works well to achieve the goal I was aiming for.

Please feel free to fork this and improve on it.

Accompanying [blog article](https://blog.cetre.co.uk/genrify-python-app-to-filter-spotify-library-based-on-genre/).

## Requirements

* A [Spotify](https://www.spotify.com/) account.
* [Python 3](https://www.python.org/).

## Setup

1. Log in to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) with your Spotify account.
1. Choose CREATE AN APP, give it a name and description, tick the "I understand" box, and choose CREATE.
1. Make a note of the Client ID and Client Secret.
1. Choose EDIT SETTINGS and add `http://127.0.0.1:9090` under Redirect URIs, then choose SAVE.
1. Copy _setup\_template_ to _setup_, then edit _setup_ and add the Client ID and Client Secret for your newly created Spotify app.
1. (Assuming you're using Bash or similar) import the setup environment variables with `. setup`.
2. Create virtualenv: `python3 -m venv .venv` if not previously done, then `source .venv/bin/activate`.
3. Install requirements if needed: `python3 -m pip install -r requirements.txt`.

## Usage

Run application:

    python3 genrify.py

## Desirable improvements

* Add breakpoints to UI so that CTRL-C is not necessary to quit.
* Fail with nicer error when no active device found when adding to Queue.
* Code could be made more modular by splitting parts off into more repeatable functions.
* Select from albums other than the 50 most recently added.
* Be able to handle more than 50 playlists, and format playlist list better.
* Be able to add more than 100 tracks.
* Improve interface, ideally by migrating to a web-based UI.