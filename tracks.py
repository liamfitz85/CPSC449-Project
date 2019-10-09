#####################################################
#TODO                                                                                                       #
#STILL NEED TO CREATE AN EDIT AND DELETE FUNCTION#
####################################################

import sys
from flask import request
import flask_api
from flask_api import status, exceptions
import pugsql
from usefultool.py import jasonifier, validContentType

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
    return jasonifier(list(allTracks))

@app.route("/api/v1/collections/tracks/<int:trackID>", methods = ["GET"])
def filterTrackByID(trackID):
    trackByID = trackQueries.track_by_id(trackID=trackID)
    return jasonifier(list(trackByID))
    
@app.route('/api/v1/collections/tracks', methods=['GET', 'POST', 'DELETE'])
def tracks():
    if request.method == 'GET':
        return filterTracks(request.args)
    elif request.method == 'POST':
        return createTrack(request.data)
    elif request.method == 'DELETE':
        #return deleteTrack(request.args)
        
# def deleteTrack(deleteParams):
    # trackID = deleteParams.get("trackID")
    # trackTitle = deleteParams.get("trackTitle")
    # trackAlbum = deleteParams.get("trackAlbum")
    
    # deleteQuery = "DELETE * FROM tracks WHERE"
    # selectQuery = "SELECT * FROM tracks WHERE"
    # to_filter = []
    
    # if trackID:
        # deleteQuery += ' trackID=? AND'
        # selectQuery += ' trackID=? AND'
        # to_filter.append(id)
    # if trackTitle:
        # deleteQuery += ' trackTitle=? AND'
        # selectQuery += ' trackTitle=? AND'
        # to_filter.append(title)
    # if trackAlbum:
        # deleteQuery += ' trackAlbum=? AND'
        # selectQuery += ' trackAlbum=? AND'
        # to_filter.append(albumTitle)
    # if not (id or title or albumTitle):
        # raise exceptions.NotFound() 
    
    #do a SELECT statement to check if the items are in the database, if they are not throw this
    #selectQuery = selectQuery[:-4] + ';'
    #if not trackQueries._enging.execute(selectQuery, to_filter).fetchall():
    #   
    #   return jasonifier("ITEM COULD NOT BE FOUND", status.HTTP_404_NOT_FOUND)
    #else:    
    #   deleteQuery = deleteQuery[:-4] + ';'

    #   trackQueries._engine.execute(deleteQuery, to_filter).fetchall()
    #   return jasonifier("REQUEST ACCEPTED", status.HTTP_202_ACCEPTED)

def createTrack(song):
    song = request.data
    requiredFields = ["trackTitle", "trackAlbum", "trackArtist", "trackLength", "trackMedia"]
    
    if not all([field in song for field in requiredFields]):
        raise exceptions.ParseError()
    try:
        song['trackID'] = trackQueries.create_track(**song)
    except Exception as e:
        return { 'error': str(e) }, status.HTTP_409_CONFLICT
        
    #return song, status.HTTP_201_CREATED
    return jasonifier(song, status.HTTP_201_CREATED)
    
def filterTracks(queryParams):
    trackID = queryParams.get("trackID")
    trackTitle = queryParams.get("trackTitle")
    trackAlbum = queryParams.get("trackAlbum")
    
    query = "SELECT * FROM tracks WHERE"
    to_filter = []
    
    if trackID:
        query += ' trackID=? AND'
        to_filter.append(id)
    if trackTitle:
        query += ' trackTitle=? AND'
        to_filter.append(title)
    if trackAlbum:
        query += ' trackAlbum=? AND'
        to_filter.append(albumTitle)
    if not (id or title or albumTitle):
        raise exceptions.NotFound()
        
    query = query[:-4] + ';'

    results = trackQueries._engine.execute(query, to_filter).fetchall()

    return jasonifier(list(map(dict, results)))