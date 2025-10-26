from Agent import Agent

class Mission:

    def __init__(self, mission_name, target_location, agent=None):
        self.mission_name = mission_name
        self.target_location = target_location
        self.agent = agent


    def assign_agent(self, agent):
        self.agent = agent

    def method_brief(self):
        txt = f"Mission: {self.mission_name}, Target: {self.target_location}, Agent: {self.agent.code_name}"
        print()
