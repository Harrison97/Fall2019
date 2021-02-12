import unittest
import satellite_api as api
import requests
from mock import patch

class Test_satellite_api(unittest.TestCase):

  def test_canary(self):
    self.assertTrue(True)

  def test_parse_json_data1(self):
    data = {
      'message': 'success',
      'request': {
        'altitude': 100,
        'datetime': 1570133865,
        'latitude': 29.72167,
        'longitude': -95.343631,
        'passes': 1
      },
      'response': [
        {
          'duration': 421,
          'risetime': 1570138073
        }
      ]
    }

    result = api.parse_json_data(data)
    self.assertEqual(1570138073, result)

  def test_parse_json_data2(self):
    data = {
      'message': 'success',
      'request': {
        'altitude': 100,
        'datetime': 1570135647,
        'latitude': 1.0,
        'longitude': 1.0,
        'passes': 1
      },
      'response': [
        {
          'duration': 463,
          'risetime': 1570139707
        }
      ]
    }

    result = api.parse_json_data(data)
    self.assertEqual(1570139707, result)

  def test_parse_json_data3(self):
    data = {
      'message': 'success',
      'request': {
        'altitude': 13,
        'datetime': 2570342547,
        'latitude': 23,
        'longitude': 43,
        'passes': 1
      },
      'response': [
        {
          'duration': 43,
          'risetime': 3746574909
        }
      ]
    }

    result = api.parse_json_data(data)
    self.assertEqual(3746574909, result)

  def test_parse_json_data4(self):
    data = {
      'message': 'failure',
      'reason': 'Latitude must be number between -90.0 and 90.0'
    }

    result = api.parse_json_data(data)
    self.assertEqual('Latitude must be number between -90.0 and 90.0', result)

  def test_parse_json_data5(self):
    data = {
      'message': 'failure',
      'reason': 'Longitue must be number between -180.0 and 180.0'
    }

    result = api.parse_json_data(data)
    self.assertEqual('Longitue must be number between -180.0 and 180.0', result)

  def test_fetch_iss_flyover_data_passes_get_data_from_url_response_to_parse_json_data(self):
    data_given = 0

    get_data_from_url = lambda parameters: 3

    def parse_json_data(data):
      nonlocal data_given
      data_given = data
      return 1570138073

    api.fetch_iss_flyover_data(10, 100, get_data_from_url, parse_json_data)
    self.assertEqual(data_given, 3)

  def test_fetch_iss_flyover_data_returns_same_time_as_get_timestamp(self):
    data = {
      'message': 'success',
      'request': {
        'altitude': 13,
        'datetime': 2570342547,
        'latitude': 23,
        'longitude': 43,
        'passes': 1
      },
      'response': [
        {
          'duration': 43,
          'risetime': 3746574909
        }
      ]
    }

    get_data_from_url = lambda parameters: data

    self.assertEqual(api.fetch_iss_flyover_data(10, 100, get_data_from_url,\
        api.parse_json_data), 3746574909)

  def test_fetch_iss_flyover_data_returns_error_returned_by_parse(self):
    data = {
      'message': 'failure',
      'reason': 'Latitude must be number between -90.0 and 90.0'
    }

    get_data_from_url = lambda parameters: data

    self.assertEquals(api.fetch_iss_flyover_data(100, 1, get_data_from_url,\
        api.parse_json_data), 'Latitude must be number between -90.0 and 90.0')

    data = {
      'message': 'failure',
      'reason': 'Longitue must be number between -180.0 and 180.0'
    }

    self.assertEquals(api.fetch_iss_flyover_data(1, 200, get_data_from_url,\
        api.parse_json_data), 'Longitue must be number between -180.0 and 180.0')

  @patch('requests.get')
  def test_fetch_iss_flyover_data_returns_exception(self, m_get):
    parse_json_data = lambda data: 2
    m_get.return_value.status_code = 404

    self.assertEquals(str(api.fetch_iss_flyover_data(10, 100, api.get_data_from_url,\
        parse_json_data)), '404 Error')

    def get(*args, **kwargs):
      raise Exception
    m_get.side_effect = get

    self.assertRaises(Exception, api.fetch_iss_flyover_data(10, 100, api.get_data_from_url,\
        parse_json_data))

  def test_fetch_iss_flyover_data_returns_timestamp(self):
    self.assertGreater(api.fetch_iss_flyover_data(1, 1, api.get_data_from_url,\
        api.parse_json_data), 1570181553)

