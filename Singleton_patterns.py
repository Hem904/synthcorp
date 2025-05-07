class CentralControlSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CentralControlSystem, cls).__new__(cls)
            cls._instance._init_state()
        return cls._instance
    
    def _init_state(self):
        self.machines = []
        self.production_log = []
        self.status = "Idle"

    def registered_machine(self, machine):
        self.machines.append(machine)
        print(f"Machine {machine.__class__.__name__} registered")

    def start_production(self):
        self.status = "Active"
        for machine in self.machines:
            machine.product()
            self.production_log.append(machine.product())
        print("Production started")

    def stop_production(self):
        self.status = "Stoped"
        print("Production stopped")

    def get_production_log(self):
       for log in self.production_log:
           print("Log-",log)
    