# -*- coding: utf-8 -*-

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-classnames-tag',
    version='0.1',
    include_package_data=True,
    packages=['django_classnames_tag'],
    url='http://github.com/sebslomski/django-classnames-tag',
    license='BSD',
    description='Django classnames template tag',
    long_description=README,
    author='Sebastian Slomski',
    author_email='me@sebslomski.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    zip_safe=False,
)
