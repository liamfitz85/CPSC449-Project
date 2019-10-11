#############################################################
#TODO                                                                                                                          #
#STILL NEED TO CREATE AN EDIT FUNCTION AND CHECK FOR JSON#
#############################################################

import sys
from flask import request
import flask_api
from flask_api import status, exceptions
import pugsql

app = flask_api.FlaskAPI(__name__)
app.config.from_envvar("APP_CONFIG")

trackQueries = pugsql.module("queries/trackQueries/")
trackQueries.connect(app.config["DATABASE_URL"])

@app.route('/api/v1/', methods=['GET'])
def home():
	return "<h1>Music Collection<h1><p>This site is a prototype API for your music collection.</p><p>This is the track handler.</p>"
    
@app.route("/api/v1/collections/tracks/all", methods = ["GET"])
def allTracks():
    allTracks = trackQueries.all_tracks()
    return list(allTracks)

@app.route("/api/v1/collections/tracks/<int:trackID>", methods = ["GET"])
def filterTrackByID(trackID):
    trackByID = trackQueries.track_by_id(trackID=trackID)
    return list(trackByID)
    
@app.route('/api/v1/collections/tracks', methods=['GET', 'POST', 'DELETE'])
def tracks():
    if request.method == 'GET':
        return filterTracks(request.args)
    elif request.method == 'POST':
        return createTrack(request.data)
    elif request.method == 'DELETE':
        results = filterTracks(request.args)
        if len(results) is 0:
            raise exceptions.NotFound()
        else:
            return deleteTrack(request.args)
        
def deleteTrack(deleteParams):
    trackID = deleteParams.get("trackID")
    trackTitle = deleteParams.get("trackTitle")
    trackAlbum = deleteParams.get("trackAlbum")
    trackArtist = deleteParams.get("trackArtist")
    
    deleteQuery = "DELETE FROM tracks WHERE"
    to_filter = []
    
    if trackID:
        deleteQuery += ' trackID=? AND'
        to_filter.append(trackID)
    if trackTitle:
        deleteQuery += ' trackTitle=? AND'
        to_filter.append(trackTitle)
    if trackAlbum:
        deleteQuery += ' trackAlbum=? AND'
        to_filter.append(trackAlbum)
    if trackArtist:
        deleteQuery += ' trackArtist=? AND'
        to_filter.append(trackArtist)
    if not (trackID or trackTitle or trackAlbum or trackArtist):
        raise exceptions.NotFound() 
        
    deleteQuery = deleteQuery[:-4] + ';'

    results = trackQueries._engine.execute(deleteQuery, to_filter)
    result = []
    return result, status.HTTP_200_OK

def createTrack(song):
    song = request.data
    requiredFields = ["trackTitle", "trackAlbum", "trackArtist", "trackLength", "trackMedia"]
    
    if not all([field in song for field in requiredFields]):
        raise exceptions.ParseError()
    try:
        song['trackID'] = trackQueries.create_track(**song)
    except Exception as e:
        return { 'error': str(e) }, status.HTTP_409_CONFLICT
        
    return song, status.HTTP_201_CREATED
    
def filterTracks(queryParams):
    trackID = queryParams.get("trackID")
    trackTitle = queryParams.get("trackTitle")
    trackAlbum = queryParams.get("trackAlbum")
    trackArtist = queryParams.get("trackArtist")
    
    query = "SELECT * FROM tracks WHERE"
    to_filter = []
    
    if trackID:
        query += ' trackID=? AND'
        to_filter.append(trackID)
    if trackTitle:
        query += ' trackTitle=? AND'
        to_filter.append(trackTitle)
    if trackAlbum:
        query += ' trackAlbum=? AND'
        to_filter.append(trackAlbum)
    if trackArtist:
        query += ' trackArtist=? AND'
        to_filter.append(trackArtist)
    if not (trackID or trackTitle or trackAlbum or trackArtist):
        raise exceptions.NotFound()
        
    query = query[:-4] + ';'

    results = trackQueries._engine.execute(query, to_filter).fetchall()

    return list(map(dict, results))