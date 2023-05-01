import unittest
from src.worldtime_unixtime import *
from unittest.mock import patch

class TestWorldTimeUnixtime(unittest.TestCase):
  
    def test_canary(self):
        self.assertTrue(True)

    def test_worldtime_unixtime_api_returns_string(self):
        self.assertEqual(type(get_response()), dict)
    
    def test_parse_response_takes_string_returns_unixtime(self):
        
        response = {'abbreviation': 'CDT', 'client_ip': '129.7.0.62', 'datetime': '2023-05-01T13:08:41.078788-05:00', 'day_of_week': 1, 'day_of_year': 121, 'dst': True, 'dst_from': '2023-03-12T08:00:00+00:00', 'dst_offset': 3600, 'dst_until': '2023-11-05T07:00:00+00:00', 'raw_offset': -21600, 'timezone': 'America/Chicago', 'unixtime': 1682964521, 'utc_datetime': '2023-05-01T18:08:41.078788+00:00', 'utc_offset': '-05:00', 'week_number': 18}
        
        self.assertEqual(parse_response(response), 1682964521)
        
    def test_parse_response_raises_exception_given_empty_string(self):
        with self.assertRaisesRegex(Exception, "Invalid response from Worldtime API"): parse_response("")
        
    def test_parse_response_raises_exception_given_empty_dict(self):
        with self.assertRaisesRegex(Exception, "Invalid response from Worldtime API"): parse_response({})
    
    @patch('src.worldtime_unixtime.get_response')
    @patch('src.worldtime_unixtime.parse_response')
    def test_get_unixtime_calls_get_response_and_parse(self, parse_response, get_response):
        
        response = {'abbreviation': 'CDT', 'client_ip': '129.7.0.62', 'datetime': '2023-05-01T13:08:41.078788-05:00', 'day_of_week': 1, 'day_of_year': 121, 'dst': True, 'dst_from': '2023-03-12T08:00:00+00:00', 'dst_offset': 3600, 'dst_until': '2023-11-05T07:00:00+00:00', 'raw_offset': -21600, 'timezone': 'America/Chicago', 'unixtime': 1682964521, 'utc_datetime': '2023-05-01T18:08:41.078788+00:00', 'utc_offset': '-05:00', 'week_number': 18}

        get_response.return_value = response
        parse_response.return_value = 1682964521

        self.assertEqual(get_unixtime(), 1682964521)
    
        get_response.assert_called()
        parse_response.assert_called_with(response)
        
    @patch('src.worldtime_unixtime.get_response')
    def test_get_unixtime_passes_exception_from_get_response_to_caller(self, get_response):

        get_response.side_effect = Exception

        with self.assertRaises(Exception):
            get_unixtime()

if __name__ == '__main__':
  unittest.main()
