"""
This file contains the various functions used when parsing my api call and analysing the playlists.
"""
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Setting up Spotipy to make the API calls easier
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def parse_playlist(uri):
    """
    This function takes as input, a spotify playlist uri.
    It parses it into a pandas dataframe and returns it.
    The user can then view the songs in the dataframe and click submit to add it to persistent storage.
    """
    # Playlist id
    playlist_id = uri.split(":")[2]
    results = sp.playlist(playlist_id, fields='name,images')

    image = results['images'][0]['url']
    name = results['name']

    return name, image