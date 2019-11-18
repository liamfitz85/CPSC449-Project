import json, requests
from xspf import xspf
from flask import request, jsonify, Response
import flask_api
from flask_api import status, exceptions
app = flask_api.FlaskAPI(__name__,static_url_path='')
# app.config.from_envvar('APP_CONFIG') # maybe

def getPlayListByID(id, playlists):
    for playlist in playlists:
        if playlist['playID'] == id:
            return playlist
    return

def getUserByID(id):
    userstr = "http://localhost:8000/api/v1/users/id/%d" % (id)
    user = requests.get(userstr).json()
    # print(user)
    return user

def getDescriptionByUser(uid):
    descstr = "http://localhost:8000/api/v1/descriptions/users/%s/descriptions/all" % (uid)
    desc = requests.get(descstr).json()
    return desc

def getPlayListURLs(playlist):
    urls = playlist['playListOfTracks'].strip('[]').split(',')
    playlist_urls = []
    for url in urls:
        playlist_urls.append(url.strip(' ').strip('\''))
    return playlist_urls

def getTrackInfoFromURL(urls, tracks, playlist):
    # print(playlistTitle)
    x = xspf.Xspf()
    x.title = playlist['playTitle']

    user = getUserByID(playlist['playUserID'])
    
    x.creator = user['userUserName']

    desc = getDescriptionByUser(user['userUserName'])
    # print(desc)
    # x.info = user['userName']
    x.annotation = playlist['playDesc']
    for url in urls:
        # print(url)
        tr = xspf.Track()
        for track in tracks:
            # print(track)
            if url in track['trackMediaURL']:
                # print(track)
                tr.creator = track['trackArtist']
                tr.title = track['trackTitle']
                tr.album = track['trackAlbum']
                tr.duration = str(track['trackLength']) # cast to string, cannot serialize otherwise.
                tr.location = track['trackMediaURL']
                tr.image = track['trackArt']
                # print(track['trackMediaURL'])
                # print(type(desc))
                # print(desc[0]['trackMediaURL'])
                if track['trackMediaURL'] == desc[0]['trackMediaURL']:
                    tr.annotation = desc[0]['descriptionDesc']
                x.add_track(tr)
    return x

# playlist = getPlayListByID(3, playlists)
# tracklist = getPlayListURLs(playlist)
# xmlplaylist = getTrackInfoFromURL(tracklist, tracks, playlist)

# print(xmlplaylist.toXml())

import xml.dom.minidom
# print(xml.dom.minidom.parseString(xmlplaylist.toXml()).toprettyxml())

# print(tracklist)

# print(type(tracklist))
# print(tracklist[0])

# getTrackInfoFromURL(playlist, tracklist)

# getTrackInfoFromURL(playlist, tracklist)

# getTrackInfoFromURL(tracklist, tracks, playlist['playTitle'])

# print("test")

@app.route("/api/v1/collections/playlists/<int:playID>/xspf", methods = ['GET'])
def generate_xspf(playID):
    playlists = requests.get("http://localhost:8000/api/v1/collections/playlists/all").json()
    tracks = requests.get("http://localhost:8000/api/v1/collections/tracks/all").json()
    playlist = getPlayListByID(playID, playlists)
    print(playlist)
    tracklist = getPlayListURLs(playlist)
    print(tracklist)
    xspf_playlist = getTrackInfoFromURL(tracklist, tracks, playlist)

    return xml.dom.minidom.parseString(xspf_playlist.toXml()).toprettyxml(), status.HTTP_200_OK