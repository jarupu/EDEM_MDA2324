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
    description="Robot Temperature Monitoring API",
    author_email="apiteam@swagger.io",
    url="",
    keywords=["Swagger", "Robot Temperature Monitoring API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    # Evaluation Exercise - Create your first API using swagger Imagine that you work for an industry company where there is a robot.  We have a sensor that is monitoring the temperature of the robot in real-time. The measurement is saved into a database. Sensor Info: - id del sensor - string - fechamuestreo - string - unidad - string - medicion - number  Our API needs to provide the following methods: &gt; /getLastMeasureBySensor/{sensor}:   sensor -&gt; string    When the method is successful, it should return: Measure - code (id del sensor) - string - fechamuestreo - string - unidad - string - medicion - number  When the method is not successful, it should return: 404 -&gt; Invalid ID supplied 400 -&gt; Sensor not found
    """
)
