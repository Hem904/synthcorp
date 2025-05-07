from Factories.Factory_Pattern import MachineFactory
from Central_Control_System.Singleton_patterns import CentralControlSystem
from Builders.Builder_Pattern import ProductionDirector, BudgetLineBuilder, PremiumLineBuilder
from Facade.Factory_facade import FactoryFacade
from Adapter_pattern.adapter_pattern import MachineAdapter
from Old_machine.old_machine import OldMachine
from Decorator_Pattern.Decorator import DecoratorMachine, RealTimeErrorDetectionDecorator, EnergyEfficientOperationModeDecorator
from Observer_pattern.observable_machine import ObservableMachine
from Observer_pattern.Engineer_observer import EngineerObserver
from Strategy_pattern.production_strategy import ProductionContext, HighDemandStrategy, LowDemandStrategy, ResourceEfficientStrategy


# Factory Pattern
def factory_pattern():
    print("\n--- Factory Pattern ---")
    control_system = CentralControlSystem()
    machine_names = ["Lenseshaper", "NanoCoater", "ARchipEmbedder", "Visionclaibrater"]

    for m in machine_names:
        machine = MachineFactory.create_machine(m)
        control_system.registered_machine(machine)
        print(machine.product())

# Singleton Pattern
def singleton_pattern():
    print("\n--- Singleton Pattern ---")
    control_system = CentralControlSystem()
    control_system.start_production()
    control_system.get_production_log()
    control_system.stop_production()

# Builder Pattern
def builder_pattern():
    print("\n--- Custom Production Lines (Builder Pattern) ---")
    # Create Premium Production Line
    premium_builder = PremiumLineBuilder()
    premium_director = ProductionDirector(premium_builder)
    premium_line = premium_director.construct()

    # Create Budget Production Line
    budget_builder = BudgetLineBuilder()
    budget_director = ProductionDirector(budget_builder)
    budget_line = budget_director.construct()

    # Run Production Lines
    print("\nRunning Premium Production Line:")
    premium_line.run()

    print("\nRunning Budget Production Line:")
    budget_line.run()

# Facade Pattern
def facade_pattern():
    print("\n--- Facade Pattern ---")
    facade = FactoryFacade()
    facade.start_production()
    facade.run_custom_line("Premium")
    facade.run_custom_line("Budget")

# Adapter Pattern
def adapter_pattern():
    print("\n--- Adapter Pattern ---")
    my_old_machine = OldMachine()
    adapter = MachineAdapter(my_old_machine)

    control_system = CentralControlSystem()
    control_system.registered_machine(adapter)
    print(adapter.product())

# Decorator Pattern
def decorator_pattern():
    print("\n--- Decorator Pattern ---")
    for m in ["Lenseshaper", "NanoCoater", "ARchipEmbedder", "Visionclaibrater"]:
        machine = MachineFactory.create_machine(m)

        # Apply decorators
        decorated_machine = RealTimeErrorDetectionDecorator(machine)
        decorated_machine = EnergyEfficientOperationModeDecorator(decorated_machine)

        control_system = CentralControlSystem()
        control_system.registered_machine(decorated_machine)
        print(decorated_machine.product())

# In your Machine class
class Machine:
    def product(self):
        print("Machine is processing...")  # Simulated processing

    def malfunction(self):
        print("Machine malfunctioning...")  # Simulate malfunction

    def maintenance_required(self):
        print("Machine requires maintenance...")  # Simulate maintenance need


# Observer Pattern
def observer_pattern():
    print("\n--- Observer Pattern ---")
    # Create machine and observable machine
    machine = Machine()
    observable_machine = ObservableMachine(machine)

    # Create and add EngineerObserver
    engineer = EngineerObserver()
    observable_machine.add_observer(engineer)

    # Trigger machine processing
    observable_machine.product()

    # Simulate a malfunction
    observable_machine.malfunction()

    # Simulate a maintenance requirement
    observable_machine.maintenance_required()


def startegy_pattern():
    print("\n--- Strategy Pattern ---")
    market_demand = "high"  # You can dynamically set this based on market conditions
    resources_available = "limited"  # This could also be dynamically decided

    # Choose the appropriate strategy based on the conditions
    if market_demand == "high":
        production_strategy = HighDemandStrategy()
    elif market_demand == "low":
        production_strategy = LowDemandStrategy()
    else:
        production_strategy = ResourceEfficientStrategy()

    # Create a ProductionContext object with the selected strategy
    production_context = ProductionContext(production_strategy)

    # Execute the selected production strategy
    print(production_context.execute_production())

if __name__ == "__main__":
    factory_pattern()
    singleton_pattern()
    builder_pattern()
    facade_pattern()
    adapter_pattern()
    decorator_pattern()
    observer_pattern()
    startegy_pattern()
