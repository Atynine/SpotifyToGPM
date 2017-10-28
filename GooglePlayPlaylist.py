from gmusicapi import Mobileclient
from SpotifyPlaylist import SpotifyTrack
import os


class GooglePlayPlaylist:
    __ENVIRONMENT_USERNAME = 'GOOGLE_PLAY_USERNAME'
    __ENVIRONMENT_PASSWORD = 'GOOGLE_PLAY_PASSWORD'
    __username = ''
    __password = ''
    __api = 0
    playlist_name = ''
    playlist_id = 0

    def __init__(self, username=os.environ[__ENVIRONMENT_USERNAME], password=os.environ[__ENVIRONMENT_PASSWORD]):
        self.__username = username
        self.__password = password
        if not self.__createConnection():
            raise ValueError("Authentication failed")

    def __createConnection(self):
        self.__api = Mobileclient()
        return self.__api.login(self.__username, self.__password, Mobileclient.FROM_MAC_ADDRESS)

    def createPlaylist(self, playlist_name, playlist_description, tracks = []):
        self.loadByName(playlist_name)
        if self.playlist_id != 0:
            self.__deletePlaylist()
        self.__createPlaylist(playlist_name, playlist_description)
        self.addTracks(tracks)

    def addTracks(self, tracks):
        if self.playlist_id == 0:
            raise ValueError("Invalid playlist ID. Call #loadByName to load a playlistID into memory")
        track_ids = []
        for track in tracks:
            track_id = self.__getTrackId__(track.name, track.artist)
            if track_id != '-1':
                track_ids.append(track_id)
        self.__api.add_songs_to_playlist(self.playlist_id, track_ids)
        return self.playlist_id

    def __getTrackId__(self, track_name, track_artist):
        results = self.__api.search(track_name + " " + track_artist)
        songs = results['song_hits']
        if len(songs) == 0:
            return '-1'
        return songs[0]['track']['storeId']

    def loadByName(self, playlist_name):
        playlists = self.__api.get_all_playlists()
        for playlist in playlists:
            if playlist['name'] == playlist_name:
                self.playlist_name = playlist_name
                self.playlist_id = playlist['id']
                return playlist['id']
        self.playlist_id = 0
        return 0

    def __createPlaylist(self, playlist_name, playlist_description):
        id = self.__api.create_playlist(playlist_name, playlist_description)
        self.playlist_id = id
        return id

    def __deletePlaylist(self):
        return self.__api.delete_playlist(self.playlist_id)
