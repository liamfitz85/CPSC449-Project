#############################################################
#TODO                                                       #
#STILL NEED TO MAKE A PARSE FUNCTION AND CHECK FOR JSON     #
#############################################################

import sys
from flask import request, jsonify
import flask_api
from flask_api import status, exceptions
import pugsql

app = flask_api.FlaskAPI(__name__)
app.config.from_envvar("APP_CONFIG")

plQueries = pugsql.module("queries/playlistQueries/")
plQueries.connect(app.config["DATABASE_URL"])

def validContentType(request, type='application/json'):
    if request.headers.has_key('Content-Type'):
        if request.headers['Content-Type'] == type:
            return True
    return { 'Error':'Unsupported Media Type', 'Support-Content-Type':type}, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE

@app.route('/api/v1/', methods=['GET'])
def home():
	return "<h1>Music Collection<h1><p>This site is a prototype API for your music collection.</p><p>This is the playlist handler.</p>"
    
@app.route("/api/v1/collections/playlists/all", methods = ["GET"])
def allPlaylists():
    allPlaylists = plQueries.all_playlists()
    allPlaylists = list(allPlaylists)
    if len(allPlaylists) is 0:
        raise exceptions.NotFound()
    else:
        return allPlaylists

@app.route("/api/v1/collections/playlists/<int:playID>", methods = ["GET"])
def filterPlaylistsByID(playID):
    playlistByID = plQueries.playlist_by_id(playID=playID)
    if len(playlistByID) is 0:
        raise exceptions.NotFound()
    else:
        return playlistByID
    
@app.route("/api/v1/users/<string:userUserName>/playlists", methods = ["GET"])
def playlistByUsername(userUserName):
    playlistByUsername = plQueries.playlist_by_username(userUserName = userUserName)
    if len(playlistByUsername):
        raise exceptions.NotFound()
    else:
        return playlistByUsername
    
@app.route('/api/v1/collections/playlists', methods=['GET', 'POST', 'DELETE'])
def playlists():
    if request.method == 'GET':
        return filterPlaylists(request.args)
    elif request.method == 'POST':
        valid = validContentType(request)
        if valid is not True:
            return valid
        return createPlaylist(request.data)
    elif request.method == 'DELETE':
        result = filterPlaylists(request.args)
        if len(result) is 0:
            raise exceptions.NotFound()
        else:
            return deletePlaylist(request.args)
        
def deletePlaylist(deleteParams):
    playID = deleteParams.get("playID")
    playTitle = deleteParams.get("playTitle")
    userName = deleteParams.get("userName")
    
    deleteQuery = "DELETE FROM playlists WHERE playlists.playUserID = users.userID AND"
    to_filter = []
    
    if playID:
        deleteQuery += ' playID=? AND'
        to_filter.append(playID)
    if playTitle:
        deleteQuery += ' playTitle=? AND'
        to_filter.append(playTitle)
    if userName:
        deleteQuery += ' users.userUserName=? AND'
        to_filter.append(userName)
    if not (playID or playTitle or userName):
        raise exceptions.NotFound() 
        
    deleteQuery = deleteQuery[:-4] + ';'

    results = plQueries._engine.execute(deleteQuery, to_filter)
    result = []
    return result, status.HTTP_200_OK

def createPlaylist(playlist):
    playlist = request.data
    requiredFields = ["playTitle", "playUserID", "playListOfTracks"]
    
    if not all([field in playlist for field in requiredFields]):
        raise exceptions.ParseError()
    if "playDesc" not in playlist:
        playlist["playDesc"] = None
    try:
        playlist['playID'] = plQueries.create_playlist(**playlist)
    except Exception as e:
        return { 'error': str(e) }, status.HTTP_409_CONFLICT
        
    return playlist, status.HTTP_201_CREATED
    
def filterPlaylists(queryParams):
    playID = queryParams.get("playID")
    playTitle = queryParams.get("playTitle")
    userName = queryParams.get("userName")
    
    query = "SELECT P.playID, P.playTitle, P.playDesc, P.playListOfTracks, U.userUserName FROM playlists as P, users as U WHERE P.playUserID = U.userID AND"
    to_filter = []
    
    if playID:
        query += ' playID=? AND'
        to_filter.append(playID)
    if playTitle:
        query += ' playTitle=? AND'
        to_filter.append(playTitle)
    if userName:
        query += " U.userUserName = ? AND"
        to_filter.append(userName)
    if not (playID or playTitle or userName):
        raise exceptions.NotFound()  
     
    query = query[:-4] + ';'

    results = plQueries._engine.execute(query, to_filter).fetchall()
    results = list(map(dict, results))

    if len(results) is 0:
        raise exceptions.NotFound()
    else:
        return results