#####################################################
#TODO                                                                                                       #
#STILL NEED TO CREATE AN EDIT AND DELETE FUNCTION#
####################################################

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
    allTracks = trackQueries.all_tracks()
    return list(allTracks)

@app.route("/api/v1/collections/songs/<int:trackID>", methods = ["GET"])
def filterSongByID(trackID):
    return trackQueries.track_by_id(trackID=trackID)
    
@app.route('/api/v1/collections/songs', methods=['GET', 'POST'])
def songs():
    if request.method == 'GET':
        return filterTracks(request.args)
    elif request.method == 'POST':
        return createTrack(request.data)
    
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
    id = queryParams.get("id")
    title = queryParams.get("title")
    albumTitle = queryParams.get("albumTitle")
    
    query = "SELECT * FROM tracks WHERE"
    to_filter = []
    
    if id:
        query += ' trackID=? AND'
        to_filter.append(id)
    if title:
        query += ' trackTitle=? AND'
        to_filter.append(title)
    if albumTitle:
        query += ' trackAlbum=? AND'
        to_filter.append(albumTitle)
    if not (id or title or albumTitle):
        raise exceptions.NotFound()
        
    query = query[:-4] + ';'

    results = trackQueries._engine.execute(query, to_filter).fetchall()

    return list(map(dict, results))