import unittest
import FlightTimeCalculator as ft
import datetime


class FlightTimeCalculatorTestCase(unittest.TestCase):
    def setUp(self):
        schedDepTime = datetime.datetime.strptime('2017-01-01T09:35:00',"%Y-%m-%dT%H:%M:%S")
        actDeptTime = datetime.datetime.strptime('2017-01-01T09:30:00',"%Y-%m-%dT%H:%M:%S")
        schedArrTime = datetime.datetime.strptime('2017-01-01T10:54:00',"%Y-%m-%dT%H:%M:%S")
        actArrTime = datetime.datetime.strptime('2017-01-01T10:52:00',"%Y-%m-%dT%H:%M:%S")
        depTimeZone = "America/Denver"
        arrTimeZone = "America/Los_Angeles"
        self.calculator = ft.FlightTimeCalculator("WN", 8, schedDepTime, actDeptTime, schedArrTime, actArrTime,
                                                  depTimeZone, arrTimeZone)

    def test_pass_parameters(self):
        self.assertEqual(self.calculator.airlineCode,"WN")
        self.assertEqual(self.calculator.flightNum, 8)

    def test_calculate_time_diff_time1_gt_time2(self):
        time1 = datetime.datetime(2017, 12, 12, 23, 57, 00)
        time2 = datetime.datetime(2017, 12, 12, 23, 48, 00)
        self.assertEqual(self.calculator.diffInTime(time1,time2), 9)

    def test_calculate_time_diff_time2_gt_time1(self):
        time1 = datetime.datetime(2017, 12, 12, 23, 48, 00)
        time2 = datetime.datetime(2017, 12, 12, 23, 57, 00)
        self.assertEqual(self.calculator.diffInTime(time1,time2), 9)

    def test_calculate_arrival_difference(self):
        self.assertEqual(self.calculator.diffInArrivalTimes(), 2)

    def test_calculate_departure_difference(self):
        self.assertEqual(self.calculator.diffInDepartureTimes(), 5)

    def test_calculate_total_flight_duration(self):
        self.assertEqual(self.calculator.getFlightDuration(), 142)

    def test_calculate_gmt_time(self):
        self.assertEqual(datetime.datetime(2017, 1, 1, 16, 30, 00),
                         self.calculator.getGMTTime(datetime.datetime(2017, 1, 1, 9, 30, 00), "America/Denver"))

    def test_calculate_gmt_time_dst(self):
        self.assertEqual(datetime.datetime(2017, 6, 10, 15, 30, 00),
                         self.calculator.getGMTTime(datetime.datetime(2017, 6, 10, 9, 30, 00), "America/Denver"))

    def test_get_FlightSummary(self):
        self.assertEqual(self.calculator.getFlightSummary(),("WN 8",5, 2, 142))

if __name__ == '__main__':
    unittest.main()
