# TODO: Migrate templates to files

TEMPLATE__INIT__ = """
\"""
Django Environments {VERSION}
\"""
from .common import *

try:
    from .__load__ import *
    print("Using %s environment" % ENVIRONMENT_NAME)
    if len(ENVIRONMENT_VERSION_CODE) > 0:
        VERSION += "." + ENVIRONMENT_VERSION_CODE
except ImportError:
    print("Environment starting fail!")
    print("Set the DEVELOP environment running: \\"python manage.py set-environment develop\\"")
"""

TEMPLATE_ENVIRONMENT = """
\"""
Django Environments {VERSION}

All settings here will override another ones
\"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ENVIRONMENT_NAME = "{ENVIRONMENT_NAME}"
ENVIRONMENT_VERSION_CODE = "{ENVIRONMENT_VERSION_CODE}"

"""


def process_template(template, output_path, **kwargs):
    with open(output_path, "w+") as file:
        file.write(template.format(**kwargs))


def process_init_template(output_path, **kwargs):
    process_template(TEMPLATE__INIT__, output_path, **kwargs)


def process_environment_template(output_path, **kwargs):
    process_template(TEMPLATE_ENVIRONMENT, output_path, **kwargs)
