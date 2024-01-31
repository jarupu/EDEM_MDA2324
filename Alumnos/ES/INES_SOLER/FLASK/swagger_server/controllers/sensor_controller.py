import connexion
import six

from swagger_server.models.sensor import Sensor  # noqa: E501
from swagger_server import util


def get_last_meassure_by_sensor(id_sensor):  # noqa: E501
    """

    Consultar el último registro de un sensor. # noqa: E501

    :param id_sensor: ID del sensor a consultar.
    :type id_sensor: str

    :rtype: Sensor
    """
    return 'do some magic!'


def post_last_measure_by_sensor(id_sensor, fechamuestreo, unidad, medicion):  # noqa: E501
    """Añadir nuevo registro

     # noqa: E501

    :param id_sensor: ID del sensor
    :type id_sensor: str
    :param fechamuestreo: Fecha de cuando se tomó la muestra
    :type fechamuestreo: str
    :param unidad: Unidad de medida
    :type unidad: str
    :param medicion: Tempeatura del sensor
    :type medicion: 

    :rtype: Sensor
    """
    return 'do some magic!'
