########################################
#TODO                                                                          #
#STILL NEED TO MAKE A DELETE FUNCTION#
########################################

import sys
from flask import request
import flask_api
from flask_api import status, exceptions
import pugsql

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
    return list(allPlaylists)

@app.route("/api/v1/collections/playlists/<int:id>", methods = ["GET"])
def filterPlaylistsByID(id):
    return plQueries.playlist_by_id(id=id)
    
@app.route('/api/v1/collections/playlists', methods=['GET', 'POST'])
def playlists():
    if request.method == 'GET':
        return filterTracks(request.args)
    elif request.method == 'POST':
        return createPlaylist(request.data)

def createPlaylist(playlist):
    playlist = request.data
    requiredFields = ["title", "user"]
    
    if not all([field in playlist for field in requiredFields]):
        raise exceptions.ParseError()
    try:
        playlist['id'] = plQueries.create_playlist(**playlist)
    except Exception as e:
        return { 'error': str(e) }, status.HTTP_409_CONFLICT
        
    return song, status.HTTP_201_CREATED
    
def filterPlaylists(queryParams):
    id = queryParams.get("id")
    title = queryParams.get("title")
    user = queryParams.get("user")
    
    query = "SELECT * FROM playlists WHERE"
    buffer = None
    buffer2 = None
    to_filter = []
    
    if id:
        buffer += ' playlist.id=? AND'
        to_filter.append(id)
    if title:
        buffer += ' playlist.title=? AND'
        to_filter.append(title)
    if user:
        buffer += ' playlist.user = (SELECT users.userID FROM users WHERE users.name=?) AND' #subject to change
        buffer2 = 1
        to_filter.append(user)
    if not (id or title or user):
        raise exceptions.NotFound()    
     
     #I have no idea if this is right or not
    if buffer2 is not None:
        query = "SELECT playlists.id, playlists.title, playlists.user, playlist.desc, playlist.listOfTracks, users.userFirstName, users.userLastName, users.userMiddleName FROM playlists INNER JOIN users ON playlists.user = users.userID WHERE" + buffer
    else:
        query += buffer
     
    query = query[:-4] + ';'

    results = plQueries._engine.execute(query, to_filter).fetchall()

    return list(map(dict, results))