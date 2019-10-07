import sys
import flask_api
from flask import request
from flask_api import status, exceptions
import pugsql


app = flask_api.FlaskAPI(__name__)
app.config.from_envvar('APP_CONFIG')

queries = pugsql.module('queries/userQueries')
queries.connect(app.config['DATABASE_URL'])

@app.route('/', methods=['GET'])
def home():
    return '''<h1>USER-SERVICE</h1>'''

@app.route('/api/v1/user/register', methods=['POST', 'GET'])
def register():
    if request.method=='POST':
        if request.headers.has_key('Content-Type'):
            if request.headers['Content-Type'] == 'application/json':
                return create_user()
    elif request.method=='GET':
        all_users=queries.all_users()
        return list(all_users)

def create_user():
    user = request.data
    required_fields = ['userFirstName','userLastName','userMiddleName','userEmail','userBD', 'userPassword']
    if not all([field in user for field in required_fields]):
        raise exceptions.ParseError()
    try:
        user['id'] = queries.create_user(**user)
    except Exception as e:
        return { 'error': str(e) }, status.HTTP_409_CONFLICT
    return user, status.HTTP_201_CREATED
       



