import sys
import flask_api
import pugsql
from flask import request, jsonify, Response
from flask_api import status, exceptions

app = flask_api.FlaskAPI(__name__)
app.config.from_envvar('APP_CONFIG')

queries = pugsql.module('queries/descriptionQueries/')
queries.connect(app.config['DATABASE_URL'])

def validContentType(request, type='application/json'):
    if request.headers.has_key('Content-Type'):
        if request.headers['Content-Type'] == type:
            return True
    return { 'Error':'Unsupported Media Type', 'Support-Content-Type':type}, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE

@app.route('/', methods=['GET'])
def home():
	return '''<h1>description-SERVICE</h1>'''

@app.route('/api/v1/descriptions/', methods=['POST'])
def description():
	if request.method=='POST':
		return create_description()

def create_description():
	description = request.data
	required_fields = ['descriptionDesc','trackTitle','userUserName']
	if not all([field in description for field in required_fields]):
		raise exceptions.ParseError()
	try:
		result= queries.track_media_url_by_title(**description)
		description['trackMediaURL'] = result['trackMediaURL']
		description['descriptionID'] = queries.create_description(**description)
	except Exception as e:
		return { 'Error': str(e) }, status.HTTP_409_CONFLICT
	return description, status.HTTP_201_CREATED



# @app.route('/api/v1/descriptions/', methods=['POST'])
# def description():
# 	if request.method=='POST':
# 		# valid = validContentType(request)
#     	# if valid is not True:
# 		# 	return valid
# 		return create_description()

# def create_description():
# 	description = request.data
# 	required_fields = ['descriptionDesc','trackTitle','userUserName']
# 	if not all([field in user for field in required_fields]):
#         raise exceptions.ParseError()
# 	try:
# 		description['trackMediaURL'] = queries.track_media_url_by_title(description['trackTitle'])
# 	except Exception as e:
#         return { 'Error': str(e) }, status.HTTP_409_CONFLICT
# 	return description, status.HTTP_201_CREATED