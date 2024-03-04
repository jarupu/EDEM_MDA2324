import connexion
import six

from swagger_server.models.measure import Measure  # noqa: E501
from swagger_server import util


def get_last_meassure_by_sensor_sensor_get(sensor):  # noqa: E501
    """Get last temperature measurement by sensor ID

     # noqa: E501

    :param sensor: ID of the sensor
    :type sensor: str

    :rtype: Measure
    """
    return 'do some magic!'
