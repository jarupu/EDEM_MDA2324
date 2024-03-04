# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.robot import Robot  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRobotsController(BaseTestCase):
    """RobotsController integration test stubs"""

    def test_add_temperature_record(self):
        """Test case for add_temperature_record

        Add a new temperature record
        """
        body = Robot()
        response = self.client.open(
            '/api/v3/robots/addLastMeassureBySensor/{sensor_id}'.format(sensor_id='sensor_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_temperature_records(self):
        """Test case for get_temperature_records

        Get temperature records for a specific sensor ID
        """
        response = self.client.open(
            '/api/v3/robots/getLastTemperatureRecord/{sensor_id}'.format(sensor_id='sensor_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
