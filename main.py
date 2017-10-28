import SpotifyPlaylist
import GooglePlayPlaylist


id_playlist_owner = 'PLAYLIST_OWNER'
id_playlist = 'PLAYLIST_ID'

spotify_playlist = SpotifyPlaylist.SpotifyPlayList(id_playlist_owner, id_playlist)
googleplay_playlist = GooglePlayPlaylist.GooglePlayPlaylist()
googleplay_playlist.createPlaylist(spotify_playlist.playlist_name, spotify_playlist.playlist_description, spotify_playlist.playlist_tracks)