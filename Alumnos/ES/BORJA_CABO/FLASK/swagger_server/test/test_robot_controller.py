# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.robot import Robot  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRobotController(BaseTestCase):
    """RobotController integration test stubs"""

    def test_get_last_meassure_by_sensor(self):
        """Test case for get_last_measure_by_sensor_get

        
        """
        response = self.client.open(
            '/getLastMeasureBySensor/{sensor}'.format(sensor=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()