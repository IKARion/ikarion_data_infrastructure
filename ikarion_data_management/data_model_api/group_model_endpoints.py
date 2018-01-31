from flask import Blueprint, jsonify
from ..data_access_layer.model_db_access_layer import group_model_dao

group_model_endpoints = Blueprint('group_model_endpoints', __name__)

@group_model_endpoints.route('/about')
def about():
    return 'Group model endpoints.'