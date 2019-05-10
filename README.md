# SpotifyToM3U
I needed a tool to use for foobar2000 so that I could import all of my spotify playlists into it. This does just that using spotipy, a python library, to connect to Spotify and get all the track URIs from it.

## How to use
1. ```pip install -r requirements.txt```
2. Get a developer client id and secret from Spotify's developer website and then paste them into `config.py`
3. ```python spotifytom3u.py <Spotify Playlist URI>```
4. It'll create a file called `playlist.m3u` with all the track URIs from Spotify