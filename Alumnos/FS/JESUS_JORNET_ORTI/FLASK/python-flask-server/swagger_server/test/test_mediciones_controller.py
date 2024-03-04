# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.medicion import Medicion  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMedicionesController(BaseTestCase):
    """MedicionesController integration test stubs"""

    def test_get_last_measure_by_sensor(self):
        """Test case for get_last_measure_by_sensor

        Obtiene la última medición registrada por un sensor específico.
        """
        response = self.client.open(
            '/v1/getLastMeasureBySensor/{sensorId}'.format(sensorId='sensorId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
