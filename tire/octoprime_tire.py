
from array import array

from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, sensor_readings: array) -> None:
        self.sensor_readings = sensor_readings

    def needs_service(self) -> bool:
        return sum(self.sensor_readings) >= 3.0
