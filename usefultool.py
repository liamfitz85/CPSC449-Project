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

def validContentType(request, type='application/json'):
    if request.headers.has_key('Content-Type'):
        if request.headers['Content-Type'] == type:
            return True
    return jasonifier({ 'Error':'Unsupported Media Type', 'Support-Content-Type':type}, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)