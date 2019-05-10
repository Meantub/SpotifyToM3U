from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import config
import sys

uri = sys.argv[1]

client_credentials_manager = SpotifyClientCredentials(
    client_id=config.client['id'],
    client_secret=config.client['secret']
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

results = sp.user_playlist(username, playlist_id)

opened_file = open("playlist.m3u", 'a')

for track in results['tracks']['items']:
    opened_file.write("{}\n".format(track['track']['uri']))

