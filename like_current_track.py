import os, sys, collections, spotipy, argparse
from spotipy.oauth2 import SpotifyOAuth

# Spotify authorisation scopes
scope = "user-read-currently-playing user-library-modify"

# Initialise spotipy library
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Get currently playing track and add to saved tracks
current_track = spotify.currently_playing()['item']['id']
spotify.current_user_saved_tracks_add(tracks=[current_track])
