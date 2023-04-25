import unittest
from src.airport_codes import *

class TestAirportCodes(unittest.TestCase):
  
  def test_canary(self):
    self.assertTrue(True)
    
  def test_airport_codes_txt_exists(self):
    self.assertTrue(read_airport_codes('airport_codes.txt'))
  
  def test_parse_response_takes_empty_string_returns_empty_list(self):
    self.assertEqual(parse_airport_codes(""), [])
  
  def test_parse_response_takes_string_returns_list_of_codes(self):
    
    response = parse_airport_codes(read_airport_codes('airport_codes.txt'))
    
    expected_response = ["IAH", "IAD", "SFO", "STL", "BOS", "MSP"]
    
    self.assertEqual(response, expected_response)

if __name__ == '__main__':
  unittest.main()