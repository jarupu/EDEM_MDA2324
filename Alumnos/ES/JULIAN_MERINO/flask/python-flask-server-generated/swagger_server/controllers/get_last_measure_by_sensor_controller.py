import connexion
import six

from swagger_server.models.measure import Measure  # noqa: E501
from swagger_server import util


def get_temp(sensor):  # noqa: E501
    """Obtains ID, date, unit, and temperature measurement, and returns Measure (200) or errors (400, 404)

     # noqa: E501

    :param sensor: Finds the sensor by ID
    :type sensor: str

    :rtype: List[Measure]
    """
    return 'do some magic!'
