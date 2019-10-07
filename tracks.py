import sys
from flask import request
import flask_api
from flask_api import status, exceptions
import pugsql

app = flask_api.FlaskAPI(__name__)
app.config.from_envvar("APP_CONFIG")

trackQueries = pugsql.module("queries/trackQueries/")
trackQueries.connect(app.config["DATABASE_URL"])

# def dict_factory(cursor, row):
    # d = {}
    # for idx, col in enumerate(cursor.description):
        # d[col[0]] = row[idx]
    # return d

@app.route('/api/v1/', methods=['GET'])
def home():
	return "<h1>Music Collection<h1><p>This site is a prototype API for your music collection.</p><p>This is the track handler.</p>"
    
@app.route("/api/v1/collections/songs/all", methods = ["GET"])
def allSongs():
    # dbConn = sqlite.connect("<INSERT DB FILENAME HERE>")
    # dbConn.row_factory = dict_factory
    # cursor = dbConn.cursor()
    # results = cursor.execute("SELECT * FROM <INSERT TABLE NAME HERE>")
    allTracks = trackQueries.all_tracks()
    return list(allTracks)

@app.route("/api/v1/collections/songs/<int:id>", methods = ["GET"])
def filterSongByID(id):
    return trackQueries.track_by_id(id=id)
    
@app.route("/api/v1/collections/songs/new", methods = ["POST"])
def createTrack():
    song = request.data
    requiredFields = ["title", "albumTitle", "artist", "length", "mediaURL"]
    
    if not all([field in song for field in requiredFields]):
        raise exceptions.ParseError()
    try:
        song['id'] = queries.create_track(**song)
    except Exception as e:
        return { 'error': str(e) }, status.HTTP_409_CONFLICT
        
    return song, status.HTTP_201_CREATED
    
@app.route("/api/v1/collections/songs/", methods = ["GET"])
def filterTracks():
    temp = request.args
    id = temp.get("id")
    title = temp.get("title")
    albumTitle = temp.get("albumTitle")
    
    query = "SELECT * FROM tracks WHERE"
    to_filter = []
    
    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if title:
        query += ' title=? AND'
        to_filter.append(title)
    if albumTitle:
        query += ' albumTitle=? AND'
        to_filter.append(albumTitle)
    if not (id or title or albumTitle):
        raise exceptions.NotFound()
        
    query = query[:-4] + ';'

    results = trackQueries._engine.execute(query, to_filter).fetchall()

    return list(map(dict, results))