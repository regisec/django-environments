# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
from os import path

from django_environments import __version__

here = path.abspath(path.dirname(__file__))

setup(
        name='django-environments',
        version=__version__,
        description='A powerful and smarter environment manager for django projects',
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
