import flask_api
from flask import request
from flask_api import status, exceptions

app = flask_api.FlaskAPI(__name__)
app.config.from_envvar('APP_CONFIG')

@app.route('/', methods=['GET'])
def home():
	db_path = app.config['DATABASE_URL']
	add = app.config['TEST_STRING_DESC']
	return str(db_path + "<br>" + add)
