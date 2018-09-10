import subprocess
import os.path
import hashlib
from . import scheduler
from . import scriptConf

scriptTypes = {
    'R':'rscript',
    'PYTHON':'python',
    'AWB':'awb'
}

def scheduledRscript(uri):
    print("EXECUTE: " + uri)
    subprocess.call([scriptConf['RSCRIPT'], uri])

def scheduledAWBworkflow(uri):
# TODO: Implement auto execution of Analytics Workbench workflows
    raise NoScriptHandlerException('Analytics Workbench')

def schedultedPythonScript(uri):
    subprocess.call(['python', uri])

def addScheduledScript(uri, interval, description='none', type='rscript'):

    handlers = {
        'rscript': scheduledRscript,
        'python': schedultedPythonScript,
        'awb': scheduledAWBworkflow
    }

    if not os.path.exists(uri):
        raise ScriptNotFoundException(uri)

    handler = handlers.get(type, None)

    if handler is None:
        raise NoScriptHandlerException(type)

    uriHash = hashlib.md5(uri.encode('utf-8'))

    scheduler.add_job(uriHash.hexdigest(), handler, args=[uri], name=description, trigger='interval', minutes=interval)

    return getCurrentJobs()

def getCurrentJobs():

    return list(map(
        lambda job: {
            'id': job.id,
            'name': job.name,
            'next_run': job.next_run_time,
            'trigger': type(job.trigger).__name__,
        }, scheduler.get_jobs())
    )

def removeJob(jobId):
    scheduler.remove_job(jobId)
    return getCurrentJobs()

def pauseJob(jobId):
    scheduler.pause_job(jobId)
    return getCurrentJobs()

def resumeJob(jobId):
    scheduler.resume_job(jobId)
    return getCurrentJobs()

# Exception classes
class ScriptNotFoundException(Exception):
    def __init__(self, uri):
        self.message = "Script {} does not exist.".format(uri)

# Exception classes
class NoScriptHandlerException(Exception):
    def __init__(self, type):
        self.message = "No handler for given script type {} implemented.".format(type)
