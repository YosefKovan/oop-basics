
class Agent:

    def __init__(self, code_name, clearance_level):
        self.code_name = code_name
        self.clearance_level = clearance_level

    def a_method_report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level : {self.clearance_level}")


