# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.robot import Robot  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRobotController(BaseTestCase):
    """RobotController integration test stubs"""

    def test_get_last_meassure_by_sensor(self):
        """Test case for get_last_meassure_by_sensor

        Robot output
        """
        query_string = [('status', 'available')]
        response = self.client.open(
            '/api/v3/robot/getLastMeassureBySensor',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
