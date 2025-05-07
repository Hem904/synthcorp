from Factories.Factory_Pattern import MachineFactory
from Central_Control_System.Singleton_patterns import CentralControlSystem
from Builders.Builder_Pattern import ProductionDirector ,BudgetLineBuilder, PremiumLineBuilder
from Adapter_pattern.adapter_pattern import MachineAdapter
from Old_machine.old_machine import OldMachine

class FactoryFacade:
    def __init__(self):
        self.control_system = CentralControlSystem()
        self.machine = ["Lenseshaper", "NanoCoater", "ARchipEmbedder", "Visionclaibrater"]

    def start_production(self):
        for m in self.machine:
            machine = MachineFactory.create_machine(m)
            self.control_system.registered_machine(machine)
            print(machine.product())

        self.control_system.start_production()
        self.control_system.get_production_log()
        self.control_system.stop_production()

    def run_custom_line(self, line_type):
        if line_type == "Premium":
            builder = PremiumLineBuilder()
        elif line_type == "Budget":
            builder = BudgetLineBuilder()
        else:
            raise ValueError("broo its not here bro")

        director = ProductionDirector(builder)
        production_line = director.construct()

        print(f"\nRunning {line_type} Production Line:")
        production_line.run()


        my_old_machine = OldMachine()
        adapter = MachineAdapter(OldMachine)

        control_system = CentralControlSystem()
        control_system.registered_machine(adapter)
        print(adapter.product())
