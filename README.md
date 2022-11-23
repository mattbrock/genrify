# Genrify

Select tracks from Saved Albums or Playlists on Spotify based on Artist Genre and add them to Queue or to a new Playlist.

## Purpose

I got frustrated at having a Spotify library of added albums and created playlists, but not being able to query my library by genre.
Basically, I wanted functionality like Smart Playlists in Apple's Music app (previously iTunes), where it's possible to say something like
"select all songs from recently added albums where the genre is darkwave". Therefore, with this goal in mind, I created this Python 3 app 
called Genrify which uses Spotify's API via the Spotipy Python library to achieve this functionality.

My Genrify app gives you the choice of selecting a genre from recently added albums or from a playlist, then it gives you the choice of
adding all the tracks from that genre to your Queue or to a new Playlist.

The interface is currently rather rudimentary, but it works well to achieve the goal I was aiming for.

## Requirements

* A [Spotify](https://www.spotify.com/) account.
* [Python 3](https://www.python.org/).
* [Spotipy](https://spotipy.readthedocs.io/) Python library.

## Setup

1. Log in to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) with your Spotify account.
1. Choose CREATE AN APP, give it a name and description, tick the "I understand" box, and choose CREATE.
1. Make a note of the Client ID and Client Secret.
1. Choose EDIT SETTINGS and add `http://127.0.0.1:9090` under Redirect URIs, then choose SAVE.
1. Copy _setup_template_ to _setup_, then edit _setup_ and add the Client ID and Client Secret for your Spotify app.
1. (Assuming you're using Bash or similar) import the setup environment variables with `. setup`.

## Usage

Assuming `python` is a symlink to `python3`:

    python genrify.py

## Desirable improvements

* Add breakpoints to UI so that CTRL-C is not necessary to quit.
* Code could be made more modular by splitting parts off into more repeatable functions.
* Select from albums other than the 50 most recently added.
* Be able to handle more than 50 playlists, and format playlist list better.
* Improve interface, ideally by migrating to a web-based UI.
