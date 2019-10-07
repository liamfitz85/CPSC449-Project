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
    
@app.route("/api/v1/collections/playlists/new", methods = ["POST"])
def createPlaylist():
    playlist = request.data
    requiredFields = ["title", "albumTitle", "artist", "length", "mediaURL"]
    
    if not all([field in playlist for field in requiredFields]):
        raise exceptions.ParseError()
    try:
        playlist['id'] = queries.create_playlist(**playlist)
    except Exception as e:
        return { 'error': str(e) }, status.HTTP_409_CONFLICT
        
    return song, status.HTTP_201_CREATED
    
@app.route("/api/v1/collections/playlists/", methods = ["GET"])
def filterPlaylists():
    temp = request.args
    id = temp.get("id")
    title = temp.get("title")
    user = temp.get("user")
    
    query = "SELECT * FROM playlists WHERE"
    buffer = None
    buffer2 = None
    to_filter = []
    
    if id:
        buffer += ' id=? AND'
        to_filter.append(id)
    if title:
        buffer += ' title=? AND'
        to_filter.append(title)
    if user:
        buffer += ' user=? AND'
        buffer2 = 1
        to_filter.append(albumTitle)
    if not (id or title or albumTitle):
        raise exceptions.NotFound()    
     
     #I have no idea if this is right or not
    if buffer2 is not None:
        query = "SELECT playlists.id, playlists.title, playlists.user, playlist.desc, playlist.listOfTracks, user.name FROM playlists INNER JOIN users ON playlists.user = users.id WHERE" + buffer
    else:
        query += buffer
     
    query = query[:-4] + ';'

    results = plQueries._engine.execute(query, to_filter).fetchall()

    return list(map(dict, results))