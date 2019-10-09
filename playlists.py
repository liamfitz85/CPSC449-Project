########################################
#TODO                                                                          #
#STILL NEED TO MAKE A DELETE FUNCTION#
########################################

import sys
from flask import request
import flask_api
from flask_api import status, exceptions
import pugsql
from usefultool.py import jasonifier, validContentType

app = flask_api.FlaskAPI(__name__)
app.config.from_envvar("APP_CONFIG")

plQueries = pugsql.module("queries/playlistQueries/")
plQueries.connect(app.config["DATABASE_URL"])

@app.route('/api/v1/', methods=['GET'])
def home():
	return "<h1>Music Collection<h1><p>This site is a prototype API for your music collection.</p><p>This is the playlist handler.</p>"
    
@app.route("/api/v1/collections/playlists/all", methods = ["GET"])
def allPlaylists():
    allPlaylists = plQueries.all_playlists()
    return jasonifier(list(allPlaylists))

@app.route("/api/v1/collections/playlists/<int:playID>", methods = ["GET"])
def filterPlaylistsByID(playID):
    playlistByID = plQueries.playlist_by_id(playID=playID)
    return jasonifier(list(playlistByID))
    
@app.route("api/v1/users/<string:username>/playlists", methods = ["GET"]) #as requested by Duy
def playlistByUsername(username):
    playlistByUsername = plQueries.playlist_by_username(username = username)
    return jasonifier(list(playlistByUsername))
    
@app.route('/api/v1/collections/playlists', methods=['GET', 'POST', 'DELETE'])
def playlists():
    if request.method == 'GET':
        return filterTracks(request.args)
    elif request.method == 'POST':
        return createPlaylist(request.data)
    elif request.method == 'DELETE':
        #return deletePlaylist()

def createPlaylist(playlist):
    playlist = request.data
    requiredFields = ["playTitle", "playUser", "playListOfTracks"]
    
    if not all([field in playlist for field in requiredFields]):
        raise exceptions.ParseError()
    try:
        playlist['playID'] = plQueries.create_playlist(**playlist)
    except Exception as e:
        return { 'error': str(e) }, status.HTTP_409_CONFLICT
        
    #return song, status.HTTP_201_CREATED
    return jasonifier(song, status.HTTP_201_CREATED)
    
#def deletePlaylist():
    
    
def filterPlaylists(queryParams):
    playID = queryParams.get("playID")
    playTitle = queryParams.get("playTitle")
    userName = queryParams.get("userName")
    
    query = "SELECT P.playID, P.playTitle, P.playDesc, P.listOfTracks, U.userName FROM playlists as P, users as U WHERE"
    to_filter = []
    
    if playID:
        query += ' playID=? AND'
        to_filter.append(playID)
    if playTitle:
        query += ' playTitle=? AND'
        to_filter.append(playTitle)
    if userName:
        query += " U.userName = ? AND P.playUserID = U.userID AND"
        to_filter.append(userName)
    if not (id or title or user):
        raise exceptions.NotFound()  
        
     #############IGNORE THIS#############IGNORE THIS#############IGNORE THIS#############IGNORE THIS#############IGNORE THIS#############IGNORE THIS#############
     #I have no idea if this is right or not
    # if buffer2 is not None:
        # query = "SELECT playlists.playID, playlists.playTitle, playlist.playDesc, playlist.listOfTracks, users.userName FROM playlists INNER JOIN users ON playlists.playUserID = users.userID WHERE" + buffer
    # else:
        # query += buffer
     
    query = query[:-4] + ';'

    results = plQueries._engine.execute(query, to_filter).fetchall()

    return jasonifier(list(map(dict, results)))