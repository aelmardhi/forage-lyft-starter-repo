from datetime import datetime
from abc import ABC

from battery.battery import Battery

class NubbinBattery(Battery,ABC):
    def __init__(self, current_date:datetime, last_service_date: datetime) -> None :
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False

