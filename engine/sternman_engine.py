from abc import ABC

from engine.engine import Engine


class SternmanEngine(Engine, ABC):
    def __init__(self, warning_light_on: bool) -> None:
        super().__init__()
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        if self.warning_light_on:
            return True
        else:
            return False
