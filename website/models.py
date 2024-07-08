"""
Our database model.
"""
from . import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    playlists = db.relationship("Playlists")

class Playlists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    name = db.Column(db.String(150), unique=True)
    image= db.Column(db.String(150))
    uri = db.Column(db.String(150), unique=True)
    tracks = db.relationship("Tracks", back_populates="playlist")

class Tracks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id"))  # Each track is in a playlist
    name = db.Column(db.String(150))
    image = db.Column(db.String(150))
    danceability = db.Column(db.Float)
    energy = db.Column(db.Float)
    key = db.Column(db.Integer)
    loudness = db.Column(db.Float)
    mode = db.Column(db.Integer)
    speechiness = db.Column(db.Float)
    acousticness = db.Column(db.Float)
    instrumentalness = db.Column(db.Float)
    liveness = db.Column(db.Float)
    valence = db.Column(db.Float)
    tempo = db.Column(db.Float)
    track_id = db.Column(db.String(150), unique=True)
    uri = db.Column(db.String(150))
    track_href = db.Column(db.String(150))
    analysis_url = db.Column(db.String(150))
    duration_ms = db.Column(db.Integer)
    time_signature = db.Column(db.Integer)

    playlist = db.relationship("Playlists", back_populates="tracks")

"""
name
image
{'danceability': 0.607,
'energy': 0.963,
'key': 6,
'loudness': -6.175,
'mode': 1,
'speechiness': 0.0411,
'acousticness': 0.00105,
'instrumentalness': 0.83,
'liveness': 0.0618,
'valence': 0.494,
'tempo': 141.997,
'type': 'audio_features',
'id': '5E5BfT1yJP1goaRINc4Zke',
'uri': 'spotify:track:5E5BfT1yJP1goaRINc4Zke',
'track_href': 'https://api.spotify.com/v1/tracks/5E5BfT1yJP1goaRINc4Zke',
'analysis_url': 'https://api.spotify.com/v1/audio-analysis/5E5BfT1yJP1goaRINc4Zke',
'duration_ms': 345040,
'time_signature': 4}
"""