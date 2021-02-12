import unittest
import src.satellite as sat

class Test_satellite(unittest.TestCase):

  def test_canary(self):
    self.assertTrue(True)

  def test_convert_timestamp_to_UTC(self):
    self.assertEqual(str(sat.timestamp_to_UTC(1)),\
     '1970-01-01 00:00:01')
    self.assertEqual(str(sat.timestamp_to_UTC(2)),\
     '1970-01-01 00:00:02')
    self.assertEqual(str(sat.timestamp_to_UTC(60)),\
     '1970-01-01 00:01:00')
    self.assertEqual(str(sat.timestamp_to_UTC(1569130749)),\
     '2019-09-22 05:39:09')

  def test_coord_to_timezone(self):
    self.assertEqual(str(sat.coord_to_timezone(29.721670, -95.343631)),\
      'America/Chicago')
    self.assertEqual(str(sat.coord_to_timezone(40.7128, -74.0060)),\
      'America/New_York')
    self.assertEqual(str(sat.coord_to_timezone(1.3521, 103.8198)),\
      'Asia/Singapore')

  def test_timestamp_to_time_at_latlon_htx(self):
    self.assertEqual(sat.timestamp_to_time_at_latlon(1, 29.7824, -95.4695),\
     ' 6:00PM')
    self.assertEqual(sat.timestamp_to_time_at_latlon(2, 29.7824, -95.4695),\
     ' 6:00PM')
    self.assertEqual(sat.timestamp_to_time_at_latlon(60, 29.7824, -95.4695),\
     ' 6:01PM')
    self.assertEqual(sat.timestamp_to_time_at_latlon(1569130749, 29.7824, -95.4695),\
     '12:39AM')

  def test_timestamp_to_time_at_latlon_nyc(self):
    self.assertEqual(sat.timestamp_to_time_at_latlon(1, 40.7128, -74.0060),\
     ' 7:00PM')
    self.assertEqual(sat.timestamp_to_time_at_latlon(2, 40.7128, -74.0060),\
     ' 7:00PM')
    self.assertEqual(sat.timestamp_to_time_at_latlon(60, 40.7128, -74.0060),\
     ' 7:01PM')
    self.assertEqual(sat.timestamp_to_time_at_latlon(\
      1569130749, 40.7128, -74.0060), ' 1:39AM')

  def test_timestamp_to_time_at_latlon_sgp(self):
    self.assertEqual(sat.timestamp_to_time_at_latlon(1, 1.3521, 103.8198),\
     ' 7:30AM')
    self.assertEqual(sat.timestamp_to_time_at_latlon(2, 1.3521, 103.8198),\
     ' 7:30AM')
    self.assertEqual(sat.timestamp_to_time_at_latlon(60, 1.3521, 103.8198),\
     ' 7:31AM')
    self.assertEqual(sat.timestamp_to_time_at_latlon(\
      1569130749, 1.3521, 103.8198), ' 1:39PM')

  def test_timestamp_to_time_at_latlon_raises_error(self):
    time = 'Not an int.'

    with self.assertRaises(Exception):
      sat.timestamp_to_time_at_latlon(time, 1.3521, 103.8198)

  def test_compute_time_of_flyover_passes_lat_lan_to_iss_flyover(self):
    lat_given, lon_given = 0, 0

    def iss_flyover_time(lat, lon, get_data_from_url, parse_json_data):
      nonlocal lat_given, lon_given
      lat_given, lon_given = lat, lon
      return 2

    get_data_from_url = lambda parameters: 2
    parse_json_data = lambda parameters: 3

    sat.compute_time_of_flyover(1.3, 103.4, iss_flyover_time,\
        get_data_from_url, parse_json_data)

    self.assertEqual(1.3, lat_given)
    self.assertEqual(103.4, lon_given)

  def test_compute_time_of_flyover_returns_time_based_on_timestamp_returned_by_iss_flyover(self):
    iss_flyover_time = lambda lat, lon, get_data_from_url, parse_json_data: 2
    get_data_from_url = lambda parameters: 2
    get_data_from_url = lambda parameters: 2
    parse_json_data = lambda parameters: 3
    parse_json_data = lambda parameters: 3

    result = sat.compute_time_of_flyover(1.3521, 103.8198, iss_flyover_time,\
        get_data_from_url, parse_json_data)

    self.assertEqual(' 7:30AM', result)

  def test_compute_time_of_flyover__gracefully_reports_error_from_webservice(self):
    err = ValueError('lat out of range')

    def iss_flyover_time(lat, lon, get_data_from_url, parse_json_data):
      raise err

    get_data_from_url = lambda parameters: 2
    parse_json_data = lambda parameters: 3

    result = sat.compute_time_of_flyover(1.3, 103.4, iss_flyover_time,\
        get_data_from_url, parse_json_data)
    self.assertEqual(err, result)

  def test_compute_time_of_flyover__gracefully_reports_network_failure(self):
    err = Exception('Network Error')

    def iss_flyover_time(lat, lon, get_data_from_url, parse_json_data):
      raise err

    get_data_from_url = lambda parameters: 2
    parse_json_data = lambda parameters: 3

    result = sat.compute_time_of_flyover(1.3, 103.4, iss_flyover_time,\
        get_data_from_url, parse_json_data)

    self.assertEqual(err, result)

