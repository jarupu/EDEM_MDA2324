import connexion
import six

from swagger_server.models.medicin import Medicin  # noqa: E501
from swagger_server import util


def get_last_meassure_by_sensor_sensor_get(sensor):  # noqa: E501
    """Obten la última medición de temperatura por el Sensor ID

    Devuelve la última medición guardada de temperatura indicado por el Sensor ID # noqa: E501

    :param sensor: ID del sensor
    :type sensor: str

    :rtype: Medicin
    """
    return 'do some magic!'
