from flask import Blueprint
from flask import request

"""
Accesss Learning Record Store.
Forward Queries
"""

xapi_access_endpoints = Blueprint('xapi_access_endpoints', __name__)

@xapi_access_endpoints.route("/about")
def about():
    return "xapi endpoint"

@xapi_access_endpoints.route("/statements")
def process_statement():
    xapi_json = request.get_json(force=True)
