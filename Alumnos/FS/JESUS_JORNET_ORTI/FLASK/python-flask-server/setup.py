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
    description="API de Monitoreo de Temperatura del Robot",
    author_email="soporte@tuempresa.com",
    url="",
    keywords=["Swagger", "API de Monitoreo de Temperatura del Robot"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    Esta API permite monitorear la temperatura de un robot en tiempo real, proporcionando acceso a las mediciones de temperatura guardadas en la base de datos.
    """
)

