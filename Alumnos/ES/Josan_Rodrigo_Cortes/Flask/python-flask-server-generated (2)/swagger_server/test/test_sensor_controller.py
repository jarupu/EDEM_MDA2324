# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSensorController(BaseTestCase):
    """SensorController integration test stubs"""

    def test_sensor_get(self):
        """Test case for sensor_get

        Obtiene la información almacenada de los datos de un sensor
        """
        response = self.client.open(
            '/sensor/getLastMeassureBySensor/{sensor}/{sensor}'.format(sensor='sensor_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
