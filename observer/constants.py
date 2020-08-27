from os import environ
from uuid import uuid4

TZ = environ.get("TZ", "UTC")
ENV = environ.get("ENV", "")

EXPORTERS_PATH = environ.get("EXPORTERS_PATH", "/tmp/reports")
REMOTE_DRIVER_ADDRESS = environ.get("REMOTE_URL", "127.0.0.1:4444")
TOKEN = environ.get('token', "")

GALLOPER_URL = environ.get("GALLOPER_URL", "http://localhost")
GALLOPER_PROJECT_ID = int(environ.get("GALLOPER_PROJECT_ID", "1"))

REPORTS_BUCKET = environ.get("REPORTS_BUCKET", "reports")
TESTS_BUCKET = environ.get("TESTS_BUCKET", "tests")

RESULTS_BUCKET = environ.get("RESULTS_BUCKET", "")
RESULTS_REPORT_NAME = environ.get("RESULTS_REPORT_NAME", f'{uuid4()}')

JIRA_URL = environ.get("JIRA_URL", None)
JIRA_USER = environ.get("JIRA_USER", None)
JIRA_PASSWORD = environ.get("JIRA_PASSWORD", None)
JIRA_PROJECT = environ.get("JIRA_PROJECT", "")

ADO_ORGANIZATION = environ.get("ADO_ORGANIZATION", None)
ADO_PROJECT = environ.get("ADO_PROJECT", None)
ADO_TOKEN = environ.get("ADO_TOKEN", None)
ADO_TEAM = environ.get("ADO_TEAM", None)
