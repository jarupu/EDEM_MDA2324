import connexion
import six

from swagger_server.models.medicion import Medicion  # noqa: E501
from swagger_server import util


def get_last_measure_by_sensor(sensorId):  # noqa: E501
    """Obtiene la última medición registrada por un sensor específico.

    Retorna la última medición de temperatura realizada por el sensor identificado por &#x60;sensorId&#x60;. # noqa: E501

    :param sensorId: El identificador único del sensor.
    :type sensorId: str

    :rtype: Medicion
    """
    return 'do some magic!'
