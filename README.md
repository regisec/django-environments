# Django Environments

*_In development_

---
[![Build Status](https://travis-ci.org/regisec/django-environments.svg?branch=develop)](https://travis-ci.org/regisec/django-environments)
[![codecov.io](https://codecov.io/github/regisec/django-environments/coverage.svg?branch=develop)](https://codecov.io/github/regisec/django-environments?branch=develop)

Django Environments is a powerful and smarter environment manager for django projects.

## Requirements
- Django: 1.8 or 1.9
- Python: 2.7, 3.4, 3.5

## Instalation
To install the **Django Environments** you can use `pip` as bellow

    pip install django-environments

Then add `'django_environments'` in your `INSTALLED_APPS` settings

    INSTALLED_APPS = (
        ...,
        'django_environments',
    )

## Starting
To start the **Django Environments** on you django project run the following command

    python manage.py start-environments

Then your `settings.py` file will be replaced by a settings package.

## Create an environment
To create a new environment run the following command

    python manage.py create-environment <NAME>

Then a new environment will appear in settings package as `<NAME>.py`

## Switch current environment
To switch the project to another environment run the command

    python manage.py switch-environment <NAME>
