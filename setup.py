# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
from os import path

from django_environments import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='django-environments',
        version=__version__,
        description='Smart environment controller for Django',
        long_description=long_description,
        url='http://www.django-environments.org/',
        author='Régis Eduardo Crestani',
        author_email='regis.crestani@gmail.com',
        license='BSD',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Framework :: Django',
            'Topic :: Software Development :: Utilities',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
        ],
        packages=find_packages(exclude=['docs', 'test']),
        install_requires=[],
)
