from flask import Blueprint, jsonify
from ..data_access_layer.model_db_access_layer import advanced_model_dao

advanced_model_endpoints = Blueprint('advanced_model_endpoints', __name__)

@advanced_model_endpoints.route('/about')
def about():
    return 'Advanced model endpoints.'