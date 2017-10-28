import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyPlayList:
    __ID_NAME = 'name'
    __ID_DESCRIPTION = 'description'
    __ID_TRACKS = 'tracks'
    __ID_TRACKS_ITEMS = 'items'
    __ID_TRACKS_ITEMS_TRACK = 'track'
    __ID_TRACKS_ITEMS_TRACK_ID = 'id'
    __ID_TRACKS_ITEMS_TRACK_NAME = 'name'
    __ID_TRACKS_ITEMS_TRACK_ARTISTS = 'artists'
    __ID_TRACKS_ITEMS_TRACK_ARTISTS_NAME = 'name'
    __connection = 0
    __full_results_json__ = ''
    playlist_name = ''
    playlist_description = ''
    playlist_owner = ''
    playlist_id = ''
    playlist_tracks = []

    def __init__(self, playlist_owner, playlist_id):
        self.playlist_id = playlist_id
        self.playlist_owner = playlist_owner
        self.__createConnection()
        self.__updatePlaylistData__()

    def __createConnection(self):
        client_credentials_manager = SpotifyClientCredentials()
        self.__connection = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def __updatePlaylistData__(self):
        self.__full_results_json__ = self.__connection.user_playlist(self.playlist_owner, self.playlist_id)
        self.playlist_name = self.__full_results_json__[self.__ID_NAME]
        self.playlist_description = self.__full_results_json__[self.__ID_DESCRIPTION]

        self.playlist_tracks.clear()
        tracks = self.__full_results_json__[self.__ID_TRACKS][self.__ID_TRACKS_ITEMS]
        for track in tracks:
            track = track[self.__ID_TRACKS_ITEMS_TRACK]
            track_id = track[self.__ID_TRACKS_ITEMS_TRACK_ID]
            track_name = track[self.__ID_TRACKS_ITEMS_TRACK_NAME]
            track_artist = track[self.__ID_TRACKS_ITEMS_TRACK_ARTISTS][0][self.__ID_TRACKS_ITEMS_TRACK_ARTISTS_NAME]
            self.playlist_tracks.append(SpotifyTrack(track_id, track_name, track_artist))


class SpotifyTrack:
    track_id = ''
    name = ''
    artist = ''

    def __init__(self, track_id, name, artist):
        self.track_id = track_id
        self.name = name
        self.artist = artist
