import unittest
import satellite as sat

class Test(unittest.TestCase):

  def test_canary(self):
    self.assertTrue(True)

  def test_convert_timestamp_to_UTC(self):
    self.assertEqual(str(sat.timestamp_to_UTC(1)),\
     "1970-01-01 00:00:01")
    self.assertEqual(str(sat.timestamp_to_UTC(2)),\
     "1970-01-01 00:00:02")
    self.assertEqual(str(sat.timestamp_to_UTC(60)),\
     "1970-01-01 00:01:00")
    self.assertEqual(str(sat.timestamp_to_UTC(1569130749)),\
     "2019-09-22 05:39:09")

  def test_coord_to_timezone(self):
    self.assertEqual(str(sat.coord_to_timezone(29.721670, -95.343631)),\
      "America/Chicago")
    self.assertEqual(str(sat.coord_to_timezone(40.7128, -74.0060)),\
      "America/New_York")
    self.assertEqual(str(sat.coord_to_timezone(1.3521, 103.8198)),\
      "Asia/Singapore")

  def test_timestamp_to_time_at_latlon_htx(self):
    self.assertEqual(sat.timestamp_to_time_at_latlon(1, 29.7824, -95.4695),\
     "1969-12-31 18:00:01 CST-0600")
    self.assertEqual(sat.timestamp_to_time_at_latlon(2, 29.7824, -95.4695),\
     "1969-12-31 18:00:02 CST-0600")
    self.assertEqual(sat.timestamp_to_time_at_latlon(60, 29.7824, -95.4695),\
     "1969-12-31 18:01:00 CST-0600")
    self.assertEqual(sat.timestamp_to_time_at_latlon(1569130749, 29.7824, -95.4695),\
     "2019-09-22 00:39:09 CDT-0500")

  def test_timestamp_to_time_at_latlon_nyc(self):
    self.assertEqual(sat.timestamp_to_time_at_latlon(1, 40.7128, -74.0060),\
     "1969-12-31 19:00:01 EST-0500")
    self.assertEqual(sat.timestamp_to_time_at_latlon(2, 40.7128, -74.0060),\
     "1969-12-31 19:00:02 EST-0500")
    self.assertEqual(sat.timestamp_to_time_at_latlon(60, 40.7128, -74.0060),\
     "1969-12-31 19:01:00 EST-0500")
    self.assertEqual(sat.timestamp_to_time_at_latlon(1569130749, 40.7128, -74.0060),\
     "2019-09-22 01:39:09 EDT-0400")

  def test_timestamp_to_time_at_latlon_sgp(self):
    self.assertEqual(sat.timestamp_to_time_at_latlon(1, 1.3521, 103.8198),\
     "1970-01-01 07:30:01 +0730+0730")
    self.assertEqual(sat.timestamp_to_time_at_latlon(2, 1.3521, 103.8198),\
     "1970-01-01 07:30:02 +0730+0730")
    self.assertEqual(sat.timestamp_to_time_at_latlon(60, 1.3521, 103.8198),\
     "1970-01-01 07:31:00 +0730+0730")
    self.assertEqual(sat.timestamp_to_time_at_latlon(1569130749, 1.3521, 103.8198),\
     "2019-09-22 13:39:09 +08+0800")

  def test_compute_flyover_time(self):

    lat_given, lon_given = 0, 0
    data = None

    def iss_flyover_data(lat, lon):
      nonlocal lat_given, lon_given, data
      lat_given, lon_given = lat, lon
      data = {}

      error_codes = {
        400: '400 - BAD REQUEST',
        500: '500 - INTERNAL SERVER ERROR',
        404: '404 - NOT FOUND'
      }

      status_code = None

      if (-90 <= lat_given < 0 or 0 < lat_given <= 90) and (-180 <= lon_given < 0 or 0 < lon_given <= 180):
        status_code = 200
        data = {
          'message': "success",
          'request': {
            'altitude': 100,
            'datetime': 1569977668,
            'latitude': lat_given,
            'longitude': lon_given,
            'passes': 1
          },
          'response': [
            {
              'duration': 444,
              'risetime': 1569978529
            }
          ]
        }
      elif lat_given == 0 or lon_given == 0:
        status_code = 400
##      elif NETWORK_ERROR:
##        status_code = 404
      else:
        status_code = 500

      if status_code == 200:
        return data
      raise Exception(error_codes[status_code])

    with self.subTest('compute_flyover_time_passes_lat_and_lon_to_iss_fly_over_function'):
      sat.compute_flyover_time(29.7824, -95.4695, iss_flyover_data)
      print(lat_given, lon_given)
      self.assertEqual(29.7824, lat_given)
      self.assertEqual(-95.4695, lon_given)

    with self.subTest('test_compute_flyover_time_returns_timestamp'):
      flyover_time = sat.compute_flyover_time(29.7824, -95.4695, iss_flyover_data)
      self.assertEqual(flyover_time, data['response'][0]['risetime'])

    with self.subTest('test_compute_flyover_time_handles_errors'):
      with self.assertLogs() as log:
        sat.compute_flyover_time(0, 0, iss_flyover_data)
        self.assertEquals(len(log.output), 1)
        self.assertIn('400 - BAD REQUEST', log.output[-1])
        sat.compute_flyover_time(1000, 1000, iss_flyover_data)
        self.assertEquals(len(log.output), 2)
        self.assertIn('500 - INTERNAL SERVER ERROR', log.output[-1])

