import unittest
import TimeZoneCalc
import os

class TimeZoneCalculatorTestCase(unittest.TestCase):
    def setUp(self):
        file = open("testfile.csv", "w")
        file.write("Airport code,Time zone\n")
        file.write("SLC,America/Denver")
        file.close()
        self.timezone = TimeZoneCalc.TimeZoneCalc("testfile.csv", "Airport code", "Time zone")

    def test_get_timezone(self):
        AirportCode = "SLC"
        self.assertEqual(self.timezone.getTimeZone(AirportCode),"America/Denver")

    def tearDown(self):
        os.remove("testfile.csv")

if __name__ == '__main__':
    unittest.main()
