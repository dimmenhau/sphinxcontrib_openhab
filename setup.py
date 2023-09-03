# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='PythonProjectTemplate',
    version='0.1.0',
    description='Python Project Template for new Projects',
    long_description=readme,
    author='Dietmar Immenhausen',
    author_email='dietmar@familie-immenhausen.de',
    url='https://github.com/dimmenhau/python_project_template',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

