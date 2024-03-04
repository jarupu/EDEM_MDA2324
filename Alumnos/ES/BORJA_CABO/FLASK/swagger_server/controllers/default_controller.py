import connexion
import six

from swagger_server.models.robot import Robot  # noqa: E501
from swagger_server import util


def get_last_measure_by_sensor_get(sensor):  # noqa: E501
    """get_last_measure_by_sensor_get

     # noqa: E501

    :param sensor: ID del sensor
    :type sensor: float

    :rtype: Robot
    """
    return 'do some magic!'