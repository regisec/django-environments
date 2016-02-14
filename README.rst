# Django Environments

*_In development_

---
[![build-status-image]][travis]

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

_`--ignore-develop` to ignore the develop environment creation_

Then your `settings.py` file will be replaced by a settings package where a _develop_ environment will be created as default.

## Create an environment
To create a new environment run the following command

    python manage.py create-environment <NAME>

Then a new environment will appear in settings package as `<NAME>.py`

## Switch current environment
To switch the project to another environment run the command

    python manage.py switch-environment <NAME>



[build-status-image]: https://secure.travis-ci.org/regisec/django-environments.svg?branch=develop
[travis]: http://travis-ci.org/regisec/django-environments?branch=develop
