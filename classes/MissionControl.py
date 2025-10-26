import Report

class MissionControl:

    def __init__(self, report):
        self.report = report
        self.immediate_response = 4
        self.monitor_closely = 3

    def analyze_report(self):

        if self.report.get_urgency_level() >= self.immediate_response:
            print("Immediate response required.")
        elif self.report.get_urgency_level() == self.immediate_response:
            print("High priority. Monitor closely.")
        else:
            print("Routine analysis.")
