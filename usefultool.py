import sys
import flask_api
from flask import request, jsonify , Response
from flask_api import status, exceptions
import pugsql

def jasonifier(data, status_code=200, mimetype='application/json'):
    js = jsonify(data)  
    js.status_code = status_code
    js.mimetype = mimetype
    return js