import connexion
import six

from swagger_server.models.robot import Robot  # noqa: E501
from swagger_server import util


def add_temperature_record(body, sensor_id):  # noqa: E501
    """Add a new temperature record

    Add a new temperature record for a specific sensor ID # noqa: E501

    :param body: Temperature record data
    :type body: dict | bytes
    :param sensor_id: ID of the sensor
    :type sensor_id: str

    :rtype: Robot
    """
    if connexion.request.is_json:
        body = Robot.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_temperature_records(sensor_id):  # noqa: E501
    """Get temperature records for a specific sensor ID

    Get the temperature records for a specific sensor ID # noqa: E501

    :param sensor_id: ID of the sensor
    :type sensor_id: str

    :rtype: List[Robot]
    """
    return 'do some magic!'
