import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = date.fromisoformat("2022-09-21")
        last_service_date = date.fromisoformat("2019-08-01")
        battery1_1 = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery1_1.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = date.fromisoformat("2022-09-21")
        last_service_date = date.fromisoformat("2021-08-01")
        battery1_2 = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery1_2.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = date.fromisoformat("2022-09-21")
        last_service_date = date.fromisoformat("2018-08-21")
        battery2_1 = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery2_1.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = date.fromisoformat("2022-09-21")
        last_service_date = date.fromisoformat("2021-08-01")
        battery2_2 = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery2_2.needs_service())
