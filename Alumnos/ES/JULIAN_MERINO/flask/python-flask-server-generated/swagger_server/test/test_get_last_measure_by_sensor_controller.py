# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.measure import Measure  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetLastMeasureBySensorController(BaseTestCase):
    """GetLastMeasureBySensorController integration test stubs"""

    def test_get_temp(self):
        """Test case for get_temp

        Obtains ID, date, unit, and temperature measurement, and returns Measure (200) or errors (400, 404)
        """
        response = self.client.open(
            '/getLastMeasureBySensor/{sensor}'.format(sensor='sensor_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
