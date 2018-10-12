from flask import Blueprint, jsonify
from ..data_access_layer.management_access_layer import management_dao
from .util import fix_url_chars

data_management_blueprint = Blueprint('data_management_blueprint', __name__)

@data_management_blueprint.route('/about')
def about():
    return 'Data management endpoints.'

@data_management_blueprint.route('/add_r_script/<string:description>/<int:interval>/<string:uri>')
def addScheduledRscript(uri, interval, description):

    return(jsonify(
        management_dao.addScheduledScript(fix_url_chars(uri), interval, fix_url_chars(description),
                                          management_dao.scriptTypes['R'])
    ))
    #TODO: Handle exception

@data_management_blueprint.route('/add_python_script/<string:description>/<int:interval>/<path:uri>')
def addScheduledPythonscript(uri, interval, description):
    return jsonify(
        management_dao.addScheduledScript(fix_url_chars(uri), interval, fix_url_chars(description),
                                          management_dao.scriptTypes['PYTHON'])
    )
    # TODO: Handle exception

@data_management_blueprint.route('/add_awb_wf/<string:description>/<int:interval>/<path:uri>')
def addScheduledAWBworkflow(uri, interval, description):
    return jsonify(
        management_dao.addScheduledScript(fix_url_chars(uri), interval, fix_url_chars(description),
        management_dao.scriptTypes['AWB'])
    )
    # TODO: Handle exception

@data_management_blueprint.route('/jobs')
def getCurrentJobs():
    return jsonify(
        management_dao.getCurrentJobs()
    )

@data_management_blueprint.route('/jobs/remove/<id>')
def removeJob(id):
    return jsonify(
        management_dao.removeJob(id)
    )
    # TODO: Handle exception

@data_management_blueprint.route('/jobs/pause/<id>')
def pauseJob(id):
    return jsonify(
        management_dao.pauseJob(id)
    )
    # TODO: Handle exception

@data_management_blueprint.route('/jobs/resume/<id>')
def resumeJob(id):
    return jsonify(
        management_dao.resumeJob(id)
    )
    # TODO: Handle exception