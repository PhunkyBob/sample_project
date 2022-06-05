# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample_project',
    version='0.1.0',
    description='Sample project for Python 3.8',
    long_description=readme,
    author='Nicolas MARTIN',
    author_email='PhunkyBob@noreply.github.com',
    url='https://github.com/PhunkyBob/sample_project',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

