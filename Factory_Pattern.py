from abc import ABC, abstractmethod

#Base class
class Machine(ABC):
    @abstractmethod
    def product(self):
        pass

#Concrete classes
class LenseshaperMachine(Machine):
    def product(self):
        return "Lenseshaper Machine is shaping the lenses"
    
class NanoCoaterMachine(Machine):
    def product(self):
        return "NanoCoater Machine is coating the lenses"
    
class ARchipEmbedderMachine(Machine):
    def product(self):
        return "ARchip Embedder Machine is embedding the ARchip"
    
class VisionclaibraterMachine(Machine):
    def product(self):
        return "Visionclaibrater Machine is calibrating the lenses"
    

#Factory Pattern
class MachineFactory:
    @staticmethod
    def create_machine(machine_type):
        if machine_type == "Lenseshaper":
            return LenseshaperMachine()
        elif machine_type == "NanoCoater":
            return NanoCoaterMachine()
        elif machine_type == "ARchipEmbedder":
            return ARchipEmbedderMachine()
        elif machine_type == "Visionclaibrater":
            return VisionclaibraterMachine()
        else:
            raise ValueError("HUM PE NOO HAAAA")

