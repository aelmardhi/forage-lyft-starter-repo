from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self) -> None :
        return        
    @abstractmethod
    def needs_service(self) -> bool:
        pass

