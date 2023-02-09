
from datetime import datetime
from array import array

from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class CarFactory():
    @staticmethod
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_sensor_readings: array) -> Car:
        battery = SpindlerBattery(current_date, last_service_date)
        engine = CapuletEngine( current_mileage, last_service_mileage)
        tire = CarriganTire(tire_sensor_readings)
        return Car(engine, battery, tire)
    
    @staticmethod
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_sensor_readings: array)-> Car:
        battery = SpindlerBattery(current_date, last_service_date)
        engine = WilloughbyEngine( current_mileage, last_service_mileage)
        tire = CarriganTire(tire_sensor_readings)
        return Car(engine, battery, tire)
    
    @staticmethod
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool, tire_sensor_readings: array) -> Car:
        battery = SpindlerBattery(current_date, last_service_date)
        engine = SternmanEngine( warning_light_on)
        tire = CarriganTire(tire_sensor_readings)
        return Car(engine, battery, tire)
    
    @staticmethod
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_sensor_readings: array) -> Car:
        battery = NubbinBattery(current_date, last_service_date)
        engine = WilloughbyEngine( current_mileage, last_service_mileage)
        tire = OctoprimeTire(tire_sensor_readings)
        return Car(engine, battery, tire)
    
    @staticmethod
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_sensor_readings: array) -> Car:
        battery = NubbinBattery(current_date, last_service_date)
        engine = CapuletEngine( current_mileage, last_service_mileage)
        tire = CarriganTire(tire_sensor_readings)
        return Car(engine, battery, tire)
