from Old_machine.old_machine import OldMachine

class MachineAdapter:
    def __init__(self, old_machine):
        self.old_machine = old_machine

    def product(self):
        # Adapts the legacy `production()` method to `product()`
        return self.old_machine.production()
