import unittest
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine1_1 = CapuletEngine(current_mileage=30001, last_service_mileage=0)
        self.assertTrue(engine1_1.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine1_2 = CapuletEngine(current_mileage=30000, last_service_mileage=0)
        self.assertFalse(engine1_2.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine2_1 = WilloughbyEngine(current_mileage=60001, last_service_mileage=0)
        self.assertTrue(engine2_1.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine2_2 = WilloughbyEngine(current_mileage=60000, last_service_mileage=0)
        self.assertFalse(engine2_2.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine3_1 = SternmanEngine(warning_light_is_on=1)
        self.assertTrue(engine3_1.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine3_2 = SternmanEngine(warning_light_is_on=0)
        self.assertFalse(engine3_2.needs_service())
