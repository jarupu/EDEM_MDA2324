# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.sensor import Sensor  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSensorController(BaseTestCase):
    """SensorController integration test stubs"""

    def test_get_last_meassure_by_sensor(self):
        """Test case for get_last_meassure_by_sensor

        
        """
        response = self.client.open(
            '/v2/LastMeasureBySensor/{id_sensor}'.format(id_sensor='id_sensor_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_last_measure_by_sensor(self):
        """Test case for post_last_measure_by_sensor

        Añadir nuevo registro
        """
        query_string = [('id_sensor', 'id_sensor_example'),
                        ('fechamuestreo', 'fechamuestreo_example'),
                        ('unidad', 'unidad_example'),
                        ('medicion', 8.14)]
        response = self.client.open(
            '/v2/postLastMeasureBySensor',
            method='POST',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
