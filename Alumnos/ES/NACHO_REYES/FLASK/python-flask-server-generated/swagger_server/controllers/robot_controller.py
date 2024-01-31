import connexion
import six

from swagger_server.models.robot import Robot  # noqa: E501
from swagger_server import util


def get_last_meassure_by_sensor(status=None):  # noqa: E501
    """Robot output

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: str

    :rtype: List[Robot]
    """
    return 'do some magic!'
