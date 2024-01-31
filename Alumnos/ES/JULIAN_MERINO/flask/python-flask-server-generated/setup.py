# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="The Ultimate Robot Temperature Listener for EDEM - TURTLE 1.0",
    author_email="",
    url="",
    keywords=["Swagger", "The Ultimate Robot Temperature Listener for EDEM - TURTLE 1.0"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
     My very unique robot temperature sensor reader server for EDEM. This work is a deliverable by Julián Merino for the Master in Big Data &amp; Cloud. Documentation done with Swagger, based on the PetStore:  [EDEM](https://edem.eu/master-big-data-analytics/)
    """
)
