from selene.support.shared import SharedBrowser
from selenium import webdriver
from selenium.webdriver.webkitgtk.options import Options

from observer.constants import REMOTE_DRIVER_ADDRESS, RESULTS_REPORT_NAME, RESULTS_BUCKET, ENV, TZ, GALLOPER_PROJECT_ID, \
    BROWSER_VERSION, GALLOPER_URL, TOKEN, OBSERVER_USER, OBSERVER_PASSWORD, JOB_NAME, ENABLE_VNC, JIRA_URL, \
    JIRA_PROJECT, JIRA_USER, JIRA_PASSWORD, ADO_PROJECT, ADO_ORGANIZATION, ADO_TOKEN, ADO_TEAM
from observer.util import get_browser_version

browser = None
cfg = None
exec_args = None


def get_driver():
    global browser
    if browser is None:
        browser_name, version = get_browser_version(exec_args.browser)
        options = get_browser_options(browser_name, version, exec_args)

        driver = webdriver.Remote(
            command_executor=f'http://{OBSERVER_USER}:{OBSERVER_PASSWORD}@{REMOTE_DRIVER_ADDRESS}/wd/hub',
            options=options)

        cfg.browser_name = browser_name
        cfg.driver = driver
        driver.set_window_position(0, 0)
        browser = SharedBrowser(cfg)
    return browser


def get_browser_options(browser_name, version, args):
    options = Options()

    if "chrome" == browser_name:
        options = webdriver.ChromeOptions()

    if "firefox" == browser_name:
        options = webdriver.FirefoxOptions()

    if options.capabilities.get("browserName") == 'MiniBrowser':
        raise Exception(f"Unsupported browser {browser_name}")

    if 'junit' in args.report:
        options.set_capability("junit_report", RESULTS_REPORT_NAME)
        options.set_capability("junit_report_bucket", RESULTS_BUCKET)

    if 'jira' in args.report:
        options.set_capability("jira_url", JIRA_URL)
        options.set_capability("jira_project", JIRA_PROJECT)
        options.set_capability("jira_user", JIRA_USER)
        options.set_capability("jira_password", JIRA_PASSWORD)

    if 'ado' in args.report:
        options.set_capability("ado_organization", ADO_ORGANIZATION)
        options.set_capability("ado_project", ADO_PROJECT)
        options.set_capability("ado_token", ADO_TOKEN)
        options.set_capability("ado_team", ADO_TEAM)

    if 'email' in args.report:
        options.set_capability("email_report", True)

    if BROWSER_VERSION:
        version = BROWSER_VERSION

    options.set_capability("test_id", args.test_id)
    options.set_capability("version", version)
    options.set_capability("venv", ENV)
    options.set_capability('tz', TZ)
    options.set_capability('galloper_project_id', GALLOPER_PROJECT_ID)
    options.set_capability('galloper_url', GALLOPER_URL)
    options.set_capability('galloper_token', TOKEN)
    options.set_capability('aggregation', args.aggregation)
    options.set_capability('job_name', JOB_NAME)
    options.set_capability("vnc", ENABLE_VNC)
    return options


def close_driver():
    global browser
    if browser:
        browser.quit()
        browser = None


def set_config(config):
    global cfg
    cfg = config


def set_args(args):
    global exec_args
    exec_args = args
