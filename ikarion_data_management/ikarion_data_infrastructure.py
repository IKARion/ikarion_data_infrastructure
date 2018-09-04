from flask import Flask
import flask_pymongo as fp
# Blueprints for the different APIs

app = Flask("db")

from ikarion_data_management.data_model_api import user_model_blueprint
from ikarion_data_management.data_model_api import group_model_blueprint
from ikarion_data_management.data_model_api import advanced_model_blueprint
from ikarion_data_management.log_aggregator import log_receiver_blueprint
from ikarion_data_management.data_access_layer.xapi_access_layer import xapi_access_endpoints
from ikarion_data_management.data_access_layer import modelDBConnection
from ikarion_data_management import config
import ikarion_data_management.data_access_layer.model_db_access_layer.user_model_dao as umd

#CONFIG = 'conf.ini'

# Register API endpoints
# Data Model API
app.register_blueprint(user_model_blueprint, url_prefix='/user_model')
# -->> TODO: implement endpoints and DAOs
app.register_blueprint(group_model_blueprint, url_prefix='/groups')
app.register_blueprint(advanced_model_blueprint, url_prefix='/advanced')

# Log receiver endpoint
app.register_blueprint(log_receiver_blueprint, url_prefix='/logs')

# xAPI access endpoint
app.register_blueprint(xapi_access_endpoints, url_prefix='/xapi')

# init
app.config.from_object(config.DevelopmentConfig)
modelDBConnection.init_app(app)


@app.route('/')
def hello_world():
    return 'IKARion data infrastructure running.'


if __name__ == '__main__':
    app.run(host="0.0.0.0")


# URL for latency calculation test:
# http://127.0.0.1:5000/groups/models/008/007/005