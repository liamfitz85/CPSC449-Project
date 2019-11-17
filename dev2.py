import json, requests
from xspf import xspf

x = xspf.Xspf()

playlists = requests.get("http://localhost:5200/api/v1/collections/playlists/all").json()
tracks = requests.get("http://localhost:5100/api/v1/collections/tracks/all").json()

def getPlayListByID(id, playlists):
    for playlist in playlists:
        if playlist['playID'] == id:
            return playlist
    return

def getPlayListURLs(playlist):
    urls = playlist['playListOfTracks'].strip('[]').split(',')
    playlist_urls = []
    for url in urls:
        playlist_urls.append(url.strip(' ').strip('\''))
    return playlist_urls

def getTrackInfoFromURL(urls, tracks, playlistTitle):
    print(playlistTitle)
    for url in urls:
        for track in tracks:
            if url in track['trackMediaURL']:
                # print(track['trackTitle'])
                print(track)

        
playlist = getPlayListByID(2, playlists)
tracklist = getPlayListURLs(playlist)

# print(type(tracklist))
# print(tracklist[0])

# getTrackInfoFromURL(playlist, tracklist)

# getTrackInfoFromURL(playlist, tracklist)

getTrackInfoFromURL(tracklist, tracks, playlist['playTitle'])

print("test")