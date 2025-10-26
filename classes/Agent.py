
class Agent:

    def __init__(self, code_name, clearance_level):
        self.code_name = code_name
        self.__clearance_level = clearance_level

    def a_method_report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level : {self.clearance_level}")

    def get_clearance_level(self):
        return self.__clearance_level

    def set_clearance_level(self, clearance_level):

        if 5 < clearance_level < 1:
            print("Unable to to add code only smaller then 5 and larger then 1")
            return

        self.__clearance_level = clearance_level

    @staticmethod
    def encrypt_message(msg):
        return msg[::-1]

    @staticmethod
    def log_transmission(agent_name, message):
        print( f"{agent_name} sent encrypted message: {message}")

