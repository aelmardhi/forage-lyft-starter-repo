from array import array

from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, sensor_readings: array) -> None:
        self.sensor_readings = sensor_readings

    def needs_service(self) -> bool:
        return max(self.sensor_readings) >= 0.9
