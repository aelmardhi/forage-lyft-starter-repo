import unittest


from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensor_readings = [.5, .7, .6, .9]
        tire = CarriganTire(sensor_readings)
        self.assertTrue(tire.needs_service())
    

    def test_tire_should_not_be_serviced(self):
        sensor_readings = [.5, .7, .6, .1]
        tire = CarriganTire(sensor_readings)
        self.assertFalse(tire.needs_service())
