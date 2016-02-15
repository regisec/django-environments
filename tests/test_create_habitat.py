import os
import shutil

import unittest2

from tests.support import setup_installed_apps

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
TEST_ARENA_DIR = os.path.join(BASE_DIR, ".tests-arena")
DJANGO_TESTS_PROJECT_NAME = "DjangoEnvironmentTests"

DJANGO_TESTS_PROJECT_DIR = os.path.join(TEST_ARENA_DIR, DJANGO_TESTS_PROJECT_NAME)
DJANGO_TESTS_PROJECT_SETTINGS_DIR = os.path.join(DJANGO_TESTS_PROJECT_DIR, DJANGO_TESTS_PROJECT_NAME)
DJANGO_TESTS_PROJECT_SETTINGS_PACKAGE_PATH = os.path.join(DJANGO_TESTS_PROJECT_SETTINGS_DIR, "settings")
DJANGO_TESTS_PROJECT_ENVIRONMENT_FILE_PATH = os.path.join(DJANGO_TESTS_PROJECT_SETTINGS_PACKAGE_PATH, "production.py")


class CreateEnvironmentTestCase(unittest2.TestCase):
    def setUp(self):
        os.chdir(BASE_DIR)
        if os.path.exists(DJANGO_TESTS_PROJECT_DIR):
            shutil.rmtree(DJANGO_TESTS_PROJECT_DIR)
        elif not os.path.exists(TEST_ARENA_DIR):
            os.mkdir(TEST_ARENA_DIR)
        os.chdir(TEST_ARENA_DIR)
        os.system("django-admin startproject {project_name}".format(project_name=DJANGO_TESTS_PROJECT_NAME))
        setup_installed_apps(os.path.join(DJANGO_TESTS_PROJECT_DIR, DJANGO_TESTS_PROJECT_NAME))
        os.chdir(DJANGO_TESTS_PROJECT_DIR)
        os.system("python manage.py start-habitat")

    def tearDown(self):
        os.chdir(BASE_DIR)
        shutil.rmtree(TEST_ARENA_DIR)

    def test_happy_path(self):
        os.chdir(DJANGO_TESTS_PROJECT_DIR)
        os.system("python manage.py create-habitat production")
        self.assertTrue(os.path.exists(DJANGO_TESTS_PROJECT_ENVIRONMENT_FILE_PATH))
