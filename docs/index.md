# Django Habitat

*_In development_

---
[![Build Status](https://travis-ci.org/regisec/django-habitat.svg?branch=develop)](https://travis-ci.org/regisec/django-habitat)
[![codecov.io](https://codecov.io/github/regisec/django-habitat/coverage.svg?branch=develop)](https://codecov.io/github/regisec/django-habitat?branch=develop)

Django Habitat is a powerful and smarter environment manager for django projects.

## Requirements
- Django: 1.8 or 1.9
- Python: 2.7, 3.4, 3.5

## Instalation
To install the **Django Habitat** you can use `pip` as bellow

    pip install django-habitat

Then add `'django_habitat'` in your `INSTALLED_APPS` settings

    INSTALLED_APPS = (
        ...,
        'django_habitat',
    )

## Starting
To start the **Django Habitat** on you django project run the following command

    python manage.py start-habitat

Then your `settings.py` file will be replaced by a settings package.

## Create an environment
To create a new environment run the following command

    python manage.py create-habitat <NAME>

Then a new environment will appear in settings package as `<NAME>.py`

## Switch current environment
To switch the project to another environment run the command

    python manage.py switch-habitat <NAME>
