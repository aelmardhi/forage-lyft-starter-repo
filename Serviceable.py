from abc import ABC, abstractmethod

class Serviceable(ABC):
    def __init__(self) -> None :
        return        
    @abstractmethod
    def need_service(self) -> bool:
        pass

