import unittest


from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensor_readings = [.8, 1, .6, .9]
        tire = OctoprimeTire(sensor_readings)
        self.assertTrue(tire.needs_service())
    

    def test_tire_should_not_be_serviced(self):
        sensor_readings = [.5, .7, .6, .1]
        tire = OctoprimeTire(sensor_readings)
        self.assertFalse(tire.needs_service())
