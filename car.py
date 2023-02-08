from abc import ABC

from Serviceable import Serviceable
from battery.battery import Battery
from engine.engine import Engine

class Car(Serviceable,ABC):
    def __init__(self, engine: Engine, battery: Battery) -> None:
        super().__init__()
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
        
    
