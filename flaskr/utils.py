import os, random
from flask import request, abort

def validate_request_args(requiredFields):
    for field in requiredFields:
        if field not in request.args:
            abort(400, description=field + " is a required field")

def validate_request_form(requiredFields):
    for field in requiredFields:
        if field not in request.form:
            abort(400, description=field + " is a required field")