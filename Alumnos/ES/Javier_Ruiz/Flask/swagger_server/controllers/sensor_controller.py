import connexion
import six
import random

from swagger_server.models.measure import Measure  # noqa: E501
from swagger_server import util


def get_last_measure_by_sensor(sensor):  # noqa: E501
    """Get the last temperature measure by sensor ID

    Retrieve the latest temperature measurement for a given sensor ID # noqa: E501

    :param sensor: Sensor ID
    :type sensor: str

    :rtype: Measure
    """
    return {
        "code": sensor,
        "fechamuestreo": "2024-02-15T12:30:00Z",
        "unidad": "{:.1f} Cº".format(random.uniform(1, 30)),
        "medicion": 0.75
    }
