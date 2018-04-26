from flask import Blueprint, jsonify
from ..data_access_layer.model_db_access_layer import advanced_model_dao

advanced_model_blueprint = Blueprint('advanced_model_blueprint', __name__)

@advanced_model_blueprint.route('/about')
def about():
    return 'Advanced model endpoints.'