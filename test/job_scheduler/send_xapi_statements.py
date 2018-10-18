import test.job_scheduler.xapi_statements as xs
import requests

LOG_PRE = "/logs"

xapi_statement = xs.triggering_statement
# xapi_statement = xs.non_trigger_statment

requests.get("http://localhost:5000"+LOG_PRE+"/log_forwarding",
             json=xapi_statement)

