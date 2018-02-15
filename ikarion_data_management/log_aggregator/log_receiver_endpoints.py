from flask import Blueprint
from ..data_access_layer.model_db_access_layer import user_model_dao
#from ..data_access_layer.model_db_access_layer import group_model_dao
from flask import request
log_receiver_endpoints = Blueprint('log_receiver_endpoints', __name__)


@log_receiver_endpoints.route('/about')
def about():
    return 'Log receiver endpoints.'

# The LRS fowards resource access logs to this endpoint.
# Log forwarding has to be specified in learning locker first.
# (See https://ht2ltd.zendesk.com/hc/en-us/articles/115002026451--NEW-LL-Statement-Forwarding)
@log_receiver_endpoints.route('/resource_access')
def processResourceAccessLog():

    None
    # TODO: Process log
    # get user
    # get user group if present
    # get resource type
    # ...
    #try:
        #user_model_dao.getUserModel(user, course)
    #except user_model_dao.NoSuchCourseException:
        # create new user model
        #user_model_dao.updateOrInsertUserModel(model)

    # increment number of resources used
    #user_model_dao.updateUserModelIncrementField(user, course, field=user_model_dao.RES_USED_FIELD, 1)

    # increment number of different resources used
    #user_model_dao.updateUserModelIncrementField(user, course, field=user_model_dao.DISTINCT_RES_USED_FIELD, ???)