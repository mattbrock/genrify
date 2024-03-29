import os, sys, collections, spotipy
from spotipy.oauth2 import SpotifyOAuth

# Function to get Selected Genre and Track IDs from Saved Albums
def tracks_from_saved_albums():

    # Get Album IDs and Artist IDs from Saved Albums
    album_ids = []
    album_artist_ids = []
    saved_albums = spotify.current_user_saved_albums(limit=50, offset=0, market=None)
    for idx, album in enumerate(saved_albums['items']):
        album_id = album['album']['id']
        album_ids.append(album_id)
        artist_id = album['album']['artists'][0]['id']
        album_artist_ids.append(artist_id)
    
    # Get Genres from list of Artist IDs
    # Create list of Album Genres corresponding to Artist ID list
    # Also create overall list of Album Genres
    album_genre_list = []
    album_genres = []
    for artist_id in album_artist_ids:
        genre_list = []
        artist_data = spotify.artist(artist_id)
        for item in (artist_data['genres']):
            genre_list.append(item)
            album_genres.append(item)
        album_genre_list.append(genre_list)
      
    # Sort and count overall list of Genres
    # Present list to choose Selected Genre from
    collection = collections.Counter(album_genres)
    sorted_album_genres = collection.most_common(20)
    os.system('clear')
    print("Top 20 Genres from 50 most recent Saved Albums:")
    print("")
    i = 1
    for genre in sorted_album_genres:
        print(str(i) + '. ' + genre[0] + ' (' + str(genre[1]) + ' albums)')
        i += 1
    print("")
    print("Select Genre:")
    selection = int(input()) -1
    selected_genre = sorted_album_genres[selection][0]
    
    # Go through Album Genre list and add to
    # Selected Album IDs if Selected Genre is matched
    selected_album_ids = []
    i = 0
    for genre in album_genre_list:
        if selected_genre in genre:
            selected_album_ids.append(album_ids[i])
        i += 1
    
    # Create corresponding lists of Artists,
    # Track IDs and Track Names
    # from all Tracks in list of Selected Album IDs
    selected_artists = []
    selected_track_ids = []
    selected_track_names = []
    album_data = spotify.albums(selected_album_ids)
    for idx, album in enumerate(album_data['albums']):
        for track in album['tracks']['items']:
            selected_artists.append(track['artists'][0]['name'])
            selected_track_ids.append(track['id'])
            selected_track_names.append(track['name'])
    
    # Print selected Artists and Tracks
    # (currently disabled in favour of total selected tracks
    # as that gives cleaner output)
    #os.system('clear')
    #print('Tracks for selected Genre "' + selected_genre + '":')
    #print("")
    #i = 0
    #while i < len(selected_artists):
    #    print(selected_artists[i], "-", selected_track_names[i])
    #    i += 1
    #print("")
    
    # Print total number of selected tracks
    os.system('clear')
    print(str(len(selected_track_names)) + ' tracks to add for selected genre "' + selected_genre + '":')
    print("")

    return selected_genre, selected_track_ids, selected_track_names

