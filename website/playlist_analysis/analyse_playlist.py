"""
This file contains the various functions used when parsing my api call and analysing the playlists.
"""
import os
import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

from dotenv import load_dotenv

load_dotenv()

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
    results = sp.playlist(playlist_id, fields='name,images,tracks')

    playlist_name = results['name']
    playlist_image = results['images'][0]['url']

    # Getting the track names
    track_names = [track['track']['name'] for track in results['tracks']['items']]

    # Now I want to get the track's images
    # These are accessed from the album they are in
    track_images = [track['track']['album']['images'][0]['url'] for track in results['tracks']['items']]

    # Now we need to get the audio features for each track.
    track_ids = [track['track']['id'] for track in results['tracks']['items']]

    # audio_features = sp.audio_features(track_ids)

    track_artists = [[artist['name'] for artist in track['track']['artists']] for track in results['tracks']['items']]
    print(track_artists)


    return playlist_name, playlist_image, zip(track_names, track_artists, track_images)
