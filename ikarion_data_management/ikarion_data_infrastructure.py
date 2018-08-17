from flask import Flask
import flask_pymongo as fp
# Blueprints for the different APIs

app = Flask("db")

from ikarion_data_management.data_model_api import user_model_blueprint
from ikarion_data_management.data_model_api import group_model_blueprint
from ikarion_data_management.data_model_api import advanced_model_blueprint
from ikarion_data_management.log_aggregator import log_receiver_blueprint
from ikarion_data_management.data_access_layer.xapi_access_layer import xapi_access_endpoints
from flask import request
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

# init DB
#TODO: Configurable initialisation (development, production) with different DBs. (See http://flask.pocoo.org/docs/0.12/patterns/appfactories/)
#app.config_from_pyfile(CONFIG)

#app.config['MONGO_DBNAME'] = "test"
#app.config['MONGO_USERNAME'] = "ikarion"
#app.config['MONGO_PASSWORD'] = "ikariondb"
MONGO_URI = "mongodb://ikarion:ikariondb@cluster0-shard-00-00-n3pml.mongodb.net:27017,cluster0-shard-00-01-n3pml.mongodb.net:27017,cluster0-shard-00-02-n3pml.mongodb.net:27017/db2?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin"
app.config['MONGO_URI'] = MONGO_URI
# app.config['MONGO2_DBNAME'] = "db"
from ikarion_data_management.data_access_layer import modelDBConnection
modelDBConnection.init_app(app)


# db_connection = fp.PyMongo(app, config_prefix="MONGO2")

# umd.con = db_connection

@app.route('/')
def hello_world():
    return 'IKARion data infrastructure running.'


if __name__ == '__main__':
    print("***4")
    app.run(host="0.0.0.0")
    print(request.u)


# URL for latency calculation test:
# OLD: http://127.0.0.1:5000/groups/models/008/007/005

# http://0.0.0.0:5000/user_model/groups_for_course/7
#http://0.0.0.0:5000/user_model/
# http://descartes.inf.uni-due.de:5000/user_model/

# http://0.0.0.0:5000/user_model/courses
# http://descartes.inf.uni-due.de:5000/user_model/courses