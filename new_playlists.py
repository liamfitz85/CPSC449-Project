import sys
from flask import request
import flask_api
from flask_api import status, exceptions
import pugsql

app = flask_api.FlaskAPI(__name__)
app.config.from_envvar("APP_CONFIG")

playlistQueries = pugsql.module("queries/playlistQueries/")
playlistQueries.connect(app.config["DATABASE_URL"])

@app.route("/api/v1/", methods=["GET"])
def root():
	return """
		<h1>Music Collection</h1>
		<p>API website for your music collecton.</p>
	"""

@app.route("/api/v1/playlists/all", methods=["GET"])
def all_playlists():
	all_playlists = playlistQueries.all_playlists()
	return list(all_playlists)

@app.route("/api/v1/playlists", methods=["GET", "POST"])
def playlists():
	if request.method == "GET":
		return getPlaylists(request.args)
	elif request.method == "POST":
		return createPlaylist(request.args)

@app.route("/api/v1/playlists/<int:playID>", methods = ["GET"])
def playlistByID(playID):
	return playlistQueries.playlist_by_id(playID=playID)

def createPlaylist(playlist):
	playlist = request.data	
	requiredFields = ["playTitle","playUser"]
	
	if not all([field in playlist for field in requiredFields]):
		raise exceptions.ParseError()
	try:
		playlist['id'] = playlistQueries.create_playlist(**playlist)
	except Exception as e:
		return { 'error' : str(e) }, status.HTTP_409_CONFLICT
	
	return playlist, status.HTTP_201_CREATED

def getPlaylists(queryParams):
	playID = queryParams.get("playID")
	playTitle = queryParams.get("playTitle")
	playUser = queryParams.get("playUser")

	query = "SELECT * FROM playlists WHERE"

	filtered_playlists = []

	if playID:
		query += " playID=? AND"
		filtered_playlists.append(playID)
	if playTitle:
		query += " playTitle=? AND"
		filtered_playlists.append(playTitle)
	if playUser:
		query += " playUser = (SELECT users.userID FROM users WHERE users.name=?) AND"
		filtered_playlists.append(playUser)
	if not (playID or playTitle or playUser):
		raise exceptions.NotFound()

	query = query[:-4] + ";"
	results = playlistQueries._engine.execute(query, filtered_playlists).fetchall()

	return list(map(dict, results))