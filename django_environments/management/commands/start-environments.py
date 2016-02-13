from django.core.management.base import BaseCommand
import os
import shutil

from django_environments import __version__

from django_environments.exceptions import IncompatibleSettings
from django_environments.templates import TEMPLATE__INIT__, TEMPLATE_ENVIRONMENT


def __process_template__(template, des):
    replaces = {
        "VERSION": __version__,
        "ENVIRONMENT_NAME": "Develop",
        "ENVIRONMENT_VERSION_CODE": "dev",
    }
    with open(des, "w+") as des_file:
        des_file.write(template.format(**replaces))


def __django_settings_path__(base_dir):
    """
    Find the settings dir inside the django project
    :param base_dir: django's project root dir
    :return: settings dir PATH, settings file name
    """
    django_settings = os.environ.get("DJANGO_SETTINGS_MODULE")
    settings_values = django_settings.split(".")
    settings_file_name = "{file_name}.py".format(file_name=settings_values.pop(-1))
    settings_dir_path = os.path.join(*([base_dir] + settings_values))
    return settings_dir_path, settings_file_name


def __setup_common__(settings_file_path, settings_package_path):
    path = os.path.join(settings_package_path, "common.py")
    shutil.move(settings_file_path, path)
    with open(path, "a") as f:
        # TODO: SEARCH ANOTHER VERSION FIRST
        f.write("\nVERSION = \"0.0.0\"\n")


def __create_settings_package__(settings_dir_path, settings_file_name):
    settings_file_path = os.path.join(settings_dir_path, settings_file_name)
    if not os.path.exists(settings_file_path):
        raise IncompatibleSettings("Django settings file not found. (%s)" % settings_file_path)
    if not os.path.isfile(settings_file_path):
        raise IncompatibleSettings("Django settings is not a file. (%s)" % settings_file_path)
    settings_package_path = os.path.join(settings_dir_path, "settings")
    if os.path.exists(settings_package_path):
        raise IncompatibleSettings("Django environments settings package already exists.\n" + settings_package_path)

    os.mkdir(settings_package_path)
    __setup_common__(settings_file_path, settings_package_path)
    __process_template__(TEMPLATE__INIT__, os.path.join(settings_package_path, "__init__.py"))
    __process_template__(TEMPLATE_ENVIRONMENT, os.path.join(settings_package_path, "develop.py"))
    return settings_package_path


class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
        from django.conf import settings
        settings_dir_path, settings_file_name = __django_settings_path__(settings.BASE_DIR)
        settings_package_path = __create_settings_package__(settings_dir_path, settings_file_name)
