import subprocess

import unittest2
import os
import shutil

from tests.support import setup_installed_apps

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
TEST_ARENA_DIR = os.path.join(BASE_DIR, ".tests-arena")
DJANGO_TESTS_PROJECT_NAME = "DjangoEnvironmentTests"
DJANGO_TESTS_PROJECT_DIR = os.path.join(TEST_ARENA_DIR, DJANGO_TESTS_PROJECT_NAME)
DJANGO_TESTS_PROJECT_SETTINGS_DIR = os.path.join(DJANGO_TESTS_PROJECT_DIR, DJANGO_TESTS_PROJECT_NAME)
DJANGO_TESTS_PROJECT_SETTINGS_FILE_PATH = os.path.join(DJANGO_TESTS_PROJECT_SETTINGS_DIR, "settings.py")
DJANGO_TESTS_PROJECT_SETTINGS_PACKAGE_PATH = os.path.join(DJANGO_TESTS_PROJECT_SETTINGS_DIR, "settings")

ENVIRONMENT_SETTINGS_START_FILES = [
    "__init__.py",
    "common.py",
    "develop.py"
]


class StarEnvironmentTestCase(unittest2.TestCase):
    def __test_django_create__(self):
        self.assertTrue(os.path.exists(DJANGO_TESTS_PROJECT_DIR))

    def setUp(self):
        if os.path.exists(DJANGO_TESTS_PROJECT_DIR):
            shutil.rmtree(DJANGO_TESTS_PROJECT_DIR)
        elif not os.path.exists(TEST_ARENA_DIR):
            os.mkdir(TEST_ARENA_DIR)
        os.chdir(TEST_ARENA_DIR)
        os.system("django-admin startproject {project_name}".format(project_name=DJANGO_TESTS_PROJECT_NAME))

        setup_installed_apps(os.path.join(DJANGO_TESTS_PROJECT_DIR, DJANGO_TESTS_PROJECT_NAME))

        self.__test_django_create__()

    def test_structure(self):
        os.chdir(DJANGO_TESTS_PROJECT_DIR)
        os.system("python manage.py start-environments")
        self.assertFalse(os.path.exists(DJANGO_TESTS_PROJECT_SETTINGS_FILE_PATH))
        self.assertTrue(os.path.exists(DJANGO_TESTS_PROJECT_SETTINGS_PACKAGE_PATH))
        for file_name in ENVIRONMENT_SETTINGS_START_FILES:
            path = os.path.join(DJANGO_TESTS_PROJECT_SETTINGS_PACKAGE_PATH, file_name)
            self.assertTrue(os.path.exists(path))
