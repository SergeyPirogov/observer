import os

from observer.app import create_parser, execute
from observer.reporters.azure_devops import AdoClient
from observer.reporters.jira_reporter import JiraClient

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def test_main_with_data_params():
    args = create_parser().parse_args(
        [
            # "-f", f"data.zip",
            # "-d", f"{ROOT_DIR}/data/data.json",
            "-sc", "/tmp/data/webmail.side",
            "-g", "False",
            "-v", "False",
            # "-r", "ado",
            "-l", "1",
            "-b", "chrome",
            "-a", "max"
        ])
    execute(args)
