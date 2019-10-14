import sys
from flask import request
import flask_api
from flask_api import status, exceptions
import pugsql

app = flask_api.FlaskAPI(__name__)
app.config.from_envvar("APP_CONFIG")

trackQueries = pugsql.module("queries/trackQueries/")
trackQueries.connect(app.config["DATABASE_URL"])

def validContentType(request, type='application/json'):
    if request.headers.has_key('Content-Type'):
        if request.headers['Content-Type'] == type:
            return True
    return { 'Error':'Unsupported Media Type', 'Support-Content-Type':type}, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE

@app.route('/api/v1/', methods=['GET'])
def home():
	return "<h1>Music Collection<h1><p>This site is a prototype API for your music collection.</p><p>This is the track handler.</p>"
    
@app.route("/api/v1/collections/tracks/all", methods = ["GET"])
def allTracks():
    allTracks = trackQueries.all_tracks()
    allTracks = list(allTracks)
    if len(allTracks) is 0:
        raise exceptions.NotFound()
    else:
        return list(allTracks)

@app.route("/api/v1/collections/tracks/<int:trackID>", methods = ["GET", "DELETE"])
def filterTrackByID(trackID):
    if request.method == "GET":
        trackByID = trackQueries.track_by_id(trackID=trackID)
        if trackByID is None:
            raise exceptions.NotFound()
        return trackByID
    elif request.method == "DELETE":
        try:
            affected = trackQueries.delete_by_id(trackID = trackID)
            if affected == 0:
                return { 'Error': "TRACK NOT FOUND" },status.HTTP_404_NOT_FOUND
            else:
                return { 'DELETE REQUEST ACCEPTED': str(trackID) }, status.HTTP_202_ACCEPTED               
        except Exception as e:
            return { 'Error': str(e) }, status.HTTP_409_CONFLICT


        
@app.route('/api/v1/collections/tracks', methods=['GET', 'POST', 'PATCH'])
def tracks():
    if request.method == 'GET':
        results = filterTracks(request.args)
        if len(results) is 0:
            raise exceptions.NotFound()
        else:
            return results
    elif request.method == 'POST':
        valid = validContentType(request)
        if valid is not True:
            return valid
        return createTrack(request.data)
    elif request.method == 'PATCH':
        valid = validContentType(request)
        if valid is not True:
            return valid
        return editTrack(request.data)
    

def createTrack(track):
    track = request.data
    requiredFields = ["trackTitle", "trackAlbum", "trackArtist", "trackLength", "trackMediaURL"]
    
    if not all([field in track for field in requiredFields]):
        raise exceptions.ParseError()
    if "trackArt" not in track:
        track["trackArt"] = None
    try:
        track['trackID'] = trackQueries.create_track(**track)
    except Exception as e:
        return { 'error': str(e) }, status.HTTP_409_CONFLICT
        
    return track, status.HTTP_201_CREATED
    
def editTrack(track):
    track = request.data
    requiredFields = ["trackID", "trackTitle", "trackAlbum", "trackArtist", "trackLength", "trackMediaURL", "trackArt"]
    if not all([field in track for field in requiredFields]):
        raise exceptions.ParseError()
    else:
        try:
            affected = trackQueries.edit_track(**track)
            if affected is 0:
                raise exceptions.ParseError("Update Failed")
            else:
                result = trackQueries.track_by_id(**track)
                return result, status.HTTP_200_OK
        except Exception as e:
            return {'error':str(e)}, status.HTTP_409_CONFLICT
    
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