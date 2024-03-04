# swagger_client.SensorApi

All URIs are relative to *https://ejemploSL/sensor/getLastMeassureBySensor/{sensor}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sensor_get**](SensorApi.md#sensor_get) | **GET** /{sensor} | Obtiene la información almacenada de los datos de un sensor

# **sensor_get**
> InlineResponse200 sensor_get(sensor)

Obtiene la información almacenada de los datos de un sensor

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SensorApi()
sensor = 'sensor_example' # str | Identificador del sensor

try:
    # Obtiene la información almacenada de los datos de un sensor
    api_response = api_instance.sensor_get(sensor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorApi->sensor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor** | **str**| Identificador del sensor | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

