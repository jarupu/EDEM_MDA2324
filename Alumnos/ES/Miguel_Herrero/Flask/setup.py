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
    description="Swagger Industry Reyes&#x27;Robot - OpenAPI 3.0",
    author_email="apiteam@swagger.io",
    url="",
    keywords=["Swagger", "Swagger Industry Reyes&#x27;Robot - OpenAPI 3.0"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    Imagine que trabaja en una empresa industrial donde hay un robot. Tenemos un sensor que controla la temperatura del robot en tiempo real. La medición se guarda en una base de datos. Información del sensor;
    """
)
