from abc import ABC, abstractmethod
import engine
import Battery 


class Car(engine, Battery):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return True

    @abstractmethod
    def needs_service(self):
        pass
