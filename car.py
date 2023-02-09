from abc import ABC

from Serviceable import Serviceable
from battery.battery import Battery
from engine.engine import Engine
from tire.tire import Tire

class Car(Serviceable,ABC):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire) -> None:
        super().__init__()
        self.engine = engine
        self.battery = battery
        self.tire = tire


    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()
        
    