# Function to get Selected Genre and Track IDs from selected Playlist
def tracks_from_playlists():

    # Get list of Playlists
    playlists = spotify.current_user_playlists()
    
    # Retrieve and store Playlist information
    playlist_ids = []
    playlist_names = []
    playlist_totals = []
    for idx, playlist in enumerate(playlists['items']):
        playlist_ids.append(playlist['id'])
        playlist_names.append(playlist['name'])
        playlist_totals.append(playlist['tracks']['total'])
    
    # Present user with available Playlist information
    os.system('clear')
    print("Available Playlists:")
    print("")
    i = 0
    while i < len(playlist_ids):
        print(str(i + 1) + '. ' + playlist_names[i] + ' (' + str(playlist_totals[i]) + ' tracks)')
        i += 1
     
    # Allow user to choose a Playlist for processing and get track info from Playlist
    print("")
    print("Select Playlist:")
    selection = int(input()) -1
    selected_playlist_id = playlist_ids[selection]
    results = spotify.playlist(selected_playlist_id, fields=None, market=None, additional_types=('track', ))
    
    # Retrieve and store info on tracks from Playlist
    tracks = []
    track_ids = []
    artists = []
    artist_ids = []
    for idx, item in enumerate(results['tracks']['items']):
        track = item['track']
        tracks.insert(idx, track['name'])
        track_ids.insert(idx, track['id'])
        artists.insert(idx, track['artists'][0]['name'])
        artist_ids.insert(idx, track['artists'][0]['id'])
    
    # Get all genres for each artist in Playlist 
    # and store for processing
    genres = []
    playlist_genres = []
    i = 0
    for artist_id in artist_ids:
        genre_list = []
        artist_data = spotify.artist(artist_id)
        for item in (artist_data['genres']):
            genre_list.append(item)
            playlist_genres.append(item)
        genres.append(genre_list)
        i += 1
    
    # Sort Playlist genres into 20 most common
    c = collections.Counter(playlist_genres)
    sorted_playlist_genres = c.most_common(20)
    
    # Present user with list of the 20 most common genres
    os.system('clear')
    print('Available Genres from Playlist:')
    print("")
    i = 1
    for genre in sorted_playlist_genres:
        print(str(i) + '. ' + genre[0] + ' (' + str(genre[1]) + ' tracks)')
        i += 1
    
    # Allow user to choose a genre
    print("")
    print("Select genre:")
    selection = int(input()) -1
    print("")
    selected_genre = sorted_playlist_genres[selection][0]
    
    # Loop through all tracks in Playlist and store track
    # when selected genre matches the genre associated with that track
    # (previously determined from the genre of the artist for that track)
    selected_track_ids = []
    selected_track_names = []
    i = 0
    for genre in genres:
        if selected_genre in genre:
            selected_track_ids.append(track_ids[i])
            selected_track_names.append(tracks[i])
        i += 1

    # Print total number of selected tracks
    os.system('clear')
    print(str(len(selected_track_names)) + ' tracks to add for selected genre "' + selected_genre + '":')
    print("")

    return selected_genre, selected_track_ids, selected_track_names

# Function to create Playlist
def create_playlist(selected_genre, selected_track_ids):

    # Create Playlist and get Playlist ID
    playlist_name = "[genrify] " + selected_genre
    playlist_description = 'Playlist automatically created for genre "' + selected_genre + '" by Genrify app.'
    me = spotify.current_user()['id']
    playlist_data = spotify.user_playlist_create(me, playlist_name, public=False, collaborative=False, description=playlist_description)
    playlist_id = playlist_data['id']
    
    # Add selected Track IDs to Playlist
    # (removing old tracks if present via "replace")
    spotify.playlist_replace_items(playlist_id, selected_track_ids)
    
    print("")
    print('Playlist "' + playlist_name + '" created and ' + str(len(selected_track_ids)) + ' tracks added')

# Function to add to Queue
def add_to_queue(selected_genre, selected_track_ids, selected_track_names):

    print("")
    print('Adding ' + str(len(selected_track_ids)) + ' "' + selected_genre + '" tracks to Queue')
    print("")
    
    # Track name printing disabled as too messy
    #i = 1
    #for track_name in selected_track_names:
    #    print(i, "-", track_name)
    #    i += 1
    
    # Add tracks to Queue
    for track_id in selected_track_ids:
        spotify.add_to_queue(track_id, device_id=None)
    
    #print("")

# Spotify authorisation scopes
scope = "user-library-read user-follow-read user-modify-playback-state playlist-read-private playlist-modify-private"

# Initialise spotipy library
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Clear screen
os.system('clear')

# Select from either Saved Albums or a Playlist
print("1. Select from Saved Albums")
print("2. Select from a Playlist")
print("")
print("Choose 1 or 2:")
selection = "0"
while selection != "1" and selection != "2":
    selection = input()
if selection == "1":
    selected_genre, selected_track_ids, selected_track_names = tracks_from_saved_albums()
elif selection == "2":
    selected_genre, selected_track_ids, selected_track_names = tracks_from_playlists()

# Create a Playlist or add to Queue
# Limit number of tracks to 100 so as to not exceed Spotify API limit
print("1. Add to Queue")
print("2. Create Playlist")
print("")
print("Choose 1 or 2:")
selection = "0"
while selection != "1" and selection != "2":
    selection = input()
if selection == "1":
    add_to_queue(selected_genre, selected_track_ids[:100], selected_track_names[:100])
elif selection == "2":
    create_playlist(selected_genre[:100], selected_track_ids[:100])
