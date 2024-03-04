import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def sensor_get(sensor):  # noqa: E501
    """Obtiene la información almacenada de los datos de un sensor

     # noqa: E501

    :param sensor: Identificador del sensor
    :type sensor: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'
