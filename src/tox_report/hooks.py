"""Tox hook implementations."""
import io
import os

from rich.console import Console
from tox import hookimpl

console = Console(record=True, file=io.StringIO())
console.print("Recording started", style="bold red")


@hookimpl
def tox_configure(config):
    """Configure hook."""
    console.print("Reporting mode enabled", style="bold red")


@hookimpl
def tox_runtest_post(venv):
    """runtest hook."""
    collect_data(venv)


@hookimpl
def tox_cleanup(session):
    """cleanup hook."""
    console.print("Recording stopped", style="bold red")

    html = console.export_html(inline_styles=True)
    with open("report.html", "w") as report_handler:
        report_handler.write(html)
        print("Report generated to %s" % os.path.abspath(report_handler.name))


def collect_data(current_venv):
    """Record data for the report."""
    # data = {}
    # data[current_venv.name] = {
    #     "name": current_venv.name,
    #     "path": current_venv.path.strpath,
    # }
    # data[current_venv.name].update(current_venv.env_log.reportlog.dict)
    console.print(current_venv.env_log.reportlog.dict)

    # data[current_venv.name].pop("testenvs", None)
    # data[current_venv.name].update(
    #     current_venv.env_log.reportlog.dict["testenvs"][current_venv.name])
    # return data
