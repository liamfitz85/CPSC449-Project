import sys
import flask_api
import pugsql
from usefultool import jasonifier, validContentType
from flask import request, jsonify, Response
from flask_api import status, exceptions
from werkzeug.security import generate_password_hash

app = flask_api.FlaskAPI(__name__)
app.config.from_envvar('APP_CONFIG')

queries = pugsql.module('queries/userQueries')
queries.connect(app.config['DATABASE_URL'])

@app.route('/', methods=['GET'])
def home():
    return '''<h1>USER-SERVICE</h1>'''

@app.route('/api/v1/users/register', methods=['POST', 'GET'])
def register():
    valid = validContentType(request)
    if valid is not True:
        return valid
    if request.method=='GET':
        all_users=queries.all_users()
        data = list(all_users)
        return jasonifier(data)
    elif request.method=='POST':
        return create_user()

def create_user():
    user = request.data
    required_fields = ['userName','userUserName','userEmail','userPassword']
    if not all([field in user for field in required_fields]):
        raise exceptions.ParseError()
    try:
        user['userPassword'] = generate_password_hash(user['userPassword'])
        user['id'] = queries.create_user(**user)
    except Exception as e:
        return jasonifier({ 'Error': str(e) }, status.HTTP_409_CONFLICT)
    return jasonifier(user, status.HTTP_201_CREATED)


@app.route('/api/v1/users/<int:id>', methods=['DELETE', 'GET'])
def user(id):
    valid = validContentType(request)
    if valid is not True:
        return valid
    if request.method=='GET':
        return get_user(id)
    elif request.method=='DELETE':
        return delete_user(id)
        
def get_user(id):
    try:
        user = queries.user_by_id(id=id)
        if user:
            return jasonifier(user)
        else:
            raise exceptions.ParseError()
    except Exception as e:
        return jasonifier({ 'Error': str(e) }, status.HTTP_409_CONFLICT)  

def delete_user(id):
    try:
        affected = queries.user_delete_by_id(id=id)
        if affected == 0:
            return jasonifier({ 'Error': "USER NOT FOUND" },status.HTTP_404_NOT_FOUND)
        else:
            return jasonifier({ 'DELETE REQUEST ACCEPTED': str(id) }, status.HTTP_202_ACCEPTED)               
    except Exception as e:
        return { 'error': str(e) }, status.HTTP_409_CONFLICT 
