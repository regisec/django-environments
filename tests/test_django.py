import unittest2
import os
import shutil

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
TEST_ARENA_DIR = os.path.join(BASE_DIR, ".tests-arena")
DJANGO_TESTS_PROJECT_NAME = "DjangoEnvironmentTests"
DJANGO_TESTS_PROJECT_DIR = os.path.join(TEST_ARENA_DIR, DJANGO_TESTS_PROJECT_NAME)

# from django.core.management import call_command


class TestDjango(unittest2.TestCase):
    def setUp(self):
        if not os.path.exists(TEST_ARENA_DIR):
            os.mkdir(TEST_ARENA_DIR)
        os.chdir(TEST_ARENA_DIR)
        os.system("django-admin startproject {project_name}".format(project_name=DJANGO_TESTS_PROJECT_NAME))

    def tearDown(self):
        shutil.rmtree(DJANGO_TESTS_PROJECT_DIR)

    def test_django_create(self):
        self.assertTrue(os.path.exists(DJANGO_TESTS_PROJECT_DIR))
