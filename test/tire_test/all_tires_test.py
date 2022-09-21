import unittest
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_grades = [0.1, 0.3, 0.2, 0.9]
        tire1_1 = CarriganTire(tire_grades)
        self.assertTrue(tire1_1.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_grades = [0.3, 0.4, 0.2, 0.8]
        tire1_2 = CarriganTire(tire_grades)
        self.assertFalse(tire1_2.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_grades = [1, 0.3, 1, 1]
        tire2_1 = OctoprimeTire(tire_grades)
        self.assertTrue(tire2_1.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_grades = [0.2, 0.4, 0.5, 1]
        tire2_2 = OctoprimeTire(tire_grades)
        self.assertFalse(tire2_2.needs_service())
